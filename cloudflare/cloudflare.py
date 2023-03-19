import requests


class Cloudflare:
    API_URL = "https://api.cloudflare.com/client/v4"

    def __init__(self):
        self.headers = {
            "Content - Type": "application / json"
        }

        self.last_request = None

    def authenticate(self, auth):
        self.headers["X-Auth-Email"] = auth.user
        self.headers["X-Auth-Key"] = auth.key

        return self

    def query(self, endpoint):
        response = requests.get(
            url=f"{self.API_URL}/{endpoint.get_list_name()}",
            headers=self.headers,
            params=endpoint.get_params()
        )
        self.last_request = response.request
        return response.json()

    def update(self, endpoint):
        response = requests.put(
            url=f"{self.API_URL}/{endpoint.get_update_name(endpoint.update.identifier)}",
            data=endpoint.update.get_body(),
            headers=self.headers,
            params=endpoint.get_params()
        )
        self.last_request = response.request
        return response.json()

