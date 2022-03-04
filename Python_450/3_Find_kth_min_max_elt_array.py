class Kthmaxmin:
    def __init__(self, arr, kmax, kmin):
        self.arr = arr
        self.kmax = kmax
        self.kmin = kmin

    def kth_max_min_elt(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr)-1):
                temp = 0
                if self.arr[j] < self.arr[j+1]:
                    temp = self.arr[j]
                    self.arr[j] = self.arr[j+1]
                    self.arr[j+1] = temp
        max = self.arr[self.kmax-1]
        min = self.arr[len(self.arr)-self.kmin]
        return max,min

if __name__ == "__main__":
    kth_max_min_elt = Kthmaxmin([1,2,3,4,5],1,1)
    result = kth_max_min_elt.kth_max_min_elt()
    print("Kth Max and Kth Min Elt are : ",result)