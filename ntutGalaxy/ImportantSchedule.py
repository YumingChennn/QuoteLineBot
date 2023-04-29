import requests
import json

html = requests.get("https://gnehs.github.io/ntut-course-crawler-node/calendar.json")
html.encoding = "UTF-8"
data = json.loads(html.text)

schedule = data

del schedule[:287]
#print(schedule)

for d in schedule:
    del d['type']
    del d['params']
    del d['datetype']
    del d['dtstamp']
    del d['uid']
    del d['created']
    del d['lastmodified']
    del d['sequence']
    del d['status']
    del d['transparency']
    del d['method']


print(schedule)

with open('importantSchedule.json', 'w') as file:
    json.dump(schedule, file)
