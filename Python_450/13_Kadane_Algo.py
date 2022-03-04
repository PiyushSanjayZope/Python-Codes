class Maxsubarray():
    def __init__(self,arr):
        self.arr = arr

    def maxsarr(self):
        max_current = max_global = self.arr[0]
        for i in range(1,len(self.arr)-1):
            max_current = max(self.arr[i],max_current + self.arr[i])
            if max_current > max_global:
                max_global = max_current
        return max_global

if __name__ == "__main__":
    rot_arr = Maxsubarray([-1,2,3,4,5])
    result = rot_arr.maxsarr()
    print("Max sub array is : ",result)