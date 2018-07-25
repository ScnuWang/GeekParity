from functools import wraps

# 由于这里被装饰的函数是带参数的，并且包含self,所以这里直接使用无参,之前的无参除出现问题
# 对出现keyError异常的直接跳过
def parseExceptWrapper(func):
    @wraps(func)
    def wrapper(*args, **kwds):
        try:
            return func(*args, **kwds)
        except KeyError :
            print("=======装饰器KeyError捕捉异常，作跳过处理===========")
            pass
        except UnicodeEncodeError:
            print("=======装饰器UnicodeEncodeError捕捉异常，作跳过处理===========")
            pass
        except Exception as error:
            print(error)
    return wrapper