for i in dir("Hello"):
    for j in dir(i):
        print "%s    %s     %s" % (type("s"), i, j)


for i in dir(1):
    for j in dir(i):
        print "%s     %s    %s" % (type(1), i, j)

for i in dir({}):
    for j in dir(i):
        print "%s     %s    %s" % (type({}), i, j)

for i in dir([]):
    for j in dir(i):
        print "%s     %s    %s" % (type([]), i, j)

