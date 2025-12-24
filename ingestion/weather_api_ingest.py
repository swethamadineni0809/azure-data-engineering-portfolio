import os
import json
import requests
from datetime import datetime
from azure.storage.filedatalake import DataLakeServiceClient
from dotenv import load_dotenv

# -------------------------------------------------
# Load environment variables
# -------------------------------------------------
load_dotenv()

# -------------------------------------------------
# Configuration (NO hardcoding)
# -------------------------------------------------
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
OPENWEATHER_BASE_URL = os.getenv("OPENWEATHER_BASE_URL")
OPENWEATHER_WEATHER_ENDPOINT = os.getenv("OPENWEATHER_WEATHER_ENDPOINT")

WEATHER_CITIES = [
    city.strip()
    for city in os.getenv("WEATHER_CITIES", "").split(",")
    if city.strip()
]

AZURE_STORAGE_ACCOUNT_NAME = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
AZURE_STORAGE_ACCOUNT_KEY = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
AZURE_RAW_CONTAINER = os.getenv("AZURE_RAW_CONTAINER")


def validate_config():
    missing = []

    if not OPENWEATHER_API_KEY:
        missing.append("OPENWEATHER_API_KEY")
    if not OPENWEATHER_BASE_URL:
        missing.append("OPENWEATHER_BASE_URL")
    if not OPENWEATHER_WEATHER_ENDPOINT:
        missing.append("OPENWEATHER_WEATHER_ENDPOINT")
    if not WEATHER_CITIES:
        missing.append("WEATHER_CITIES")
    if not AZURE_STORAGE_ACCOUNT_NAME:
        missing.append("AZURE_STORAGE_ACCOUNT_NAME")
    if not AZURE_STORAGE_ACCOUNT_KEY:
        missing.append("AZURE_STORAGE_ACCOUNT_KEY")
    if not AZURE_RAW_CONTAINER:
        missing.append("AZURE_RAW_CONTAINER")

    if missing:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing)}"
        )


# -------------------------------------------------
# Weather API call
# -------------------------------------------------
def get_weather(city: str) -> dict:
    url = f"{OPENWEATHER_BASE_URL}{OPENWEATHER_WEATHER_ENDPOINT}"

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


# -------------------------------------------------
# Upload JSON to ADLS Gen2
# -------------------------------------------------
def upload_to_adls(data: dict) -> None:
    service_client = DataLakeServiceClient(
        account_url=f"https://{AZURE_STORAGE_ACCOUNT_NAME}.dfs.core.windows.net",
        credential=AZURE_STORAGE_ACCOUNT_KEY,
    )

    file_system_client = service_client.get_file_system_client(
        AZURE_RAW_CONTAINER
    )

    # Partitioned path (best practice)
    date_path = datetime.utcnow().strftime("%Y/%m/%d")
    city = data.get("name", "unknown").lower()
    timestamp = datetime.utcnow().strftime("%H%M%S")

    filename = f"weather_{city}_{timestamp}.json"
    full_path = f"{date_path}/{filename}"

    file_client = file_system_client.create_file(full_path)

    json_data = json.dumps(data)
    file_client.append_data(
        json_data,
        offset=0,
        length=len(json_data)
    )
    file_client.flush_data(len(json_data))

    print(f"Uploaded file: {full_path}")


# -------------------------------------------------
# Main execution
# -------------------------------------------------
def main():
    validate_config()

    for city in WEATHER_CITIES:
        weather_data = get_weather(city)
        upload_to_adls(weather_data)

    print("Weather ingestion completed successfully")


if __name__ == "__main__":
    main()
