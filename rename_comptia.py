def enumer(lee):
    for i in enumerate(lee, start=1):
        yield (i)

pako = ['a','b','c','d','e']

for p in enumer(pako):
    print(p)



