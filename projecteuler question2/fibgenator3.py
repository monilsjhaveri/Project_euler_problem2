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

def fibgenatator(x):
    fibarray = []
    a = 0
    b = 1
    for i in range(x):
        a = b
        b = a + b
        fibarray.append(b)
    return fibarray
print fibgenatator(20)