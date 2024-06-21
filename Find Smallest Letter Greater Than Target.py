class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]
                break
        return letters[0]
