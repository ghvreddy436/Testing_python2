import requests
import shutil
import datetime
import azure.functions as func
import tempfile
from os import listdir
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import time, os, fnmatch, shutil
from azure.identity import ClientSecretCredential 
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import *
from datetime import datetime, timedelta
import sys

def main(mytimer: func.TimerRequest, outputblob: func.Out[bytes]):
    url = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_Asia_24h.csv"
    r = requests.get(url, verify=False,stream=True)
    if r.status_code!=200:
        print ("Failure!!")
        exit()
    else:
        r.raw.decode_content = True
        t = time.localtime()
        timestamp = time.strftime('%b-%d-%Y_%H%M', t)
        CONNECTION_STRING = os.environ['AZURE_STORAGE_CONNECTION_STRING']
        with open('/tmp/'+"MODIS_C6_1_South_Asia_24h.csv"+ timestamp, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        blob = BlobClient.from_connection_string(CONNECTION_STRING, container_name="poc1dataloaddb1", blob_name="MODIS_C6_1_South_Asia_24h.csv")
        with open('/tmp/'+"MODIS_C6_1_South_Asia_24h.csv"+ timestamp, "rb") as data:
            blob.upload_blob(data,overwrite=True)
            print ("Success")

if __name__ == '__main__':
    main()