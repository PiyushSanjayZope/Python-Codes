class Uniinterarr():
    def __init__(self,arr1,arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def uni_int(self):
        union = []
        inter = []
        
        temp_u1 = self.arr1[0:]
        temp_u2 = self.arr2[0:]

        temp_i1 = self.arr1[0:]
        temp_i2 = self.arr2[0:]
        
        union = temp_u1
        for i in range(len(temp_u2)):
            if i not in temp_u1:
                union.append(temp_u2[i])
        
        for k in range(len(temp_i1)):
            for j in range(len(temp_i2)):
                if temp_i1[k] == temp_i2[j]:
                    inter.append(temp_i1[k])
        return union, inter

if __name__ == "__main__":
    uni_inter_arr = Uniinterarr([1,2,4,7,3,8],[9,8,2,3,1,-1,-5])
    result = uni_inter_arr.uni_int()
    print("Union and Intersection is : ",result)