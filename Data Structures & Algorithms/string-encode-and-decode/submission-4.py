class Solution:
    # We are given two machines that are encode and decode respectively.
    # Machine 1 sends of a List of strings to be encodeded within it self
    # Machine 2 recieves the encoded string, and has to decoded it into 
    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedStrs = []
        i = 0
        
        while i < len(s):
            # j is the location of the delimeter
            j = s.find('#',i)
            # s[i to j] gets the length of the encoded str fragment
            length = int(s[i:j])
            # Since j is the location, we increment by 1 to get the
            # start of the string, and the end of the string is given 
            # by incrementing j by both 1 and the lenght found earlier.
            decodedStrs.append(s[j+1:j+1+length])
            # The new lower bound of this scan will be after the 
            # fragment we have just decoded
            i = j + 1 + length
        return decodedStrs
