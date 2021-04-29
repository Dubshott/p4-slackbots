

letters = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12,
           "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24,
           "y":35, "z":26}
#a = 1 b= 2 c = 3 d = 4 e = 5 f = 6 g = 7 h = 8 i = 9 j = 10 k = 11 l = 12 m = 13 n = 14 o = 15 p = 16 q = 17 r = 18 s = 19 t = 20 u = 21 v = 22 w = 23 x = 24 y = 25 z = 26

# creating a class
class bubbleSort:
    def init(self):
        for i in range(len(self) - 1, 0, -1): # (6, -1, 0, -1)
            for j in range(i):
                if self[j] > self[j + 1]:
                    temp = self[j]
                    self[j] = self[j + 1]
                    self[j + 1] = temp
            #print(f'Iteration: {abs(i - len(self))}', self)

# we are inserting a list now that the user can choose from and we are turning them into integers and splitting them with a comma
letter1 = input("Please input your first letter: ")
letter2 = input("Please input your first letter: ")
letter3 = input("Please input your first letter: ")
letter4 = input("Please input your first letter: ")
letter5 = input("Please input your first letter: ")
print("Awesome! You said,", letter1, letter2, letter3, letter4, letter5, ". In the alphabet these are numbered,", letters[letter1], letters[letter2], letters[letter3], letters[letter4], letters[letter5], ",respectively.")

def bubbleSort(data_to_sort):
    for i in range(len(data_to_sort) - 1, 0, -1):
        for j in range(i):
            if data_to_sort[j] > data_to_sort[j + 1]:
                temp = data_to_sort[j]
                data_to_sort[j] = data_to_sort[j + 1]
                data_to_sort[j + 1] = temp
        print(f'Iteration: {abs(i - len(data_to_sort))}', data_to_sort)
list_to_sort = [letter1, letter2, letter3, letter4, letter5]
print('Original List: ', list_to_sort)
bubbleSort(list_to_sort)
print('Sorted List: ', list_to_sort)