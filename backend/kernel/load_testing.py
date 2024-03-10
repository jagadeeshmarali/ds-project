from locust import task, FastHttpUser, HttpUser
import json


class MyUser(HttpUser):
    headers = {"x-api-key": "3ea06cb8-5fb5-4762-a647-70811eb3394f"}

    @task
    def async_inference(self):

        f = open("/mnt/locust/data/payload.json", "r")
        payload = json.loads(f.read())
        f.close()
        self.client.post(
            "/api/v1/inference/async?batch_size=25&max_concurrency=2&executor=standard",
            json=payload,
            headers=self.headers,
        )