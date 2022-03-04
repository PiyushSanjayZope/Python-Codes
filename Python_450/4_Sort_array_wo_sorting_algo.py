class Sortwoalgo:
    def __init__(self, arr):
        self.arr = arr

    def sort_arr(self):
        for i in range(0,2):
            for j in range(0,2):
                if self.arr[j] > self.arr[j+1]:
                    temp = self.arr[j]
                    self.arr[j] = self.arr[j+1]
                    self.arr[j+1] = temp
        return self.arr

if __name__ == "__main__":
    sort_arr_woal = Sortwoalgo([3,1,2])
    result = sort_arr_woal.sort_arr()
    print("Sorted array is : ",result)