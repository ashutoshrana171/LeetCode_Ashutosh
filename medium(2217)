"""
Q:
Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.

A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.
"""
# Working code with time complexity check
class Solution(object):
    def kthPalindrome(self, queries, intLength):
            #check for boundary conditions
            if not (len(queries) >=1 and  len(queries)<= 5*(10**4)) or (not (intLength >= 1 and intLength <=15)):
                return -1

            #concentrate on half the number the other half is just a reflection
            base = 10**((intLength-1)/2)
            result = [q-1+base for q in queries] # store first half of numbers
            for i,x in enumerate(result):
                temp = str(x) + str(x)[-1 - intLength%2::-1] #concatenate reflection to form pallindrome
                result[i] = int(temp) if len(temp) == intLength else -1

            return result

            


# This code exceeds time
class Solution(object):
    def kthPalindrome(self, queries, intLength):
            #check for boundary conditions
            if not (len(queries) >=1 and  len(queries)<= 5*(10**4)) or (not (intLength >= 1 and intLength <=15)):
                return -1

            #define pallindrome check function
            def pallindrome(x):
                x = str(x)
                return x==x[::-1]

        
            #get highest and lowest numbers from intlength
            smallest = 10**(intLength-1) # if intLength = 2; smallest = 10^1 = 10
            largest = 10**intLength - 1  # if intLength = 2; largest = 10^2 -1 = 99

            #iterate and check each number for pallindrome and store pallindrome number to temp
            temp = []
            for i in range(smallest,largest+1):
                if str(i)==str(i)[::-1]:
                    temp.append(i)
            
            #return query indexed pallindrome
            result = []
            for i in queries:
                if not (i>=1) and not (i<= 10**9):
                    return -1
                else:
                    if i<len(temp)+1:
                        result.append(temp[i-1])
                    else:
                        result.append(-1)
            
            return result
