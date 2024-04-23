from itertools import combinations

class Target_sum:
    def __init__(self,array_target,exp,maxi):
        self.emplst = []
        self.reslst = []
        self.array_target = array_target 
        self.exp = exp 
        self.maxi = maxi
        self.generate_combinations()
        self.filter_case1()
        self.filter_numbers()
    def generate_combinations(self):
        for i in range(2,self.maxi+1):
            comb = list(combinations(self.array_target, i))
            self.emplst.append(comb)
    def filter_case1(self):
        filtered_numbers = [num for num in self.array_target if num ==self.exp]
        self.reslst.append(filtered_numbers)
    def filter_numbers(self):
       for i in self.emplst:
            res_w_lst = []
            for num in i:
                if sum(num) == self.exp:
                    res_w_lst.append(list(num))
            self.reslst.append(res_w_lst)
    def Displaying(self):
        for i in range(len(self.reslst)):
            if self.reslst[i] == []:
                print(f"ใช้ทั้งหมด item count = {i+1} ค่า ตามนี้ : N/A")
            else:
                print(f"ใช้ทั้งหมด item count = {i+1} ค่า ตามนี้ : {self.reslst[i]}")

        
if __name__ =='__main__':
    arrayInt = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    expectedResult = 200
    maximumItemCount = 4
    ts = Target_sum(arrayInt,expectedResult,maximumItemCount)
    ts.Displaying()