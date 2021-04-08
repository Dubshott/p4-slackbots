import random
from dominate.tags import a

roygbp="red,orange,yellow,green,blue,purple"
bbp="brown,black,pink"

class Color:

    def __init__(self, series):
        if series < 2 or series > 100:
            raise ValueError("Series must be between 2 and 100")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.color_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    def color_series(self):
        limit = self._series
        f = [(random.sample((roygbp), k=3))] #starting array/list
        while limit > 0:
            self.set_data(f[0])
            f = [f[1], f[0]]
            limit -= 1

    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]


    def get_sequence(self, nth):
        return self._dict[nth]

# Output
if __name__ == "__main__":

    n = 6

    color = Color(a/a)

print(f"Here are some colors = {color.list}")


