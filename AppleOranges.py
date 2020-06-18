#!/bin/python3

import math
import os
import random
import re
import sys

# Function to count Apples And Oranges 
def countApplesAndOranges(s, t, a, b, m, n, apples, oranges):
    count_apples=0
    count_oranges=0
    for i in range(0,m):
        sum=0
        sum=a+ apples[i]
        if sum >= s and sum <= t:
            count_apples=count_apples + 1
    print(count_apples)
    for i in range(0,n):
        sum=0
        sum=b+ oranges[i]
        if sum >= s and sum <= t:
            count_oranges=count_oranges + 1
    print(count_oranges)
if __name__ == '__main__':
    st=input().split()
    s=int(st[0])
    t=int(st[1])
    ab=input().split()
    a=int(ab[0])
    b=int(ab[1])
    mn=input().split()
    m=int(mn[0])
    n=int(mn[1])
    apples=list(map(int, input().rstrip().split()))
    oranges=list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, m, n, apples, oranges)
