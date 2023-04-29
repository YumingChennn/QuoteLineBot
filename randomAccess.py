import pickle
import random


def randomGet():
    # positive
    with open('/Users/kenchen/PycharmProjects/Selenium/quoteCrawler/posQuo.pkl', 'rb') as f:
        pos = pickle.load(f)
    print(pos)
    # motivatioinal
    with open('/Users/kenchen/PycharmProjects/Selenium/quoteCrawler/motiQuo.pkl', 'rb') as f:
        moti = pickle.load(f)

    # inspirational
    with open('/Users/kenchen/PycharmProjects/Selenium/quoteCrawler/inspQuo.pkl', 'rb') as f:
        insp = pickle.load(f)

    # life
    with open('/Users/kenchen/PycharmProjects/Selenium/quoteCrawler/lifeQuo.pkl', 'rb') as f:
        life = pickle.load(f)

    # funny
    with open('/Users/kenchen/PycharmProjects/Selenium/quoteCrawler/funnyQuo.pkl', 'rb') as f:
        funny = pickle.load(f)
    allList=pos+moti+insp+life+funny
    return random.choice(allList)

#randomGet()
