#!/usr/bin/python3
import sys
k, a, b, a1, b1 = 2, 4, 1, 12, 4
i=" 0123456789.,abcdefghijklmnopqrstuvwxyz"
f=0
while(True):
  # Next approximation
  p, q, k = k*k, 2*k+1, k+1
  a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
  # Print common digits
  d = a / b
  d1 = a1 / b1
  n1=-1
  while(d == d1):
    if n1==-1:
        pass
    else:
        n=int((int(n1)*10+int(d))/100*len(i))
        print(i[n],end='')
    n1=d
    sys.stdout.flush()
    a, a1 = 10*(a%b), 10*(a1%b1)
    d, d1 = a/b, a1/b1
