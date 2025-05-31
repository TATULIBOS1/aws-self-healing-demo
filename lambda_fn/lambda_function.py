pipeline_client = None
runtime = None

def lambda_handler(event, context):
    response = runtime.invoke_endpoint()
    action = eval(response['Body'].read().decode())['action']
    if action == 'retry':
        pipeline_client.retry_stage_execution()
    return {"status": "done"}