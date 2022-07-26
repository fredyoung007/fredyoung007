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

dic = {'john':'1','alice':'90','rook':'45','emma':'22','roz':'11'} 
dic.update({'fred':'16'})
dic["fred"] = '18
skdic = dict(sorted(dic.items(), key=lambda item: item[0]))
svdic = dict(sorted(dic.items(), key=lambda item: item[1]))
print(skdic)
print(svdic)