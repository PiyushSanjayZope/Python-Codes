class Maxmin:
    def __init__(self, arr):
        self.arr = arr

    def max_min_elt(self):
        max = 0
        min = self.arr[0]
        for i in range(len(self.arr)):
            if self.arr[i] > max:
                max = self.arr[i]
            if self.arr[i] < min:
                min = self.arr[i]
        return max,min

if __name__ == "__main__":
    find_max_min_elt = Maxmin([1,2,3,4,5])
    result = find_max_min_elt.max_min_elt()
    print("Max and Min Elt are : ",result)