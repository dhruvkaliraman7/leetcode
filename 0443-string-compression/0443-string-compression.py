class Solution:
    def compress(self, chars: List[str]) -> int:
        inputInd = 0
        start , end = 0, len(chars) 
        while start<end:
            tmpChar = chars[start]
            tmpCount = 1
            start += 1
            while start < end and chars[start] == tmpChar:
                tmpCount += 1
                start += 1
            chars[inputInd] = tmpChar
            inputInd += 1
            if tmpCount > 1:
                str_count = str(tmpCount)
                for l in str_count:
                    chars[inputInd] = l
                    inputInd += 1
        return inputInd
        