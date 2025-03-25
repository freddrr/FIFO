import json
import requests
from bs4 import BeautifulSoup

from api_client import ApiClient
from chat_gpt_client import ChatGptClient
from email_client import EmailClient

#emailClient = EmailClient()
#emailClient.send_email("Hi Trae 2", "What up")

api_client = ApiClient("https://linkedin-data-api.p.rapidapi.com")
response = api_client.search_jobs("search-jobs?keywords=software%20engineer&locationId=104472865&datePosted=past24Hours&sort=mostRecent", {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': '959ffaad04msh195f863bae0c884p151c0bjsn64bc8e40f8b1'})
data = response.json()

testUrl = data["data"][0]["url"]

print(testUrl)

testId = data["data"][0]["id"]

details = api_client.get_job_details("get-job-details", testId, {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': '959ffaad04msh195f863bae0c884p151c0bjsn64bc8e40f8b1'}).json()

description = details["data"]["description"]

ChatGptClient().make_call(description)