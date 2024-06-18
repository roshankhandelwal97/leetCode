#https://leetcode.com/problems/number-of-valid-words-in-a-sentence/description/

class Solution:
    def countValidWords(self, sentence: str) -> int:
        arr = sentence.split(' ')
        res = 0
        for i in arr: 
            count = 0
            for j in range(len(i)):
                # if i[j].islower():
                #     continue
                if i[j] == '-' and (j == 0 or j == len(i)-1 ):
                    break
                if i[j] == '-':
                    count +=1
                    if (not i[j-1].islower() or not i[j+1].islower()) or count > 1:
                        break
                if i[j] in ["!", ",", "."] and j != len(i) - 1:
                    break
                if i[j] == '':
                    break
                if i[j].isdigit():
                    break
                if j == len(i) - 1:
                    res +=1  

        return res
                        
