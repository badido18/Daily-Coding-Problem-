'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) 
returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

Implement car and cdr.

'''

#implementation

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(a):
    def t(a,b) :
        return a
    return a(t)
def cdr(a): 
    def k(a,b) :
        return b
    return a(k)

#Solution 

if __name__ == "__main__":

    print(car(cons(3,4)))
    print(cdr(cons(3,4)))
    pass