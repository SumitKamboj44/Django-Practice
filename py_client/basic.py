import requests

endpoint="https://calendar.google.com/calendar/u/0/r/week"
endpoint="https://httpbin.org/anything"
get_response=requests.get(endpoint,json={"query":"hello world"})
print(get_response.json())