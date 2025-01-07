from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from datetime import datetime


def fix_start_date_incompletion(query: str) -> str:
    parsed_url = urlparse(query)

    query_params = parse_qs(parsed_url.query)

    # Check if start_date exists in query_params but end_date doesn't
    if "start_date" in query_params and "end_date" not in query_params:
        # Add end_date parameter with the same value as start_date
        query_params["end_date"] = [query_params["start_date"][0]]

        # Reconstruct URL with new params
        url_with_end_date = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{'&'.join(f'{key}={value[0]}' for key, value in query_params.items())}"

        query = url_with_end_date

    return query


def fix_date_time_value(request_url: str) -> str:
    # Parse the URL into its components
    parsed_url = urlparse(request_url)

    # Parse the query parameters into a dictionary
    query_params = parse_qs(parsed_url.query)

    # Define the date parameters to check
    date_keys = ["start_date", "end_date"]

    # Iterate over the date parameters
    for key in date_keys:
        if key in query_params and query_params[key]:
            # Extract the first value for the parameter
            date_value = query_params[key][0]
            try:
                # Parse the datetime string to a datetime object
                date_obj = datetime.fromisoformat(date_value)
                # Format the datetime object to a date string 'YYYY-MM-DD'
                date_str = date_obj.date().isoformat()
                # Update the query parameter with the formatted date string
                query_params[key] = [date_str]
            except ValueError:
                print(f"Invalid date format for '{date_value}' in parameter '{key}'")

    # Encode the updated query parameters back into a query string
    updated_query = urlencode(query_params, doseq=True)

    # Construct the updated URL with the modified query string
    updated_url = urlunparse(parsed_url._replace(query=updated_query))

    return updated_url


def fix_forecast_day_inconsistency(request_url: str) -> str:
    # Parse the URL into components
    parsed_url = urlparse(request_url)

    # Parse the query parameters into a dictionary
    query_params = parse_qs(parsed_url.query)

    # Check if 'forecast_days' is in the query parameters
    if "forecast_days" in query_params:
        # Remove 'start_date' and 'end_date' if they exist
        query_params.pop("start_date", None)
        query_params.pop("end_date", None)

    # Encode the updated query parameters back into a query string
    new_query = urlencode(query_params, doseq=True)

    # Construct the updated URL with the modified query string
    updated_url = urlunparse(parsed_url._replace(query=new_query))

    return updated_url


# import ollama
# import yaml

# call = "https://marine-api.open-meteo.com/v1/marine?latitude=-34.93&longitude=138.6&timezone=Australia%2FSydney&daily=wave_height_max,swell_wave_height_max,ocean_current_velocity,ocean_current_direction&forecast_days=1"

# error = """
# {"error":true,"reason":"Data corrupted at path ''. Cannot initialize IconWaveVariableDaily from invalid String value wave_height_max,swell_wave_height_max,ocean_current_velocity,ocean_current_direction."}
# """

# doc = yaml.safe_load(open("yml/marine_weather_api.yml", "r", encoding="utf-8"))

# res = ollama.chat(
#     model="codegemma",
#     messages=[
#         {
#             "role": "user",
#             "content": """
# Fix the API call {}
# that fails with error {},
# With Reference Doc:
# {}
# """.format(
#                 call, error, doc
#             ),
#         }
#     ],
#     options={"temperature": 0.1, "num_ctx": 16384},
# )


# print(res["message"]["content"])
