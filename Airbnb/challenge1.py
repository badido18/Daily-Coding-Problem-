'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, 
write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
 [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def getmaxna(arr,i):
    if i == len(arr)-1:
        return arr[i]
    else :
        try :
            return max(arr[i] + getmaxna(arr,i+2),getmaxna(arr,i+1))
        except IndexError :
            return 0

if __name__ == "__main__":

    arr = [2, 4, 6, 2, 5]
    print(getmaxna(arr,0))

    arr = [5, 1,1, 5]
    print(getmaxna(arr,0))

    pass

#done in less than 5min