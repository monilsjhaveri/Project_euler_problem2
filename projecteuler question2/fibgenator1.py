#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      MonilRushi
#
# Created:     08/01/2014
# Copyright:   (c) MonilRushi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def fibgenator(x):
    fibarray = []
    a,b = 0,1
    for i in range(x):
        a,b = b, a +b
        fibarray.append(b)
    return fibarray
print fibgenator(40)

def sumnumber(x):
    total = 0
    for i in x:
        if (i < 4000000) and (i%2 == 0):
            total += i
    return total

print sumnumber(fibgenator(40))
