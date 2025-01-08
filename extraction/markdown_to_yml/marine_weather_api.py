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
# 2. Function to generate the "hourly" param YAML
# --------------------------------------------------------------------------
def hourly_param_generator(
    param_name, required, description, enum_items=None, default_val=None
):
    """
    Generates a parameter entry specifically for the 'hourly' param,
    which is of type 'string array' with enumerations as objects.

    'enum_items' should be a list of dicts like:
       [
         { "value": "temperature_2m", "unit": "°C", "description": "..." },
         { "value": "dew_point_2m",   "unit": "°C", "description": "..." },
         ...
       ]
    """
    param_entry = {
        "name": param_name,
        "in": "query",
        "required": required,
        "description": description or "",
        "explode": False,  # Typically for array query params
        "schema": {"type": "array", "items": {"type": "string"}},
    }
    if enum_items:
        # Attach the list of dict objects to enum
        param_entry["schema"]["items"]["enum"] = enum_items

    # Set default if provided
    if default_val:
        param_entry["schema"]["default"] = default_val

    return param_entry


def daily_param_generator(
    param_name, required, description, enum_items=None, default_val=None
):
    """
    Generates a parameter entry for 'daily' param, of type 'string array',
    with enumerations as objects: { "value": ..., "unit": ..., "description": ... }.
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
            "default": default_val if default_val else None,
        },
    }


# --------------------------------------------------------------------------
# 3. The main function to convert a recognized "Parameter" table to YAML
# --------------------------------------------------------------------------
def convert_markdown_tables_to_yaml(file_path: str):
    # Create doc from our MarkdownAnalyzer
    doc = MarkdownAnalyzer(file_path)

    # Extract all tables from the doc
    tables = doc.identify_tables().get("Table", [])

    # Identify relevant tables:
    # - parameter_table => header: ["Parameter", "Format", "Required", "Default", "Description"]
    # - hourly_enum_table => header: ["Variable", "Valid time", "Unit", "Description"]
    # - current_enum_table => header: ["Variable", "Valid time", "Unit", "HRRR", "ICON-D2", "AROME"]
    # - daily_enum_table => header: ["Variable", "Unit", "Description"]
    parameter_table = None
    hourly_enum_table = None
    current_enum_table = None
    daily_enum_table = None

    for table in tables:
        header = [h.lower() for h in table.get("header", [])]
        # Identify the "Parameter" table
        if header == ["parameter", "format", "required", "default", "description"]:
            parameter_table = table

        # For 'hourly'
        if header[:4] == ["variable", "valid time", "unit", "description"]:
            hourly_enum_table = table

        # For 'current'
        if header == ["variable", "valid time", "unit", "hrrr", "icon-d2", "arome"]:
            current_enum_table = table

        # For 'daily'
        if header == ["variable", "unit", "description"]:
            daily_enum_table = table

    if parameter_table is None:
        raise ValueError("Could not find the Parameter table with the expected header.")

    # -------------------------------------------
    # Parse the 'hourly' table for enum items
    # -------------------------------------------
    hourly_enum_items = []
    if hourly_enum_table:
        for row in hourly_enum_table.get("rows", []):
            # row example: ["temperature_2m", "hourly", "°C", "Air temperature at 2 m"]
            if len(row) >= 4:
                variable = markdown_to_plain_text(row[0]).strip()
                unit = markdown_to_plain_text(row[2]).strip()
                desc = markdown_to_plain_text(row[3]).strip()
                if variable:
                    hourly_enum_items.append(
                        {"value": variable, "unit": unit, "description": desc}
                    )

    # -------------------------------------------
    # Parse the 'current' table for enum items
    # -------------------------------------------
    current_enum_items = []
    if current_enum_table:
        for row in current_enum_table.get("rows", []):
            # row example: ["temperature_2m", "hourly", "°C", "...", "...", "..."]
            if len(row) >= 3:
                variable = markdown_to_plain_text(row[0]).strip()
                unit = markdown_to_plain_text(row[2]).strip()
                if variable:
                    current_enum_items.append(
                        {
                            "value": variable,
                            "unit": unit,
                            # ignoring row[3], row[4], row[5]
                        }
                    )

    # -------------------------------------------
    # Parse the 'daily' table for enum items
    # -------------------------------------------
    daily_enum_items = []
    if daily_enum_table:
        for row in daily_enum_table.get("rows", []):
            # row example: ["precipitation_sum", "mm", "Total precipitation in mm"]
            if len(row) >= 3:
                variable = markdown_to_plain_text(row[0]).strip()
                unit = markdown_to_plain_text(row[1]).strip()
                desc = markdown_to_plain_text(row[2]).strip()
                if variable:
                    daily_enum_items.append(
                        {"value": variable, "unit": unit, "description": desc}
                    )

    # Build a list of parameter entries to be turned into YAML
    parameters_yaml = []

    # 4. Iterate over each row in the parameter table and convert to YAML structure
    for row in parameter_table["rows"]:
        param_name = markdown_to_plain_text(row[0]).strip()
        format_str = markdown_to_plain_text(row[1]).strip()
        required_str = markdown_to_plain_text(row[2]).strip()

        default_val = ""
        description = ""
        if len(row) >= 5:
            default_val = markdown_to_plain_text(row[3]).strip()
            description = markdown_to_plain_text(row[4]).strip()
        elif len(row) == 4:
            description = markdown_to_plain_text(row[3]).strip()

        # Convert "Yes"/"No" to boolean
        required = True if required_str.lower() == "yes" else False

        # Decide how to build this param's schema
        # Check for the special array-based params: "hourly", "current", "daily"
        if format_str.lower() == "string array":
            if param_name.lower() == "hourly":
                param_entry = hourly_param_generator(
                    param_name=param_name,
                    required=required,
                    description=description,
                    enum_items=hourly_enum_items,
                    default_val=default_val,
                )
            elif param_name.lower() == "current":
                param_entry = hourly_param_generator(
                    param_name=param_name,
                    required=required,
                    description=description,
                    enum_items=hourly_enum_items,
                    default_val=default_val,
                )
            elif param_name.lower() == "daily":
                param_entry = daily_param_generator(
                    param_name=param_name,
                    required=required,
                    description=description,
                    enum_items=daily_enum_items,
                    default_val=default_val,
                )
            else:
                # Generic array param
                param_entry = {
                    "name": param_name,
                    "in": "query",
                    "required": required,
                    "description": description or "",
                    "explode": False,
                    "schema": {"type": "array", "items": {"type": "string"}},
                }
                # If there's a default, set it
                if default_val:
                    param_entry["schema"]["default"] = default_val

        else:
            # Fallback for non-array params
            param_entry = {
                "name": param_name,
                "in": "query",
                "required": required,
                "description": description or "",
                "schema": {},
            }

            # Handle special data types or default values
            if format_str.lower() in ("float", "double", "number"):
                param_entry["schema"]["type"] = "number"
                param_entry["schema"]["format"] = "float"  # or "double"
            elif format_str.lower() in ("string", "text"):
                param_entry["schema"]["type"] = "string"
            elif format_str.lower().startswith("yyyy-"):
                # interpret as date/time
                param_entry["schema"]["type"] = "string"
                param_entry["schema"]["format"] = "date"  # or "date-time"
            else:
                # fallback
                param_entry["schema"]["type"] = "string"

            if default_val:
                param_entry["schema"]["default"] = default_val

        # Add final param entry to the list
        parameters_yaml.append(param_entry)

    # Convert the constructed parameter list to a YAML string
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
# 4. Putting it all together: run the conversion
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # file_path = "docs/marine_weather_api.md"
    # final_yaml = convert_markdown_tables_to_yaml(file_path)
    yml = None
    with open("yml/marine_weather_api.yml", "r", encoding="utf-8") as f:
        yml = yaml.dump(
            {
                "api-endpoint": "https://marine-api.open-meteo.com/v1/marine",
                "parameters": yaml.safe_load(f),
                "tags": ["marine-conditions"],
                "file": "marine_weather_api.yml",
            },
            Dumper=NoAliasDumper,
            sort_keys=False,
            default_flow_style=False,
            allow_unicode=True,
            indent=2,
        )
        f.close()
    with open("yml/marine_weather_api.yml", "w", encoding="utf-8") as f:
        f.write(yml)
        f.close()
