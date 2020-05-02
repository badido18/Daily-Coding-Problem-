'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
aditinla ex :
[(0,5),(0,6),(2,7),(1,5),(6,8),(7,9)]
'''
if __name__ == "__main__":
    n = int(input())
    arr  = []
    for _ in range(n):
        arr.append(tuple(map(int,input().split(" "))))
    m=0
    print(arr)
    for i in range(min(min(arr)),max(max(arr))+1): 
        inter = 0  
        for x in arr :
            if i in range(x[0],x[1]) :
                inter+=1
        if m < inter :
            m = inter 
    print(m)
    pass