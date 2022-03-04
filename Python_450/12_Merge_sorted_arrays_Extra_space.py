class Solution():
    def __init__(self,arr1, arr2, n, m):
        self.arr1 = arr1
        self.arr2 = arr2
        self.n = n
        self.m = m

    def merge_arr(self):
        self.arr1.sort()
        self.arr2.sort()
        merge = []
        for i in range(0,len(self.arr1)-1):
            if self.arr1[i] in self.arr2:
                self.arr1.remove(self.arr1[i])
       
        m_array = self.arr1 + self.arr2
        m_array.sort()
        return m_array

if __name__ == "__main__":
    merge = Solution([5,7,1,3],[2,4,6,1],4,4)
    result = merge.merge_arr()
    print("Merged array : ",result)
