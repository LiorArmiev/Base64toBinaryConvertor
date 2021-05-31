import logging
import base64
import json

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP Base64/Binary convertion function')
    
    req_body = req.get_json()
    action = req_body.get('convertto')
    input = req_body.get('input')

    if action == 'base64':
        base64_data = input
        base64_encoded_data = base64.b64encode(base64_data)
        base64_message = base64_encoded_data.decode('utf-8')
        outreturn = {"base64":f"{base64_message}","Binary":f"{input}"}
        return func.HttpResponse(       
        json.dumps(outreturn),
        mimetype="application/json"
        )
    elif action == "binary":
        base64_data = input
        base64_bytes = base64_data.encode('utf-8')
        binery_data_output = base64.decodebytes(base64_bytes)
        outreturn = {"base64":f"{input}","Binary":f"{binery_data_output}"}
        return func.HttpResponse(       
        json.dumps(outreturn),
        mimetype="application/json"
        )
    else:
        return func.HttpResponse("Sorry but the API is missing parameters")
