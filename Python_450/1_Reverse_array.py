class Reverse:
    def __init__(self, arr, start, end):
        self.arr = arr
        self.start = start
        self.end = end

    def reverseList(self):
        while self.start < self.end:
            self.arr[self.start], self.arr[self.end] = self.arr[self.end], self.arr[self.start]
            self.start += 1
            self.end -= 1
        return self.arr

if __name__ == "__main__":
    reverse_obj = Reverse([1,2,3,4,5],0,4)
    result = reverse_obj.reverseList()
    print("Rev list is : ",result)