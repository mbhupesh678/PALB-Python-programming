class Solution:
    def frequencySort(self, s):
        #Count frequency of each character
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        
       
        sorted_chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))
       #Sort characters by (frequency, character)
        result = ""
        for ch, count in sorted_chars:
            result += ch * count
        
        return result
