import multyvac
import os
import time

multyvac.config.api_key = os.environ["MULTYVAC_API_KEY"]
multyvac.config.api_secret_key = os.environ["MULTYVAC_API_SECRET_KEY"]
multyvac.config.api_url = os.environ["MULTYVAC_API_URL"]

import requests

def status(url):
    return requests.get(url).status_code

def server_header(url):
    return requests.get(url).headers.get('server')


jid = multyvac.submit(lambda: "foo")
job = multyvac.get(jid)
print job
print job.get_result()
