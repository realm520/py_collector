# encoding=utf-8

import json
import requests

def http_request(method, args):
    url = "http://127.0.0.1:8091"
    args_j = json.dumps(args)
    payload =  "{\r\n \"id\": 1,\r\n \"method\": \"%s\",\r\n \"params\": %s\r\n}" % (method, args_j)
    headers = {
            'content-type': "text/plain",
            'cache-control': "no-cache",
    }
    try:
        response = requests.request("POST", url, data=payload, headers=headers)
        #print type(response)
        #print response.text
        rep = response.json()
        if "result" in rep:
            return rep["result"]
    except:
        return None

