import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("AZURE_CONTAINER_RAW")
RAW_DATA_PATH = "raw_data"

def upload_files():
    # Connect to Azure
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    
    # Get all CSV files in raw_data folder
    csv_files = [f for f in os.listdir(RAW_DATA_PATH) if f.endswith('.csv')]
    
    print(f"Found {len(csv_files)} CSV files to upload...")
    
    for filename in csv_files:
        file_path = os.path.join(RAW_DATA_PATH, filename)
        
        print(f"Uploading {filename}...")
        
        with open(file_path, "rb") as data:
            container_client.upload_blob(
                name=filename,
                data=data,
                overwrite=True
            )
        
        print(f"✓ {filename} uploaded successfully")
    
    print(f"\nAll {len(csv_files)} files uploaded to Azure Blob Storage!")
    print(f"Container: {CONTAINER_NAME}")

if __name__ == "__main__":
    upload_files()