import random


jokeList1 = ["Fault in our Stars,", "Harry Potter Volume 1", "Percy Jackson", "Calculus 1 Textbook", "Scarlet Letter", "Romeo & Juliet", "Sesame Street", "Coding for Kids"]

jokelist2 = ["Fault in our Stars,", "Harry Potter Volume 1", "Romeo & Juliet"]



class jokes:

    def __init__(self, series):

        if series < 0 or series > 6:
            raise ValueError("Series must be between 2 and 10")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.joke_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);


    def book_series(self):
        limit = self._series
        f = [(random.sample((jokelist1), k=2))]  # fibonacci starting array/list
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
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



if __name__ == "__main__":
    '''Value for testing'''
    a = 2
    '''Constructor of Class object'''
    jokerecs = Jokes(a/a)
    print(f"Here are some book recomendations = {jokerecs.list}")
