import json
import urllib.request
import logging

# ロギングの設定
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        message = body.get('message', '')
        
        url = "https://8d7f-35-222-103-243.ngrok-free.app"
        
        headers = {"Content-Type": "application/json"}
        data = json.dumps({"message": message}).encode('utf-8')
        
        req = urllib.request.Request(
            url,
            data=data,
            headers=headers,
            method="POST"
        )
        
        with urllib.request.urlopen(req) as res:
            api_res = json.loads(res.read().decode('utf-8'))
        
        assistant_response = api_res.get("response", "")
        
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*" 
            },
            "body": json.dumps({
                "success": True,
                "response": assistant_response
            })
        }
    
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "success": False,
                "error": "Internal server error"
            })
        }