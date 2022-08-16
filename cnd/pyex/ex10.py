"""ex10.py
"""
def mergeList(list1, list2):
    list1 += list2
    lst = list(set([w.capitalize() for w in list1]))
    lst.sort()
    return lst

list1 = ["sam", "Sandra", "pETer", "Ethan"]
list2 = ["Peter", "Helen", "sanDRA", "frank", "Lynn"]

print(mergeList(list1, list2))