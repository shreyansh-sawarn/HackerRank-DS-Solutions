#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        
        count = 0

        for x in range(n, 1, -1):
            for y in range(x-1, 0, -1):
                kk = x & y
                if kk > count and kk < k:
                    count = kk
                if count == k - 1:
                    break
            if count == k - 1:
                break

        print(count)