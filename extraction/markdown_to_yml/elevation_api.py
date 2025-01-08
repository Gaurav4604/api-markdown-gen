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
# 2. Main function to parse the Parameter Table and generate YAML
# --------------------------------------------------------------------------
def convert_markdown_tables_to_yaml(file_path: str):
    """
    Reads a Markdown file containing only a 'Parameter' table:
      ['Parameter', 'Format', 'Required', 'Default', 'Description']
    and converts each row into a parameter definition in YAML format.

    Since there are NO array parameters here, we only handle scalar types:
      - number/float/double
      - string
      - date (yyyy-...)
    """
    # 2.1. Read and parse the Markdown file
    doc = MarkdownAnalyzer(file_path)
    tables = doc.identify_tables().get("Table", [])

    # 2.2. Identify the Parameter Table
    parameter_table = None
    for table in tables:
        header = [h.lower() for h in table.get("header", [])]
        if header == ["parameter", "format", "required", "default", "description"]:
            parameter_table = table
            break

    if parameter_table is None:
        raise ValueError(
            "Could not find a Parameter table with header: "
            "['Parameter', 'Format', 'Required', 'Default', 'Description']"
        )

    # 2.3. Build a list of parameter entries
    parameters_yaml = []

    for row in parameter_table["rows"]:
        # Each row is something like:
        #   [param_name, format_str, required_str, default_val, description]
        param_name = markdown_to_plain_text(row[0]).strip()
        format_str = markdown_to_plain_text(row[1]).strip()
        required_str = markdown_to_plain_text(row[2]).strip()

        # Handle missing columns gracefully
        default_val = ""
        description = ""
        if len(row) >= 5:
            default_val = markdown_to_plain_text(row[3]).strip()
            description = markdown_to_plain_text(row[4]).strip()
        elif len(row) == 4:
            description = markdown_to_plain_text(row[3]).strip()

        # Convert "Yes"/"No" to boolean
        required = required_str.lower() == "yes"

        # 2.4. Create the param entry (no arrays needed)
        param_entry = {
            "name": param_name,
            "in": "query",  # or "path", etc. as needed
            "required": required,
            "description": description,
            "schema": {},
        }

        # Handle the Format
        fmt_lower = format_str.lower()
        if fmt_lower in ("float", "double", "number"):
            param_entry["schema"]["type"] = "number"
            param_entry["schema"]["format"] = "float"  # or "double"
        elif fmt_lower in ("string", "text"):
            param_entry["schema"]["type"] = "string"
        elif fmt_lower.startswith("yyyy-"):
            # interpret as date/time
            param_entry["schema"]["type"] = "string"
            param_entry["schema"]["format"] = "date"  # or "date-time"
        else:
            # fallback
            param_entry["schema"]["type"] = "string"

        # If there's a default value, set it
        if default_val:
            param_entry["schema"]["default"] = default_val

        parameters_yaml.append(param_entry)

        # 2.5. Convert the list of parameters to a YAML string
        yaml_output = yaml.dump(
            parameters_yaml,
            sort_keys=False,
            default_flow_style=False,
            allow_unicode=True,
            indent=2,
            encoding="utf-8",
        )
        return yaml_output


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


# --------------------------------------------------------------------------
# 3. Putting it all together: run the conversion
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # Example: specify your Markdown file here
    # file_path = "docs/elevation_api.md"
    # final_yaml = convert_markdown_tables_to_yaml(file_path)
    # with open("yml/elevation_api.yml", "wb") as f:
    #     f.write(final_yaml)
    #     f.close()
    yml = None
    with open("yml/elevation_api.yml", "r", encoding="utf-8") as f:
        yml = yaml.dump(
            {
                "api-endpoint": "https://api.open-meteo.com/v1/elevation",
                "parameters": yaml.safe_load(f),
                "tags": ["elevation-data"],
                "file": "elevation_api.yml",
            },
            Dumper=NoAliasDumper,
            sort_keys=False,
            default_flow_style=False,
            allow_unicode=True,
            indent=2,
        )
        f.close()
    with open("yml/elevation_api.yml", "w", encoding="utf-8") as f:
        f.write(yml)
        f.close()
