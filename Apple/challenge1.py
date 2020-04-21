'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''

import time 

def job():
    print("do you job")
    pass


if __name__ == "__main__":
    n= int(input('Enter n milliseconds : '))
    while True:
        job()
        time.sleep(n//1000)
    pass
