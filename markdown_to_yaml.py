from mrkdwn_analysis import MarkdownAnalyzer
import markdown
from bs4 import BeautifulSoup


def markdown_to_plain_text(md_content):
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)
    # Parse HTML and extract plain text
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text()


doc = MarkdownAnalyzer("docs/climate_api.md")

tables = doc.identify_tables().get("Table")

for table in tables:
    print(table["header"])

parameter_list = tables[0]

for row in parameter_list["rows"]:
    # row[0] <- param name
    # row[1] <- format
    # row[2] <- required (Yes/No)
    # row[3] <- default value set for parameter (can be empty string)
    # row[4] <- description of parameter

    """
    if param is of type string array,
    it needs to be defined as type array
    the order of definition of string array is
    1. hourly: tables[1] contains parameter hourly's enum values
    2. skip this one <-

    """
    print(markdown_to_plain_text(row[0]))


"""
['Parameter', 'Format', 'Required', 'Default', 'Description'] <- this is the table containing parameters
['Variable', 'Valid time', 'Unit', 'Description'] <- for the parameter hourly, this is the table of available enum options
['Variable', 'Valid time', 'Unit', 'HRRR', 'ICON-D2', 'AROME'] <- skip this one
['Level (hPa)', '1000', '975', '950', '925', '900', '850', '800', '700', '600', '500', '400', '300', '250', '200', '150', '100', '70', '50', '30'] <- skip this one
['Variable', 'Unit', 'Description'] <- skip this one
['Variable', 'Unit', 'Description'] <- for parameter daily 
['Parameter', 'Format', 'Description'] <- this contains all response values
['Code', 'Description'] <- skip this one

"""
