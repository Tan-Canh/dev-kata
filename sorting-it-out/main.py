
from sqlalchemy import false

def sorting_balls(arr):
    if len(arr) == 0:
        return false
    list = []
    for i in arr:
        list.append(i)
    list.sort()
    return list
