# lru_cache
import time
from functools import lru_cache

# @lru_cache(maxsize=32)
# if we run this program it will take 3-3 seconds break because we use time.sleep
'''def some_work(n):
    # Some task taking n seconds
    time.sleep(n)
    return n

if __name__=='__main__':
    print("Now running some work")
    some_work(3)
    print("Done... again running some work")
    some_work(3)
    print("Final Done")'''

# above problem solution.. we use lru_cache it will store our last nth(3) calling
# records nth(32) last records with the defined maxsize

'''@lru_cache(maxsize=3)
def some_work(n):
    # Some task taking n seconds
    time.sleep(n)
    return n

if __name__=='__main__':
    print("Now running some work")
    some_work(3)
    print("Done... again running some work")
    some_work(3)
    print("Final Done")'''

# same as above but with the input from keyboard
lru_input = int(input("Enter your maxsize of lrucache : "))
@lru_cache(maxsize=lru_input)
def some_work(n):
    # Some task taking n seconds
    time.sleep(n)
    return n

if __name__=='__main__':
    print("Now running some work")
    sw_input = int(input("Enter n for passing : "))
    some_work(sw_input)
    print("Done... again running some work")
    some_work(sw_input)
    print("Final Done")