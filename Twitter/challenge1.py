'''
 Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system.
 That is, given a query string s and a set of all possible query strings,
  return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

import re

def autocomplete(s,dic):
    output = []
    for x in dic :
        if re.match(s+r"\w*",x):
            output.append(x)
    return output
    
if __name__ == "__main__":

    inp = input()
    dictionary = ["madjid","madre","mecal","nada","badido18"]
    print(autocomplete(inp,dictionary))    
    pass