import boto3
import json

try:
    prompt_data = "Write a short poem about nature."

    bedrock = boto3.client(service_name="bedrock-runtime")

    payload = {
        "prompt": "[INST]" + prompt_data + "[/INST]",
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }

    body = json.dumps(payload)
    model_id = "meta.llama3-70b-instruct-v1:0"

    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )

    response_body = json.loads(response.get("body").read())
    response_text = response_body['generation']
    print("Response received:", response_text)

except Exception as e:
    print("An error occurred:", e)
