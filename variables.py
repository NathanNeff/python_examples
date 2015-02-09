#!/usr/bin/env python

var1 = 0

def func1():
    global var1
    var1 = var1 + 1
    func2()


def func2():
    global var1
    var1 = var1 + 1

func1()
print var1
