class Movenegtive():
    def __init__(self,arr):
        self.arr = arr

    def move_neg(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr)-1):
                if self.arr[j] > self.arr[j+1]:
                    temp = self.arr[j]
                    self.arr[j] = self.arr[j+1]
                    self.arr[j+1] = temp
        return self.arr

if __name__ == "__main__":
    move_arr_side = Movenegtive([1,2,-4,3,-2,-6,-9,7])
    result = move_arr_side.move_neg()
    print("Negative sorted array is : ",result)