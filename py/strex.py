# str.format(*parameters)
frs =[
    (100, 10),
    (200, 16),
    (280, 12)
]

header = "INCOME | PROFIT | PERCENT"
txt = "{income:>6} | {profit:^6} | {percent:<6.2%}"

print(header)
for i, p in frs:
    print(txt.format(income=i, profit=p, percent=p/i))