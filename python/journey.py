def get_journey(connections, start) :
    jl = []
    if start not in dict.keys():
        raise ValueError("key is not valid")
    else:
        jl.append(start)
    nk = dict.get(start)
    while nk is not None:
        if (nk not in dict.keys()):
            raise ValueError("key is not valid")
        jl.append(nk)
        nk = dict.get(nk)
    return jl

dict = {'a':'q', 'd':'a', 'e':'f', 'q':None, 'f':'i', 'g':'h'}
print(get_journey(dict, 'd'))

dict = {'a':'q', 'd':'a', 'e':'f', 'q':None, 'f':'i', 'g':'h'}
try:
    print(get_journey(dict, 'i'))
except ValueError as err:
    print('{}'.format(err))