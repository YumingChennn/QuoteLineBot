import requests
import json
html = requests.get("https://gnehs.github.io/ntut-course-crawler-node/calendar.json")
html.encoding="UTF-8"

print(html.text)


data = json.loads(html.text)
'''
for dict in data:
    listvalues= list(dict.values())
    print(listvalues)
'''


