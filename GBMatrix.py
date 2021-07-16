import random
#если я не хочу определять матрицу самостоятельно

class Matrix:
    def __init__(self, strings, columns, start, limit):
        self.strings = 3
        self.columns = 3
        self.limit = 99
        self.start = 0

    def generateMatrix(self):
        matrix = []
        s = 0
        while s < self.strings:
            a = random.sample(range(self.start, self.limit), self.columns)
            matrix.append(a)
            s += 1
        return matrix

    def manyMatrix(self,other):
        a=Matrix.generateMatrix(self)
        print(a)
        b=Matrix.generateMatrix(other)
        print(b)
        newmatrix=[]
        if self.strings==other.columns:
            for line in a:
                lineindex = 0
                newline=[]
                counter=0
                newel=0
                index=0
                while counter<self.strings:
                    lineindex=0
                    for el in line:
                        newel+=el*b[lineindex][index]
                        lineindex+=1
                        if lineindex==self.strings:
                            newline.append(newel)
                            newel=0
                            index+=1
                            counter+=1
                newmatrix.append(newline)
        else:
            print ("Умножение невозможно")
        return newmatrix

a=Matrix(3,3,0,9)
a.strings=3
a.limit=9
b=Matrix(3,3,0,9)
b.limit=9
print(a.manyMatrix(b))

#если я хочу ввести свою матрицу

class MyMatrix():
    def __init__(self,args):
        self.matrix=args

    def manyMyMatrix(self,other):
        other=MyMatrix(other.matrix)
        newmatrix=[]
        for linea in other.matrix:
            if len(self.matrix) == len(linea):
                pass
            else:
                print ('Умножение невозможно')
        for line in self.matrix:
            lineindex = 0
            newline = []
            counter = 0
            newel = 0
            index = 0
            while counter < len(self.matrix):
                 lineindex = 0
                 for el in line:
                    p=other.matrix [lineindex][index]
                    newel += el * p
                    lineindex += 1
                    if lineindex == len(self.matrix):
                        newline.append(newel)
                        newel = 0
                        index += 1
                        counter += 1
            newmatrix.append(newline)
        return newmatrix


n=MyMatrix([[1,2,3],[4,5,6],[7,8,9]])
m=MyMatrix([[10,11,12],[13,14,15],[16,17,18]])
print(n.manyMyMatrix(m))

#если я запрашиваю матрицу с клавиатуры

def tapMatrix(strings, columns):
    a=[]
    sa=1
    matrix=[]
    while sa <= strings:
        a=input(f"Введите значения {sa} строки матрицы #1 через пробел:").split(' ')
        while len(a) < columns:
            a.append("0")
        index=0
        newa=[]
        for el in a:
            if el.isdigit()==True:
                newa.append(float(el))
                index+=1
                if index==columns:
                  matrix.append(newa)
                  sa+=1
                  break
            else:
                print('Cтрока введена неверно. Введите строку из чисел')
        return matrix
print (tapMatrix(2,4))
