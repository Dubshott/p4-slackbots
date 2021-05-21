class BubbleSort_Megan:
    def __init__(self, input_list: object, string: object):

        self.input_list = input_list

        self.BubbleSort_Megan(input_list)

        self.string = string

    def BubbleSort_Megan(self, input_list):
        pass


list1 = 5, 4, 2, 1, 3
arr = [list1]
print("Original List:",arr)


def BubbleSort_Megan():
    n = len(arr)


    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if swapped == False:
            break

BubbleSort_Megan()

for i in range(len(arr)):
    print ("Sorted List:",arr[i],end=" ")