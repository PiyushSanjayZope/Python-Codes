class Rotate_arr():
    def __init__(self,arr,rotn):
        self.arr = arr
        self.rotn = rotn

    def rot_array(self):
        arr_r = []
        if self.rotn > len(self.arr):
            self.rotn = self.rotn - len(self.arr)
        for i in range(self.rotn,0,-1):
            arr_r.append(self.arr[len(self.arr)-i])
        
        for i in range(len(self.arr)-self.rotn):
            arr_r.append(self.arr[i])
        return arr_r

if __name__ == "__main__":
    rot_arr = Rotate_arr([1,2,3,4,5],6)
    result = rot_arr.rot_array()
    print("Rotated array is : ",result)