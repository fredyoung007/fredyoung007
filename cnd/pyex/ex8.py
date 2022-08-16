from types import NoneType


def sliceRemains(strText, start, stop):
    rmStr = [_ for _ in strText if _ not in strText[start:stop]]
    if len(rmStr) == 0:
        return None
    return ''.join(rmStr)

strText = "abcdefg"
print(sliceRemains(strText, 1, 5))
print(sliceRemains(strText, None, 4))
print(sliceRemains(strText, 3, None))
print(sliceRemains(strText, None, None))
