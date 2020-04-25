'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''
import math
if __name__ == "__main__":
    pi = 0
    for i in range(1,2000):
        pi += 1/(pow(i,2))
    print(math.sqrt(pi*6))
    pass