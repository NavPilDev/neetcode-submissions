from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We use default dict here since you cannot user a hashmap as a key, as it is muttable.
        res = defaultdict(list)
        ALPHABET_SIZE = 26
        for s in strs:
            # We create an array to get around the hashmap key constraint
            count = [0] * ALPHABET_SIZE
            for c in s:
                # ord(c) = the ASCII value of the character
                count[ord(c) - ord("a")] += 1
            # Tuples make arrays immutable, which allows us to follow the hashmap constaint
            # Default dict makes it to where if the key is not present, it will just add it.
            # If the key is there, then it gets appended to the existing key
            res[tuple(count)].append(s)
        # Return the values of the hasmap
        return list(res.values())
        