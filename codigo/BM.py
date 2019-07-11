#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy

def berlekampMassey(secuencia):
    n = len(secuencia)
    T = []

    c = [1]
    b = [1]
    for i in range(0, n-1):
        c.append(0)
        b.append(0)
        i+=1

    L = 0
    r = 0
    m = -1

    while r <= n-1:      
        d = 0

        for i in range(0, r+1):
            d = (d ^ (int(c[i]) and int(secuencia[r-i])))

        if d == 1:
            T = copy.copy(c)
            for j in range(0, ((n-r) + (m-1))):
                c[r-m+j] = c[r-m+j] ^ b[j]
            
            if L <= r/2:
                L = r + 1 - L
                m = r
                b = T                
        
        r = r + 1
        

    j=0
    for i in c:
        if i == 1:
            if j != 0:
                print(i,'x^(',j,')+')
            else:
                print(i,'+')
        j += 1
    i += i

    return L