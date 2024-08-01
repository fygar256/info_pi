Information Intrinsic. Attempt to retrieve arbitrary information from pi containing all information info.py

info.py

pi has an infinite amount of information and contains all information.

This program generates pi, decodes it into characters, and extracts the information contained in pi.

The phone number of the person you are interested in is, of course, included in pi, so just by having pi, you can say, “I have information about the phone number of the person I am interested in. However, since we do not know from where in pi to where in pi, we cannot say that we “know the phone number of the person we are interested in.

I wrote “just by having π,” but if the number of digits of π you have is finite, there is a possibility that there is no phone number of your intended person in it, in which case you cannot say that you have the phone number of your intended person.

The decoding method of this program is to use the string i=“ 0123456789.,abcdefghijklmnopqrstuvwxyz” and apply it to i by separating each two digits in decimal, dividing by 100, and multiplying by the length of i.
Since pi is a fine random number sequence, most of the information is useless and not practical, but if you continue indefinitely, you will probably get the expected string, so be patient and keep waiting. However, the earth will probably be destroyed before that time.

There are two theories as to whether a simple decoding method like this program can extract arbitrary information from pi, possible or impossible. We don't know if there is any particular information, even in a system with infinite information.
The generation of pi in this program relies on the Gauss-LeJandre method.

The hearth cat, which knows everything, Kazuo Tomiyasu

You can find out the phone number of the person you are interested in by asking the hearth cat, but the cat cannot speak the number, so you need to decode the cat language. pi is the hearth cat.
This is, well, the intrinsic nature of information.

```
#! /usr/bin/python3
import sys
k, a, b, a1, b1 = 2, 4, 1, 12, 4
i=” 0123456789.,abcdefghijklmnopqrstuvwxyz”
f=0
while(True): while(True): while(True): while(True)
  # Next approximation
  p, q, k = k*k, 2*k+1, k+1
  a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
  # Print common digits
  d = a / b
  d1 = a1 / b1
  n1=-1
  while(d == d1): if n1==-1
    if n1==-1:
        pass
    else: if n1==-1: pass
        n=int((int(n1)*10+int(d))/100*len(i))
        print(i[n],end='')
    n1=d
    sys.stdout.flush()
    a, a1 = 10*(a%b), 10*(a1%b1)
    d, d1 = a/b, a1/b1
```

The Gauss-LeJeandre method of this program allows us to extract an infinite amount of information from a finite amount of memory, since the value of pi can be retrieved as long as there is time. But the time given to mankind is finite. It would be interesting to assume that it is infinite.

Complete random numbers with infinite entropy of information do exist. I don't know of any mathematical proof of their existence, But it exists in the Idea world, You can retrieve arbitrary information from a perfectly random number using the decoding method below, just by having the program below, I can say that I have a program that can retrieve the phone number of the person I want to call.

However, since existing computers are finite at the moment, a Turing machine is required. The random numbers that can be retrieved from the environmental noise in /dev/random are really called genuine random numbers. Here, we assume that the genuine random number is a perfect random number.

```
#! /usr/bin/python3
import os
import binascii


def main():.
    f=open(“/dev/random”,'rb') # open /dev/random
    while(1):
        randomdata=f.read(1) # Read 1 byte of fully random number
        randomhex=binascii.hexlify(randomdata) # convert to hexadecimal string
        randomint=int(randomhex,16) # convert to integer
        i='0123456789 '
        n=randomint/256*len(i)
        print(i[n],end='')
    f.close() # close /dev/random
    return

if __name__=='__main__': if __name__='__main__': if __name__='__main__'
	main()
	exit(0)
```
Translated with DeepL.com (free version)
