class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_count = Counter(words[0])
        for word in words[1:]:
            char_count &= Counter(word)
        result = []
        for char, count in char_count.items():
            result.extend([char] * count)
        return result
