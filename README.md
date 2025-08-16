If pi is a normal number, then it is a perfectly random number sequence, and pi has infinite information content, containing all information.

However, whether pi is a normal number has not yet been proven in modern mathematics. It is conjectured that it is a normal number. Normal numbers are perfectly random number sequences.

Here, we will assume that pi is a normal number.

This program generates pi, decodes it into characters, and extracts the information contained in pi.

The decoding method for this program uses the string i=" 0123456789.,abcdefghijklmnopqrstuvwxyz", divides it into decimal digits, divides it by 100, multiplies it by the length of i, and applies the result to i.

The information that can be extracted varies depending on the decoding method. Since pi is a high-quality random number sequence, most of it is useless information and not of practical use.

The generation of pi in this program relies on the Gauss-Legendre algorithm.

```info.py
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
n=int((int(n1)*10+int(d))/100*len(i)) print(i[n],end='')
n1=d
sys.stdout.flush()
a, a1 = 10*(a%b), 10*(a1%b1)
d, d1 = a/b, a1/b1
```

This program's Gauss-Legendre algorithm allows us to extract the value of π given enough time, so we can extract an infinite number of digits of π from a finite amount of memory. However, humanity's time is finite. It would be interesting to assume it's infinite.

Next, we attempt to extract arbitrary information from the environmental noise in /dev/random.

Random numbers that can be extracted from the environmental noise in /dev/random are actually called true random numbers. Here, we're assuming that true random numbers are completely random.

The difference between completely random numbers and true random numbers is as follows:

|There are two types of random numbers that computers can use: pseudorandom numbers with a period, and true random numbers obtained from a TRNG. There is also something called "perfectly random numbers," which can only be handled probabilistically. In other words, perfect random numbers exist only in the realm of ideas.

|

| "True random numbers" have a different definition from "perfectly random numbers."

|

| True random numbers are fundamentally unpredictable and truly chaotic random numbers. They are the opposite of pseudorandom numbers, which are generated arithmetically by computers. Physical random numbers that utilize quantum behavior, such as the decay of radioactive elements, are known as true random numbers. - Shogakukan - From the Digital Daijisen Dictionary.

|

| Perfectly random numbers refer to a sequence of numbers that occur in a completely random order, and are also called ideal random numbers. They can only be handled probabilistically. - Search Labs | By AI.

|

| Although the definitions are different, true random numbers can be considered to be perfect random numbers and treated in the same way.

|

|Perfectly random numbers are subject to Jungian synchronicity (strange coincidences that transcend the laws of causality), and since the EPR paradox has become the EPR correlation, it may be difficult or impossible to create in the real world. There are two answers to the question of whether truly random numbers are truly random: yes or no.

The phone number of a person of interest is also included in a truly random number sequence.

Any information can be extracted from a truly random number using the decoding method below, so simply possessing the program below can be said to "possess a program that can extract the phone number of a person of interest."

However, since it is impossible to know the range of normal numbers, it cannot be said that "I know the phone number of a person of interest."

If the number of attempts is finite, there is a chance that the phone number of the person of interest will not be included, in which case it cannot be said that the person of interest's phone number is possessed.

A truly random number sequence is mostly useless information and is not practical, but if you continue infinitely, the desired number sequence will probably appear, so be patient and wait. However, the Earth will probably be destroyed before that happens.

The Kamaneko, who knows everything - Tomiyasu Fuu

You can find out the phone number of someone you like by asking Kamaneko, but since cats can't speak numbers, you'll need to decode it in cat language. The official number is Kamaneko.

This is what you might call the intrinsic nature of information.

```phoneno.py
#!/usr/bin/python3
import os
import binascii

def main():
f=open("/dev/random",'rb') # Open /dev/random
while(1):
randomdata=f.read(1) # Read one byte of completely random data
randomhex=binascii.hexlify(randomdata) # Convert to a hexadecimal string
randomint=int(randomhex,16) # Convert to an integer
i='0123456789'
n=randomint/256*len(i)
print(i[n],end='')
f.close() # Close /dev/random
return

if __name__=='__main__':
main()
exit(0)

```

Next, I tried to guess the three-digit number on the medicine cabinet lock.

Since the amount of information contained in an event occurring with probability p is -log_2 p,the amount of information contained in the answer to a safe key riddle that has a 1/1000 chance of being correct is -log_2 1/1000=3log_2 10=6.907755279.

If an event occurs with probability 0, the amount of information is infinite, and if an event occurs with probability 1, the amount of information is 0.

The term "information amount" requires two definitions:

1) "information amount" as quantitatively defined in information theory.

2) "information amount" that simply expresses the number of digits of 1 bit of information.

The unit is 'bit'.
