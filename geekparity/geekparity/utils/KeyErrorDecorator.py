# 对出现keyError异常的直接跳过
def keyError(func):
    def inner():
        try:
            func()
        except KeyError :
            print("=======装饰器KeyError捕捉异常===========")
            pass
    return inner