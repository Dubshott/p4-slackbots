class Sequence:

    def __init__(self, series):

        if series < 2 or series > 100:
            raise ValueError("Series must be between 2 and 100")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.calc_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    def calc_series(self):
        limit = self._series
        f = [0, 1]  #starting array/list
        while limit > 0:
            self.set_data(f[0])
            f = [f[1], f[0] + f[1]]
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

    n = 24

    sequence = Sequence(n)

    print(f"Sequence for {n} = {sequence.number}")
    print(f"Sequence for {n} = {sequence.list}")

    for i in range(n):
        print(f"Sequence for {i + 1} = {sequence.get_sequence(i)}")


