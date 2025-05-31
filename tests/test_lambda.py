import lambda_fn.lambda_function as lf

def test_lambda_retry(monkeypatch):
    class MockPipeline:
        def retry_stage_execution(self, **kwargs):
            print("Retry called")

    class MockSageMaker:
        def invoke_endpoint(self, **kwargs):
            return {'Body': type('obj', (object,), {'read': lambda self: b'{"action": "retry"}'})()}

    monkeypatch.setattr(lf, 'pipeline_client', MockPipeline())
    monkeypatch.setattr(lf, 'runtime', MockSageMaker())

    event = {'detail': {'pipeline': 'SelfHealingPipeline', 'execution-id': '1'}}
    lf.lambda_handler(event, None)