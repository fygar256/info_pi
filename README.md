---
title: Attempt to extract arbitrary information from π and true random number sequences
tags: Terminal Linux Python Information Theory PyPI
author: fygar256
slide: false
---

If π is a normal number, then it is a perfect random number sequence, containing infinite information and all information.

However, whether π is a normal number has not yet been proven in modern mathematics. It is conjectured to be a normal number. A normal number is a perfect random number sequence.

Here, we assume that π is a normal number.

This program generates π, decodes it into characters, and extracts the information contained in π.  

The decoding method used in this program involves using the string “i=” 0123456789.,abcdefghijklmnopqrstuvwxyz", dividing it into two-digit decimal numbers, dividing by 100, multiplying by the length of i, and applying it to i.

The information that can be extracted varies depending on the decoding method. Since π is a high-quality random number sequence, most of it is useless information and not very practical.

This program generates π using the Gauss-Legendre method.

```info.py
#!/usr/bin/python3
import sys
k, a, b, a1, b1 = 2, 4, 1, 12, 4
i=“ 0123456789.,abcdefghijklmnopqrstuvwxyz”
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
        n = int((int(n1) * 10 + int(d)) / 100 * len(i))
        print(i[n], end=‘’)
    n1 = d
    sys.stdout.flush()
    a, a1 = 10 * (a % b), 10 * (a1 % b1)
    d, d1 = a/b, a1/b1
```

In this program's Gauss-Legendre method, as long as there is enough time, the value of π can be obtained, allowing us to extract infinite digits of π from finite memory. However, the time given to humanity is finite. It would be interesting to assume infinity.

Next, we will attempt to extract arbitrary information from the environmental noise of /dev/random.

The random numbers that can be extracted from the environmental noise of /dev/random are actually called true random numbers. Here, we assume that true random numbers are perfect random numbers.

The difference between perfect random numbers and true random numbers is as follows.

| There are two types of random numbers that can be used in computers: pseudo-random numbers with a cycle and true random numbers obtained from a TRNG. There is also something called a “perfect random number,” which can only be handled probabilistically. In other words, perfect random numbers exist only in the realm of ideas.  

| “True random numbers” have a different definition from “perfect random numbers.”  
  
| • True random numbers are numbers that are inherently unpredictable and truly disordered. They are contrasted with pseudo-random numbers, which are generated arithmetically by computers. Physical random numbers that utilize quantum behavior, such as the decay of radioactive elements, are well known. True random numbers. - Shogakukan - From the Digital Daijisen dictionary.

|• Perfect random numbers refer to a sequence of numbers that occur in a completely random order and are also called ideal random numbers. They can only be handled probabilistically. - Search Labs | AI-generated.

|Although the definitions are different, it is acceptable to treat true random numbers as perfect random numbers and handle them similarly.

|Perfect random numbers have Jungian synchronicity (strange coincidences beyond causality), so the EPR paradox may have become EPR correlation, making it difficult or impossible to create them in the real world. Whether a true random number is a perfect random number or not has two possible answers: yes or no.

The phone number of the person you like is also included in the perfect random number sequence.

Since any information can be extracted from perfect random numbers using the decoding method below, simply having the program below means that you have a program that can extract the phone number of the person you like.

However, since it is unclear where in the normal number sequence the phone number is located, you cannot say that you know the phone number of the person you like.

If the number of trials is finite, there is a possibility that the phone number of the person you like is not included, in which case you cannot say that you have the phone number of the person you like.

A completely random number sequence is mostly useless information and not very practical, but if you continue it infinitely, the desired number sequence will probably appear, so be patient and keep waiting. However, the Earth will probably be destroyed before that happens.

Knowing everything, the stove cat, Tomiyasu Fūsei

The phone number of the person you like can be found by asking the stove cat, but since cats cannot speak numbers, decoding cat language is necessary. The proper number is the stove cat.

This is what we might call the intrinsic nature of information.

```phoneno.py
#!/usr/bin/python3
import os
import binascii


def main():
    f=open(“/dev/random”,‘rb’) # Open /dev/random
    while(1):
        randomdata=f.read(1) # Read 1 byte of completely random data
        randomhex=binascii.hexlify(randomdata) # Convert to a hexadecimal string
        randomint=int(randomhex,16) # Convert to integer
        i = ‘0123456789 ’
        n = randomint / 256 * len(i)
        print(i[n], end=‘’)
    f.close() # Close /dev/random
    return

if __name__ == ‘__main__’:
    main()
    exit(0)

```

Next, I tried to guess the three-digit code for a medicine cabinet.

The amount of information contained in an event that occurs with probability p is -log₂ p, so the amount of information contained in the answer to a safe code quiz with a probability of 1/1000 is -log₂ 1/1000 = 3log₂ 10 = 6.907755279.

If an event with probability 0 occurs, the information content is infinite, and if an event with probability 1 occurs, the information content is 0.

There are two definitions of the term “information content”:

① “Information content” as quantitatively defined in information theory.

② “Information content” as simply the number of bits of information in a sequence.

The unit is [bit].

Translated with DeepL.com (free version)
