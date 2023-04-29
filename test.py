import pickle

add='/Users/kenchen/PycharmProjects/Selenium/quoteCrawler/motiQuo.pkl'

with open(add,'rb') as f:
    data = pickle.load(f)

print(data)