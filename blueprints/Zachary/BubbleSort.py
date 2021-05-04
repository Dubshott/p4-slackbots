

class BubbleSort_zach:
    def __init__(self, input_list: object, string: object):

        self.input_list = input_list

        self.BubbleSort_zach(input_list)

# I thought I needed to tell python if it is a string or not but clearly python is smarter than I am
        self.string = string

# Found this algorithm on the internet that seems to work great and handle all of the cases
    def BubbleSort_zach(self, data):
        n = len(data)

        # Traverse through all array elements
        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n-i-1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]