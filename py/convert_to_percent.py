def convert_to_percent(scores_list, out_of):
    lst = []
    ratio = 100 / out_of
    for i in scores_list:
        lst.append(round(i * ratio))
    scores_list[:] = list(lst)

marks = [25.5,50,49,15.9,0]
convert_to_percent(marks, 50)
print(marks)
