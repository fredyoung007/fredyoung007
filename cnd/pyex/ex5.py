"""ex5.py
"""
def calCost(cost, dest):
    shipCost = 0
    if (dest == "Europe"):
        if cost < 50:
            shipCost = 15
        elif (cost >= 50) and (cost < 100):
            shipCost = 10
        elif (cost >= 100) and (cost < 200):
            shipCost = 5
        elif cost >= 200:
            shipCost = 0
    else:
        if cost < 100:
            shipCost = 20
        else:
            shipCost = 0
    
    return shipCost + cost

print(calCost(100, "Europe"))
print(calCost(50, "USA")) 

