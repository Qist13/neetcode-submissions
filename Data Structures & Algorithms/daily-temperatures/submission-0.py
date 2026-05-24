class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            cur_temp = temperatures[i]
            for j in range(i, len(temperatures)):
                if temperatures[j] > cur_temp:
                    result[i] = j - i
                    break
        
        return result