cardict1 = {
    "brand": "Ford", 
    "electric": False, 
    "year": 1964, 
    "colors": ["red", "white", "blue"]
}

cardict2 = dict(
                brand="Ford", 
                electric=False, 
                year=1964, 
                colors=["red", "white", "blue"]
            )

cardict3 = dict(cardict1)
print(cardict1)
print(cardict2)
print(cardict1 == cardict3)