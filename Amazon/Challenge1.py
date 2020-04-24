'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, 
find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


"aafregfdsqsfddf" k=2
we have aaf sqs fddf
return fddf so longest = 4 
'''




if __name__ == "__main__":
    s ,k = input().split(" ")
    k = int(k) 
    m = 0
    car =""
    for i in range(len(s)):
        ct = set() #disctinct caracters
        j = i
        tmp = "" #seq caracter
        while len(ct)<=k and j<len(s):
            if s[j] in ct:
                tmp+=s[j] 
            else :                
                ct.add(s[j])
                if  len(ct)<=k :
                    tmp+=s[j] #no caracters at the end execption for the second loop
            j+=1
        if len(tmp) > len(car) : 
            car = tmp  #save the caracters sequence
    print(car,len(car))
    pass