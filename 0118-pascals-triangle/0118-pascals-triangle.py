class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(1, numRows + 1):
            result.append(self.generateRow(i))
        return result
    def generateRow(self, row):
        ans = 1
        ansRow = [1]  # The first element is always 1
        
        for col in range(1, row):
            ans = ans * (row - col) // col
            ansRow.append(ans)
        
        return ansRow

