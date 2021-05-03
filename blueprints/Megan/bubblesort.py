class BubbleSort:
    def __init__(self, input_list: object, string: object):

        self.input_list = input_list

        self.BubbleSort(input_list)

        self.string = string

Variable1 = input("Enter a string: ")
int_list = list(map(int, Variable1.split(",")))
List1 =[]
list1.append(int_list)
print("List")
print(list1)
BubbleSort.init(int_list)
list2 = []
lists.append(int_list)
print("Sorted list")
print(lists)

def BubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if swapped == False:
            break


BubbleSort(arr)

for i in range(len(arr)):
    print ("%d" %arr[i],end=" ")

