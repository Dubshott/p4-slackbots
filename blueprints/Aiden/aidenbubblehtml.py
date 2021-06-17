class bubblesort_aiden:
    def __init__(self, input_list: object, string: object):
        self.input_list = input_list
        self.bubblesort_aiden(input_list)
        self.string = string

    def bubblesort_aiden(self, data):
        n = len(data)
        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n-i-1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
