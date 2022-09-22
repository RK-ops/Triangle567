# -*- coding: utf-8 -*-

def classifyTriangle(a,b,c):
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'


    # require that the input values be >= 0 and <= 200
    if a >= 200 or b >= 200 or c >= 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'
    
        
    # now we know that we have a valid triangle 
    if a == b and b == c and c == a:
        return 'Equilateral'
    elif ((a**2) + (b**2)) == (c**2):
        return 'Right'
    elif (a==b) or (b==c) or (c==a):
        return 'Isoceles'
    else:
        return 'Scalene'
