"""ex6.py
"""
def strFilter(st, ft):
    """
    Takes in a string st and a filter symbol ft as input arguments

    This function prints out: <TBA>

    Parameters
    ----------
    st : str
        A string.
    ft : str
        A filter symbol.

    Returns
    -------
    No return
    """
    n = len(st)
    while n > 0:
        print(st[-n]*n + ft*(len(st)+1-n))
        n -= 1

strFilter("abc", '*') 
strFilter("hello", '!')
        