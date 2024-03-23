class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        temp=capacity
        i=0
        steps=0
        while i <len(plants):
            if capacity>= plants[i]:
                capacity-=plants[i]
                steps+=1
                i+=1
            else:
                steps+=i*2
                capacity=temp
        return steps 
