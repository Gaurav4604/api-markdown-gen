import yaml
import markdown
from bs4 import BeautifulSoup
from mrkdwn_analysis import MarkdownAnalyzer


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
# 2. Generator function specifically for the 'daily' parameter
# --------------------------------------------------------------------------
def daily_param_generator(
    param_name, required, description, enum_items=None, default_val=None
):
    """
    Generates a parameter entry for 'daily', which is a 'string array'
    with enumerations as objects:
      { "value": ..., "unit": ..., "description": ... }.
    """
    param_entry = {
        "name": param_name,
        "in": "query",
        "required": required,
        "description": description or "",
        "explode": False,
        "schema": {"type": "array", "items": {"type": "string"}},
    }
    # Attach the enumerations (if any) as an array of objects
    if enum_items:
        param_entry["schema"]["items"]["enum"] = enum_items

    if default_val:
        param_entry["schema"]["default"] = default_val

    return param_entry


# --------------------------------------------------------------------------
# 3. Main function to parse tables and generate YAML
# --------------------------------------------------------------------------
def convert_markdown_tables_to_yaml(file_path: str):
    # 3.1. Read and parse the Markdown file
    doc = MarkdownAnalyzer(file_path)
    tables = doc.identify_tables().get("Table", [])

    # 3.2. Identify the relevant tables:
    parameter_table = None
    daily_enum_table = None

    for table in tables:
        header = [h.lower() for h in table.get("header", [])]

        # The Parameter Table
        if header == ["parameter", "format", "required", "default", "description"]:
            parameter_table = table

        # The Daily Table
        if header == ["variable", "unit", "description"]:
            daily_enum_table = table

    if parameter_table is None:
        raise ValueError(
            "Could not find Parameter table with header: "
            "['Parameter', 'Format', 'Required', 'Default', 'Description']"
        )

    if daily_enum_table is None:
        raise ValueError(
            "Could not find Daily table with header: "
            "['Variable', 'Unit', 'Description']"
        )

    # 3.3. Parse the 'daily' table to build enum items for daily
    daily_enum_items = []
    for row in daily_enum_table["rows"]:
        # row = ["precipitation_sum", "mm", "Total precipitation"]
        if len(row) >= 3:
            variable = markdown_to_plain_text(row[0]).strip()  # "precipitation_sum"
            unit = markdown_to_plain_text(row[1]).strip()  # "mm"
            desc = markdown_to_plain_text(row[2]).strip()  # "Total precipitation"
            if variable:
                daily_enum_items.append(
                    {"value": variable, "unit": unit, "description": desc}
                )

    # 3.4. Build a list of parameter entries from the Parameter Table
    parameters_yaml = []

    for row in parameter_table["rows"]:
        param_name = markdown_to_plain_text(row[0]).strip()
        format_str = markdown_to_plain_text(row[1]).strip()
        required_str = markdown_to_plain_text(row[2]).strip()

        # Possibly missing columns
        default_val = ""
        description = ""
        if len(row) >= 5:
            default_val = markdown_to_plain_text(row[3]).strip()
            description = markdown_to_plain_text(row[4]).strip()
        elif len(row) == 4:
            description = markdown_to_plain_text(row[3]).strip()

        required = required_str.lower() == "yes"

        # 3.5. For daily param with "string array", attach daily_enum_items
        if format_str.lower() == "string array" and param_name.lower() == "daily":
            param_entry = daily_param_generator(
                param_name=param_name,
                required=required,
                description=description,
                enum_items=daily_enum_items,
                default_val=default_val,
            )
        # 3.6. Generic array fallback
        elif format_str.lower() == "string array":
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
            # 3.7. Fallback for non-array parameters
            param_entry = {
                "name": param_name,
                "in": "query",
                "required": required,
                "description": description,
                "schema": {},
            }

            fmt_lower = format_str.lower()
            if fmt_lower in ("float", "double", "number"):
                param_entry["schema"]["type"] = "number"
                param_entry["schema"]["format"] = "float"
            elif fmt_lower in ("string", "text"):
                param_entry["schema"]["type"] = "string"
            elif fmt_lower.startswith("yyyy-"):
                param_entry["schema"]["type"] = "string"
                param_entry["schema"]["format"] = "date"
            else:
                param_entry["schema"]["type"] = "string"

            if default_val:
                param_entry["schema"]["default"] = default_val

        parameters_yaml.append(param_entry)

    # 3.8. Convert final param list to a YAML string
    yaml_output = yaml.dump(
        parameters_yaml,
        sort_keys=False,
        default_flow_style=False,
        allow_unicode=True,
        indent=2,
        encoding="utf-8",
    )
    return yaml_output


# --------------------------------------------------------------------------
# 4. Putting it all together: run the conversion
# --------------------------------------------------------------------------
if __name__ == "__main__":
    file_path = "docs/climate_api.md"  # or wherever your markdown is
    final_yaml = convert_markdown_tables_to_yaml(file_path)
    with open("yml/climate_api.yml", "wb") as f:
        f.write(final_yaml)
        f.close()
