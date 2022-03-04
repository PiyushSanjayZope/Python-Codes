class Solution():
    def __init__(self,arr, n):
        self.arr = arr
        self.n = n

    def inversionCount(self):
        min = self.arr[0]
        max = 0
        count = 0
        count1 = 0
        for i in range(len(self.arr)-1):
            if self.arr[i] > self.arr[i+1]:
                min = self.arr[i+1]
                count = count + 1
        for j in range(len(self.arr)-1):
            if self.arr[i] < self.arr[j+1]:
                max = self.arr[j+1]
                count1 = count1 + 1
        inversions = count + count1
        return inversions

if __name__ == "__main__":
    min_j = Solution([4,3,7,5,8,1,9],7)
    result = min_j.inversionCount()
    print("Inversions Required are : ",result)
