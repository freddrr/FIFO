import json

from api_client import ApiClient

api_client = ApiClient("https://linkedin-data-api.p.rapidapi.com")
response = api_client.search_jobs("search-jobs?keywords=software%20engineer&locationId=104472865&datePosted=past24Hours&sort=mostRecent", {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': '959ffaad04msh195f863bae0c884p151c0bjsn64bc8e40f8b1'})
data = response.json()

for x in range(len(data["data"])):
    print(data["data"][x]["id"])