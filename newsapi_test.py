import requests

url = ('https://newsapi.org/v2/everything?'
       'q=OpenAI&'
       'from=2024-12-03&'
       'sortBy=popularity&'
       'apiKey=e83103d896a94189b0ea213e541d91cc')

response = requests.get(url)

print(response.json())
