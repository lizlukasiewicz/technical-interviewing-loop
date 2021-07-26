arr = [453, "hello", 293, True]
def arrayCount(arr):
    i = 0
    if len(arr) > i:
        for x in arr:
            if type(x) != str:
                stringified = ''.join(map(str,arr))
                integer = int((len(stringified)))
            else:
                integer = int((len(x)))
            i += 1
        print(integer)
    else:
        print("all done!")

arrayCount(arr)