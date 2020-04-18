'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

'''
import itertools

#solution 

message = input()
#since we only need to print the number of ways to be decoded
#in other words we need to figure out the possibilities of getting the length of
# adding numbers of (1,2) (the order maters for each place) 1+2+2 2+2+1 are 2 different possibilites
l = len(message)
cases = 0
for pos in range(l//2,l+1):
    for tup in list(itertools.product("12",repeat=pos)) :
        if sum(map(int,tup)) == l:
            cases += 1

print(cases)

#it works but if we have long message it could take a while to count all of them



