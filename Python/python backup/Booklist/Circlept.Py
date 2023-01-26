import time
from functools import lru_cache
@lru_cache(maxsize=2)
def trycha1(n):
    time.sleep(n)
    return 2+3

print(trycha1(1))
print("This Is A")
print(trycha1(2))
print("This Is B")
print(trycha1(3))
print("This Is C")
print(trycha1(1))
print("This Is D")
print(trycha1(1))
print("This Is E")

