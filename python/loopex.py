rateings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
while (rateings[i] > 6):
    print(rateings[i])
    i += 1


squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
newSquares = []
i = 0

while (i<len(squares)) and (squares[i] == "orange"): 
    newSquares.append(squares[i])
    i += 1
print(newSquares)
