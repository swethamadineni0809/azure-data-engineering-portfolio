import os
import json
import requests
from datetime import datetime
from azure.storage.filedatalake import DataLakeServiceClient
from dotenv import load_dotenv

load_dotenv()

# Config
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
STORAGE_ACCOUNT_NAME = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
STORAGE_ACCOUNT_KEY = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
CONTAINER_NAME = "raw"

def get_weather(city="Berlin"):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={OPENWEATHER_API_KEY}"
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def upload_to_adls(file_path, data):
    service_client = DataLakeServiceClient(
        account_url=f"https://{STORAGE_ACCOUNT_NAME}.dfs.core.windows.net",
        credential=STORAGE_ACCOUNT_KEY
    )
    file_system_client = service_client.get_file_system_client(CONTAINER_NAME)

    dirname = datetime.utcnow().strftime("%Y/%m/%d")
    filename = f"weather_{datetime.utcnow().strftime('%H%M%S')}.json"
    full_path = f"{dirname}/{filename}"

    file_client = file_system_client.create_file(full_path)
    file_client.append_data(data.encode(), 0)
    file_client.flush_data(len(data))

    print(f"Uploaded to ADLS: {full_path}")

def main():
    data = get_weather()
    upload_to_adls("weather.json", json.dumps(data))
    print("Done ")

if __name__ == "__main__":
    main()
