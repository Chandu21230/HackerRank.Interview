#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n=len(arr)
    count1=0
    count2=0
    count3=0
    #int a,b,c
    for j in range(n):
        i=arr[j]
        if i>=1:
            count1=count1+1
        elif i<=-1:
            count2+=1
        else:
            count3+=1
    a=count1/n
    b=count2/n
    c=count3/n
    #arr.append(a)
    #arr.append(b)
    #arr.append(c)
    print(a)
    print(b)
    print(c)
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
