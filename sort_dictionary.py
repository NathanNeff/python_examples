foo = {
        'a' : 2,
        'b' : 3,
        'c' : -4,
        'd' : 42,
        'e' : 16,
        'f' : 3,
        'g' : 8000,
        'h' : 8000 }

srtd = sorted(foo.items(), key=lambda(k,v):(v,k))

for i in range(-1, -5, -1):
    print srtd[i]

