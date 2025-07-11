import logging
import os

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

#from dotenv import load_dotenv
#load_dotenv()

key_vault_uri = os.getenv("KEYVAULT_URI")

#azure auth
credential = DefaultAzureCredential()

#create cient keyvat
client = SecretClient(vault_url=key_vault_uri, credential=credential)

def get_secret(secret_name: str) -> str:
    try:
        return client.get_secret(name=secret_name).value
    except Exception as error:
        logging.error(f"ERROR GET SECRET {error}")