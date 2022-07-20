#NEED TO IMPLEMENT TRIE BASED SOLUTION AS WELL

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        #Recursive approach
        def recursion(word, i, j, s):
            if j>=len(s) and i<len(word): return 0
            
            if i>=len(word): return 1
        
            if word[i]==s[j]: return recursion(word,i+1,j+1,s)
            else: return recursion(word,i,j+1,s)
            
        count = 0
        for word, cnt in Counter(words).items():
            count+=recursion(word,0,0,s)*cnt
        return count
        
        
        
        # Improved version 2
#         dt = defaultdict(list)
#         count = 0
#         for word in words:
#             dt[word[0]].append(word)
        
#         for ch in s:
#             wordList = dt[ch]
#             dt[ch] = []
            
#             for word in wordList:
#                 if len(word) == 1: count+=1
#                 else: dt[word[1]].append(word[1:])
#         return count
        
        
#         #Imrpoved version - seems odd though.. Should have been of similar time complexity
#         count = 0
#         for word, cnt in Counter(words).items():
#             i, match = 0,True
            
#             for ch in word:
#                 i = s.find(ch,i)+1
#                 if not i:
#                     match = False
#                     break
#             if match:
#                 count+=cnt
#         return count
        
        #brute force with slight modification
#         dt = {}
        
#         count = 0
#         for word in words:
#             if word in dt:
#                 if dt[word]:
#                     dt[word]+=1
#                     count+=1
#             else:
#                 i = 0
#                 for ind,ch in enumerate(word):
#                     found = False
#                     while(i<len(s)):
#                         if s[i]==ch:
#                             i+=1
#                             found = True
#                             break
#                         i+=1
#                     if ind==len(word)-1 and found:
#                         count+=1
#                         dt[word] = True
#                     if found==False:
#                         dt[word]=False
#                         break
#         return count

        
        