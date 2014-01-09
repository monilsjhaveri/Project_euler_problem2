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
def fibGenerator():
    a, b = 0, 1
    yield 0
    while True:
        a, b = b, a + b
        yield a

fibonaccinumbers = []
fib = fibGenerator()
for n in range(75):
    fibonaccinumbers.append(next(fib))
print fibonaccinumbers