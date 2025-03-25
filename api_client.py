import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def _build_url(self, endpoint):
        return f"{self.base_url}/{endpoint}"

    def search_jobs(self, endpoint, headers):
        url = self._build_url(endpoint)
        response = requests.get(url, headers=headers)
        return response

    def get_job_details(self, endpoint, jobID, headers):
        url = self._build_url(endpoint) + "?id=" + jobID
        response = requests.get(url, headers=headers)
        return response