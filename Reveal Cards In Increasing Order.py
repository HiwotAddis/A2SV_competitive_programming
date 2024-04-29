class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res=[0]*len(deck)
        q=deque(range(len(deck)))
        for card in deck:
            i=q.popleft()
            res[i]=card
            if q:
                q.append(q.popleft())
        return res
