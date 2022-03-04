class Solution():
    def __init__(self,arr):
        self.arr = arr

    def occurance(self):
        d_num = 0
        for i in range(1, len(self.arr)):
            if self.arr[i] == self.arr[i-1]:
                d_num = self.arr[i]
                return d_num

if __name__ == "__main__":
    occ_num = Solution([1,3,3,4,6,8,9])
    result = occ_num.occurance()
    print("Duplicate number : ",result)
