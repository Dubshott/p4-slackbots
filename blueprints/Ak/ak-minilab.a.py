"""Paraphrased off of mortensen's code for the fibonacci series but created new series"""


class AKsequnce:
    def __init__(self, series):
        if series < 0 or series > 500:
            raise ValueError("Must be between 0 and 500")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.calculate_series()

    def calculate_series(self):
        limit = self._series
        f = [0, 1,2,3,4]
        while limit > 1:
            self.set_data(f[0])
            f = [f[1], f[0] - f[1]]
            limit -= 1

    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1
#getters with decorators
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 3]

    def get_sequence(self, nth):
        return self._dict[nth]

if __name__ == "__main__":
    n = 34
    fibonacci = AKsequnce(n)
    print(f"AK series for {n} = {fibonacci.number}")
    print(f"AKseries for {n} = {fibonacci.list}")
    for i in range(n):
        print(f"Fibonacci sequence {i + 1} = {fibonacci.get_sequence(i)}")
    #I created a new series that adds the abs values and will change from negitive to positive