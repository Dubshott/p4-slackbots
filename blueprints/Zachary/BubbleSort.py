

class BubbleSort:
    def __init__(self, input_list, string):

        self.input_list = input_list

        self._output_list = []

        self.BubbleSort(input_list)

        self.string = string

    def BubbleSort(self, data):
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

    def string_sort(self, data):
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'j', 'K', 'L',
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                    'Y', 'Z']
        for j in range(0, len(data)):
            for i in range(0, len(data)):
                _sorted = False
                if i != len(data)-1:
                    for k in range(0, len(data[i])):
                        if not _sorted:
                            if k != (len(data[i]) and len(data[i+1])):
                                if alphabet.index(data[i][k]) > alphabet.index(data[i+1][k]):
                                    data[i], data[i+1] = data[i+1], data[i]
                                    _sorted = True
                                elif alphabet.index(data[i][k]) < alphabet.index(data[i+1][k]):
                                    _sorted = True
                                else:
                                    if len(data[i+1]) < len(data[i]):
                                        data[i], data[i+1] = data[i+1], data[i]
                                        _sorted = True

    def string_convert(self, data):
        for j in range(0, len(data)):
            data[j] = data[j].upper()

    @property
    def output_list(self):
        data = self.input_list
        if self.string:
            self.string_convert(data)
            self.string_sort(data)
            for i in range(len(data)):
                self._output_list.append(data[i])
            return self._output_list
        else:
            self.BubbleSort(data)
            for i in range(len(data)):
                self._output_list.append(data[i])
            return self._output_list
