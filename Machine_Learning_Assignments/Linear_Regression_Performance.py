# -*- coding: utf-8 -*-

import numpy
import pandas 
import matplotlib.pyplot as plt

print("Assignment 2")
list1 = [1, 2, 5]
list2 = [2, 4, 6]
xy = []
for num1, num2 in zip(list1, list2):
   xy.append(num1*num2)
print(xy)

print("Assignment 3")
def xySum_Prod(list1,list2):
    result=0
    for num1, num2 in zip(list1, list2):
       ##result = result + (num1*num2)
       result += (num1*num2)
    return result

print(xySum_Prod(list1, list2));

#Cost per click of individual keywords
x = [1.0, 2.1, 2.3, 2.5, 4.1, 4.5, 4.9, 5.9, 8.9]
#Total amount of clicks per day
y = [48.2, 63.0, 89.0, 71.0, 89.0, 82.2, 70.0, 80.0, 150.0]

print("Assignment 4")
def find_a(x,y):
    n = len(x)
    xSum = sum(x)
    ySum = sum(y)
    xySum = xySum_Prod(x,y)
    x2Sum = xySum_Prod(x,x)
    a = ((ySum * x2Sum) - (xSum*xySum))/(n*x2Sum - xSum*xSum)
    return a
a = find_a(x,y)
print(f"a: {a}")


print("Assignment 5")
def find_b(x,y):
    n = len(x)
    xSum = sum(x)
    ySum = sum(y)
    xySum = xySum_Prod(x,y)
    x2Sum = xySum_Prod(x,x)
    b = (n*xySum - xSum*ySum)/(n*x2Sum - xSum**2)
    return b
b = find_b(x,y)
print(f"b: {b}")

#b = 9.8 # try later 8 9 9.8
#a = 44.5 # try later 50 40 44.5

def h(x):
 return b*x + a

h(2)

A, B, C = 2.7, 1.6, 40.0
print(A,B,C)
def hPolynomial(x):
    return A*x**2 + B*x + C

hPolynomial(2)

plt.axis([0, 10, 0, 200])
plt.scatter(x, y)

regression_line = [h(item)for item in [0, 10]]
polynomial_line = [hPolynomial(item)for item in [0, 10]]

plt.xlabel("individual keywords")
plt.ylabel("amount of clicks per day")
plt.title("Linear Regression")
plt.plot([0, 10], regression_line)
plt.plot([0, 10], polynomial_line)

def Sum_Of_Squares(x_list, y_list, hFunc):
    xy2 =[]
    for numX, numY in zip(x_list,y_list):
        dif = hFunc(numX) - numY
        xy2.append(dif**2)
    return xy2

result = Sum_Of_Squares(x, y, h)
print(result)


from sklearn.metrics import mean_squared_error
import math
def RMSE(x_list, y_list, hFunc): 
    dif = []
    for numX, numY in zip(x_list,y_list):
        dif.append(hFunc(numX))
    MSE = mean_squared_error(y_list,dif)
    RMSE = math.sqrt(MSE)
    print(dif)
    return RMSE

print(RMSE(x,y,h))
print(RMSE(x,y,hPolynomial))

