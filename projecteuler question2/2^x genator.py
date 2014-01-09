#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MonilRushi
#
# Created:     08/01/2014
# Copyright:   (c) MonilRushi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def twoexp(x):
    fibarray = []
    a = 0
    b = 1
    for i in range(x):
        a = b
        b = a + b
        fibarray.append(b)
    return fibarray
print twoexp(30)

def sumnumber(x):
    total = 0
    for i in x:
        if i < 4000000:
            total += i
    return total

print sumnumber(twoexp(40))
