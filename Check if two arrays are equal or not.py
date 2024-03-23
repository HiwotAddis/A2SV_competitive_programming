class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
    
        dict_A = {}
        dict_B = {}

        for num in A:
            dict_A[num] = dict_A.get(num, 0) + 1
    
        for num in B:
            dict_B[num] = dict_B.get(num, 0) + 1
        return dict_A == dict_B
