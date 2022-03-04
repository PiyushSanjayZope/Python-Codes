class Solution():
    def __init__(self,arr, n_size):
        self.arr = arr
        self.n_size = n_size

    def min_jumnps(self):
        jumps = 0
        for i in range(0,len(self.arr)-1):
            if self.n_size > 0:
                self.n_size = self.n_size - self.arr[i]
                jumps = jumps + 1
        return jumps

if __name__ == "__main__":
    min_j = Solution([1,3,4,1,2,5,1,2,7],9)
    result = min_j.min_jumnps()
    print("Max jumps : ",result)
