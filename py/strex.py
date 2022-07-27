import os
import sys


# str.format(*parameters)

def sformat(): 
    frs =[
        (100, 10),
        (200, 16),
        (280, 12)
    ]

    header = "INCOME | PROFIT | PERCENT"
    template = "{income:>6} | {profit:^6} | {percent:<6.2%}"

    print(header)
    for i, p in frs:
        print(template.format(income=i, profit=p, percent=p/i))

    print("Hello {0}, how are you {1}?".format("Fred Young", "Fred"))

# str ETL
def sETL():
    fname = os.path.join(sys.path[0])+ "\\test.txt"
    
    with open(fname, "r") as inf:
        for line in inf:
            print(''.join(w[0].upper() for w in line.split()))
    
    inf = open(fname, 'r')
    words = inf.read().split()
    inf.close()

    redacted = [''.join('X' if c.isdigit() else c for c in word) for word in words]
    
    print(' '.join(redacted))

# sformat()
sETL()