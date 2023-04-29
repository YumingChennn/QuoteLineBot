import pickle

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

