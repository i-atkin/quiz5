#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:19:14 2021

@author: i_atkin
"""

# load needed packages
from pylab import *
from scipy.integrate import quad

# define the integrand function
def gaus(x):
	return 1/(o*np.sqrt(2*pi))*exp(-1/2*(((x-u)**2)/o**2))

o=1
u=0
quad(gaus,-inf,inf)


# define erfc(x) function
def erfc(x):
    # extract value of the integral, ignore error estimate
	value,error = quad(gaus,x,inf)
	return 2.*value/sqrt(pi)

# create arrays for x and the erfc(x)
N = 100
x = linspace(-3,3,N)
# array to hold results of erfc()
y = zeros(N)
for idx in range(100):    # for loop is needed because quad() doesn't allow array arguments
	y[idx] = erfc(x[idx])

# probability that velocity lies within -o to o
a = quad(gaus,-o,o)
print(a[0])


# plot the result
figure(1)
clf()
xlabel('x values (velocities)')
ylabel('erfc(x) (integrated probability)')
plot(x,y)
