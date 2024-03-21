class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: # Loop through the List[str] pulling out each string
            res += str(len(s)) + '#' + s    # Encode it by adding the length of the string in front of the string followed by #
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # i is the pointer

        while i < len(s): # while 'i' is not at the end of the string
            j = i         
            while s[j] != "#": # Make sure that j is on the '#'
                j += 1
            length = int(s[i:j]) # the length of the word is from i up to j. Technically its (i + j) - 1 but # does not count
            res.append(s[j + 1 : j + 1 + length]) # Append the string to the list from the first letter to the last.
            i = j + 1 + length # Update i to be accurate
        
        return res