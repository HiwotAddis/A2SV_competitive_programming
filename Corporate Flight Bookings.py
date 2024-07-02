class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0]*n
        for f,s,seat in bookings:
            ans[f-1]+=seat
            if s <n:
                ans[s]+=(-seat)
        for i in range(1,n):
            ans[i]+=ans[i-1]
        return ans
