#Script to calculate various mathematical formulas using continued fractions
#http://en.wikipedia.org/wiki/Continued_fraction

import math

#Calculate e using continued fraction
def e(n):

    n = 100

    x = 0.0

    for i in range(n, 0, -1):
        if i % 3 == 1:
            m = int(i / 3) * 2
        else:
            m = 1

        x = 1.0 / (x + m)

    print (x + 1), math.e


#PI Using a continued Fraction

def pi(n):

    n = 900000

    x = 0.0

    for i in range(n, 0, -1):
        x = 1.0 / (x + 1.0 / i)

    print (x * 2.0 + 2.0), math.pi


#PI Using a Mandlebrot Fractal

#What relation is there between Pi and the Mandelbrot set ?
#This pretty picture at the top of the page is the Mandelbrot set (which is ... by the way).
#It is made up of the points c=x+i*y of the complex plane (with coordinates (x,y) in the catesian plane)
#such that the sequence Zn+1=Zn2+c with Z0=0 does not diverge.In practice to build up this set and dits
#graphical representation, one shows that when the modulus of Zn is greater than 2 it will diverge.
#No need to reach a big value ! The points c of this Mandelbrot set are represented in black
#(So the points for which Zn stays bounded), and the colours around represent the points according to the value
#of n from which we consider the sequence diverges. In 1991 David Bolle tried to verify if the narrowing
#we can see at (-0.75,0) was actually infinitely thin. That is to say that that however wide a non-zero
#width vertical line would be passing through that point it would meet the fractal set before the x-axis.
#And D Bolle then had the idea of using the point c=(-0.75,X) for the quadratic iteration and to make X
#tend to 0. And there, what was his surprise when he counted the number of iterations before which the series diverged
#and by discovering the following table .:

#The above passage was taken from http://www.pi314.net/eng/mandelbrot.php ...All credit to Boris Gourévitch for the excellent description

def Mandlebrot(n):    

    value = 5 

    logic = 1.0 / 10 ** value

    mandle = complex(-0.75, logic)

    c = mandle

    n = 0
    while True:
        n += 1
        mandle = mandle * mandle + c
        if abs(mandle) >= 2.0: break

    print (n * logic), math.pi
    
