# using instance method
# Eager Initialization
class Singleton:
    __instance = None
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
    def print_hello(self):
        print("Hello Eager Initialization")
s = Singleton()       # object s we can use in whole code. we can't create again
print(s)
s.print_hello()
# s1 = Singleton() 
# print(s1)



# =============================
# Lazy Initialization
class Singleton1:
    __instance = None
    def __init__(self):
         pass
    @staticmethod 
    def getInstance():
        if Singleton1.__instance == None:
            Singleton1.__instance = Singleton1()
        return Singleton1.__instance
    def print_hello(self):
        print("Hello Lazy Initialization")

s1 = Singleton1.getInstance()
print(s1)
s2 = Singleton1.getInstance()
print(s2)
s3 = Singleton1.getInstance()
print(s3)


# =======================================
# Synchronized Lazy Initialization
import threading

class LockingSingleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
        return cls._instance
    def print_hello(self):
        print("Hello Locking Singleton")
    
ls = LockingSingleton.get_instance()
print(ls)
ls1 = LockingSingleton.get_instance()
print(ls1)
ls.print_hello()


# ==================================

# Double checked locking
import threading

class DoubleCheckedLockingSingleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance


# ==========================================
class StaticHolderSingleton:
    class SingletonHelper:
        INSTANCE = None
        def __init__(cls):
            cls.INSTANCE = StaticHolderSingleton()

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if not StaticHolderSingleton.SingletonHelper.INSTANCE:
            StaticHolderSingleton.SingletonHelper.INSTANCE = StaticHolderSingleton()
        return StaticHolderSingleton.SingletonHelper.INSTANCE
    
sh = StaticHolderSingleton.get_instance()
print(sh)
sh1 = StaticHolderSingleton.get_instance()
print(sh1)

