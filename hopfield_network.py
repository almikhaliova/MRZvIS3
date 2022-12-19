class Matrix:
    def transp(A):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

    def multiply(A, B):
        if type(B[0]) == int:
            return list(list(sum([A[i][k] * B[k] for k in range(len(B))]) for i in range(len(A))))
        else:
            return list(list(sum([A[i][k] * B[k][j] for k in range(len(B))]) for j in range(len(B[0]))) for i in range(len(A)))

    def multiply_number(number, A):
        return [[A[i][j] * number for j in range(len(A[0]))] for i in range(len(A))]

class TemplatesManager:
    def __init__(self):
        self.file_name = ['GIRAFFE', 'FOX']
        self.pattern = self.file_to_pattern(self.file_name)
        self.giraffe = self.file_to_giraffe()
        self.fox = self.file_to_fox()

    def file_to_pattern(self, file_name):
        raw_text = list()
        for el in file_name:
            file = open(f"stan/{el}", "r")
            try:
                raw_text.append(file.read())
            finally:
                file.close()
        result = list()
        for sign in raw_text:
            pattern = []
            sign = self.convert_symbols(sign).split(' ')
            for element in sign:
                pattern.append(int(element))
            result.append(pattern)
            return result

    def convert_symbols(self, mystring):
        mystring = mystring.replace('*', '1 ').replace('.', '-1 ').replace('\n', '')[:-1]
        return mystring


    def file_to_giraffe(self):
        result = list()
        file = open("giraffe", "r")
        try:
            giraffe = file.read()
        finally:
            file.close()
        giraffe = self.convert_symbols(giraffe).split(' ')
        print(giraffe)
        for element in giraffe:
            result.append(int(element))
        return result

    def file_to_fox(self):
        result = list()
        file = open("fox", "r")
        try:
            fox = file.read()
        finally:
            file.close()
        fox = self.convert_symbols(fox).split(' ')
        print(fox)
        for element in fox:
            result.append(int(element))
        return result



MAX_TRIES = 500

class Network:
    def __init__(self, patterns):
        self.patterns = patterns
        self.weight_matrix = len(self.patterns)
        self.weight = [[0 for i in range(self.weight_matrix)] for j in range(self.weight_matrix)]

    def print(giraffe):
        result = ''
        for i in range(len(giraffe)):
            if i % 30 == 0:
                result += '\n'
            result += str(giraffe[i])
        print(result.replace('-1', '.').replace('1', '*'))

    def print(fox):
        result = ''
        for i in range(len(fox)):
            if i % 30 == 0:
                result += '\n'
            result += str(fox[i])
        print(result.replace('-1', '.').replace('1', '*'))

    def sign(element):
        return 1 if element >= 0 else -1

    def learning(self, my_giraffe):
        current_try = 0
        flag = True
        while flag:
            if my_giraffe in self.patterns and current_try >= MAX_TRIES:
                flag = False
            else:
                self.current_weight = MatrixOperation.multiply_number(1 / self.weight_matrix_size,
                                                                      MatrixOperation.multiply(
                                                                          MatrixOperation.transposition(self.patterns),
                                                                          self.patterns))
                for num in range(self.weight_matrix_size):
                    self.current_weight[num][num] = 0
                my_giraffe = MatrixOperation.multiply(self.current_weight, my_giraffe)
                temp_list = []
                for el in my_giraffe:
                    temp_list.append(Network.sign(el))
                my_giraffe = temp_list
                current_try = current_try + 1

        if self.checking(current_try):
            print('ERROR!')
        else:
            Network.print(my_giraffe)

    def learningf(self, my_fox):
        current_try = 0
        flag = True
        while flag:
            if my_fox in self.patterns and current_try >= MAX_TRIES:
                flag = False
            else:
                self.current_weight = MatrixOperation.multiply_number(1 / self.weight_matrix_size,
                                                                      MatrixOperation.multiply(
                                                                          MatrixOperation.transposition(self.patterns),
                                                                          self.patterns))
                for num in range(self.weight_matrix_size):
                    self.current_weight[num][num] = 0
                my_fox = MatrixOperation.multiply(self.current_weight, my_fox)
                temp_list = []
                for el in my_fox:
                    temp_list.append(Network.sign(el))
                my_fox = temp_list
                current_try = current_try + 1

        if self.checking(current_try):
            print('ERROR!')
        else:
            Network.print(my_fox)

    def checking(self, current_cnt):
        return current_cnt == MAX_TRIES