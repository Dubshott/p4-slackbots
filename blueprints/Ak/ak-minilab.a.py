class bubbleSort:
    def init(self):
        for i in range(len(self) - 1, 0, -1): # (6, -1, 0, -1)
            for j in range(i):
                if self[j] > self[j + 1]:
                    temp = self[j]
                    self[j] = self[j + 1]
                    self[j + 1] = temp

            print(f'Iteration: {abs(i - len(self))}', self)

example_string = input("enter string: ")
int_list = list(map(int, example_string.split(",")))


#Printing the original list code;/code'';
listO = []

listO.append(int_list)
print("OriginalList")
print(listO)
#sorted list
bubbleSort.init(int_list)
listS = []
listS.append(int_list)
print("Sorted List")
print(listS)
# print('Sorted List: ', list_to_sort)
#Logic for sorting
def bubbleSort(data_to_sort):
    for i in range(len(data_to_sort) - 1, 0, -1):
        for j in range(i):
            if data_to_sort[j] > data_to_sort[j + 1]:
                temp = data_to_sort[j]
                data_to_sort[j] = data_to_sort[j + 1]
                data_to_sort[j + 1] = temp

        print(f'Iteration: {abs(i - len(data_to_sort))}', data_to_sort)


list_to_sort = [90, 50, 10, 20, 70, 60, 40, 30, 80]
print('Original List: ', list_to_sort)
bubbleSort(list_to_sort)
print('Sorted List: ', list_to_sort)