import yaml
import markdown
from bs4 import BeautifulSoup
from mrkdwn_analysis import MarkdownAnalyzer


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


# --------------------------------------------------------------------------
# 1. Helper function to convert Markdown cells to plain text
# --------------------------------------------------------------------------
def markdown_to_plain_text(md_content):
    """
    Converts a small piece of Markdown text to plain text.
    """
    html_content = markdown.markdown(md_content)
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text()


# --------------------------------------------------------------------------
# 2. Param generator for "hourly" or "current"
#    (Both will reference the same table in this new file.)
# --------------------------------------------------------------------------
def array_param_generator(
    param_name, required, description, enum_items=None, default_val=None
):
    """
    Generates a parameter entry for a param of type 'string array'
    (e.g. 'hourly' or 'current'), with enumerations as objects:
      { "value": ..., "unit": ..., "description": ... }.
    """
    return {
        "name": param_name,
        "in": "query",
        "required": required,
        "description": description or "",
        "explode": False,
        "schema": {
            "type": "array",
            "items": {"type": "string", "enum": enum_items or []},
        },
        # We'll add "default" below if applicable
    }


# --------------------------------------------------------------------------
# 3. The main function to convert recognized tables to a YAML parameter list
# --------------------------------------------------------------------------
def convert_markdown_tables_to_yaml(file_path: str):
    # 3.1. Read and parse the Markdown file
    doc = MarkdownAnalyzer(file_path)
    tables = doc.identify_tables().get("Table", [])

    # 3.2. Identify the two relevant tables
    parameter_table = None
    variable_table = None  # This will be used for both hourly & current

    for table in tables:
        header = [h.lower() for h in table.get("header", [])]

        # Check for the Parameter table
        if header == ["parameter", "format", "required", "default", "description"]:
            parameter_table = table

        # Check for the Variable table (for both hourly & current)
        if header == ["variable", "valid time", "unit", "description"]:
            variable_table = table

    if parameter_table is None:
        raise ValueError(
            "Could not find the Parameter table with header: "
            "['Parameter', 'Format', 'Required', 'Default', 'Description']"
        )

    if variable_table is None:
        raise ValueError(
            "Could not find the Variable table with header: "
            "['Variable', 'Valid time', 'Unit', 'Description']"
        )

    # 3.3. Build the enum items from the Variable table
    #      (Same for both 'hourly' and 'current' in this new file.)
    enum_items = []
    for row in variable_table["rows"]:
        # row = ["temperature_2m", "hourly", "°C", "Air temperature at 2 m"]
        if len(row) >= 4:
            variable = markdown_to_plain_text(row[0]).strip()  # "temperature_2m"
            unit = markdown_to_plain_text(row[2]).strip()  # "°C"
            desc = markdown_to_plain_text(row[3]).strip()  # "Air temperature at 2 m"
            if variable:
                enum_items.append(
                    {"value": variable, "unit": unit, "description": desc}
                )

    # 3.4. Build a list of parameter entries from the Parameter table
    parameters_yaml = []

    for row in parameter_table["rows"]:
        param_name = markdown_to_plain_text(row[0]).strip()
        format_str = markdown_to_plain_text(row[1]).strip()
        required_str = markdown_to_plain_text(row[2]).strip()

        # default_val & description might be missing if fewer columns
        default_val = ""
        description = ""
        if len(row) >= 5:
            default_val = markdown_to_plain_text(row[3]).strip()
            description = markdown_to_plain_text(row[4]).strip()
        elif len(row) == 4:
            description = markdown_to_plain_text(row[3]).strip()

        required = required_str.lower() == "yes"

        # 3.5. Decide how to build this param's schema
        if format_str.lower() == "string array" and param_name.lower() in [
            "hourly",
            "current",
        ]:
            print(param_name)
            # Both "hourly" and "current" use the SAME table in this new file
            param_entry = array_param_generator(
                param_name=param_name,
                required=required,
                description=description,
                enum_items=enum_items.copy(),
                default_val=default_val,
            )
            if default_val:
                # If there's a default, add it under schema
                param_entry["schema"]["default"] = default_val

        elif format_str.lower() == "string array":
            # A generic fallback for any other array param
            param_entry = {
                "name": param_name,
                "in": "query",
                "required": required,
                "description": description,
                "explode": False,
                "schema": {"type": "array", "items": {"type": "string"}},
            }
            if default_val:
                param_entry["schema"]["default"] = default_val

        else:
            # Non-array param fallback
            param_entry = {
                "name": param_name,
                "in": "query",
                "required": required,
                "description": description,
                "schema": {},
            }

            # Handle common data types
            fmt_lower = format_str.lower()
            if fmt_lower in ("float", "double", "number"):
                param_entry["schema"]["type"] = "number"
                param_entry["schema"]["format"] = "float"  # or "double"
            elif fmt_lower in ("string", "text"):
                param_entry["schema"]["type"] = "string"
            elif fmt_lower.startswith("yyyy-"):
                param_entry["schema"]["type"] = "string"
                param_entry["schema"]["format"] = "date"  # or "date-time"
            else:
                # fallback
                param_entry["schema"]["type"] = "string"

            if default_val:
                param_entry["schema"]["default"] = default_val

        parameters_yaml.append(param_entry)

    # 3.6. Convert the constructed parameter list to a YAML string
    yaml_output = yaml.dump(
        parameters_yaml,
        Dumper=NoAliasDumper,
        sort_keys=False,
        default_flow_style=False,
        allow_unicode=True,
        indent=2,
        encoding="utf-8",
    )
    return yaml_output


# --------------------------------------------------------------------------
# 4. Run the conversion (for demonstration)
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # file_path = "docs/air_quality_api.md"  # or wherever your markdown is
    # final_yaml = convert_markdown_tables_to_yaml(file_path)
    # with open("yml/air_quality_api.yml", "wb") as f:
    #     f.write(final_yaml)
    #     f.close()
    yml = None
    with open("yml/air_quality_api.yml", "r", encoding="utf-8") as f:
        yml = yaml.dump(
            {
                "api-endpoint": "https://air-quality-api.open-meteo.com/v1/air-quality",
                "parameters": yaml.safe_load(f),
                "tags": ["air-quality"],
                "file": "air_quality_api.yml",
            },
            Dumper=NoAliasDumper,
            sort_keys=False,
            default_flow_style=False,
            allow_unicode=True,
            indent=2,
        )
        f.close()
    with open("yml/air_quality_api.yml", "w", encoding="utf-8") as f:
        f.write(yml)
        f.close()
