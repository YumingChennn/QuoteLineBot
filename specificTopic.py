import pickle

def posQuoGet():
    # 如果函數對象中沒有屬性 data，則從文件中讀取並加載名言列表
    if not hasattr(posQuoGet, "data"):
        with open('/Users/kenchen/PycharmProjects/Selenium/quoteCrawler/posQuo.pkl', 'rb') as f:
            posQuoGet.data = pickle.load(f)

    # 如果函數對象中沒有屬性 index，則將其初始化為 0
    if not hasattr(posQuoGet, "index"):
        posQuoGet.index = 0

    # 如果已經達到列表的末尾，則將索引重置為 0，以便重新開始
    if posQuoGet.index == len(posQuoGet.data):
        posQuoGet.index = 0

    # 從列表中返回當前索引對應的名言
    result = posQuoGet.data[posQuoGet.index]

    # 將索引值加 1，以便下次調用時返回下一個名言
    posQuoGet.index += 1

    # 返回名言
    return result

def motiQuoGet():
    # 如果函數對象中沒有屬性 data，則從文件中讀取並加載名言列表
    if not hasattr(motiQuoGet, "data"):
        with open('/Users/kenchen/PycharmProjects/Selenium/quoteCrawler/motiQuo.pkl', 'rb') as f:
            motiQuoGet.data = pickle.load(f)

    # 如果函數對象中沒有屬性 index，則將其初始化為 0
    if not hasattr(motiQuoGet, "index"):
        motiQuoGet.index = 0

    # 如果已經達到列表的末尾，則將索引重置為 0，以便重新開始
    if motiQuoGet.index == len(motiQuoGet.data):
        motiQuoGet.index = 0

    # 從列表中返回當前索引對應的名言
    result = motiQuoGet.data[motiQuoGet.index]

    # 將索引值加 1，以便下次調用時返回下一個名言
    motiQuoGet.index += 1

    # 返回名言
    return result

def inspQuoGet():
    # 如果函數對象中沒有屬性 data，則從文件中讀取並加載名言列表
    if not hasattr(inspQuoGet, "data"):
        with open('/Users/kenchen/PycharmProjects/Selenium/quoteCrawler/inspQuo.pkl', 'rb') as f:
            inspQuoGet.data = pickle.load(f)

    # 如果函數對象中沒有屬性 index，則將其初始化為 0
    if not hasattr(inspQuoGet, "index"):
        inspQuoGet.index = 0

    # 如果已經達到列表的末尾，則將索引重置為 0，以便重新開始
    if inspQuoGet.index == len(inspQuoGet.data):
        inspQuoGet.index = 0

    # 從列表中返回當前索引對應的名言
    result = inspQuoGet.data[inspQuoGet.index]

    # 將索引值加 1，以便下次調用時返回下一個名言
    inspQuoGet.index += 1

    # 返回名言
    return result

def lifeQuoGet():
    # 如果函數對象中沒有屬性 data，則從文件中讀取並加載名言列表
    if not hasattr(lifeQuoGet, "data"):
        with open('/Users/kenchen/PycharmProjects/Selenium/quoteCrawler/lifeQuo.pkl', 'rb') as f:
            lifeQuoGet.data = pickle.load(f)

    # 如果函數對象中沒有屬性 index，則將其初始化為 0
    if not hasattr(lifeQuoGet, "index"):
        lifeQuoGet.index = 0

    # 如果已經達到列表的末尾，則將索引重置為 0，以便重新開始
    if lifeQuoGet.index == len(lifeQuoGet.data):
        lifeQuoGet.index = 0

    # 從列表中返回當前索引對應的名言
    result = lifeQuoGet.data[lifeQuoGet.index]

    # 將索引值加 1，以便下次調用時返回下一個名言
    lifeQuoGet.index += 1

    # 返回名言
    return result

def funnyQuoGet():
    # 如果函數對象中沒有屬性 data，則從文件中讀取並加載名言列表
    if not hasattr(funnyQuoGet, "data"):
        with open('/Users/kenchen/PycharmProjects/Selenium/quoteCrawler/funnyQuo.pkl', 'rb') as f:
            funnyQuoGet.data = pickle.load(f)

    # 如果函數對象中沒有屬性 index，則將其初始化為 0
    if not hasattr(funnyQuoGet, "index"):
        funnyQuoGet.index = 0

    # 如果已經達到列表的末尾，則將索引重置為 0，以便重新開始
    if funnyQuoGet.index == len(funnyQuoGet.data):
        funnyQuoGet.index = 0

    # 從列表中返回當前索引對應的名言
    result = funnyQuoGet.data[funnyQuoGet.index]

    # 將索引值加 1，以便下次調用時返回下一個名言
    funnyQuoGet.index += 1

    # 返回名言
    return result
