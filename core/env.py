import json

with open('./config.json') as f:
    CONFIG = json.load(f)

API_HOST = CONFIG["project"]["host"] 
API_PORT = CONFIG["project"]["port"] 
URL_PREFIX = CONFIG["project"]["url_prefix"] 
API_NAME = CONFIG["project"]["api_name"]  
API_VERSION = CONFIG["project"]["version"]  

 