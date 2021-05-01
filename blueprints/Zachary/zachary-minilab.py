import random

jokeList1 = []

jokelist2 = []

class jokes:

    def __init__(self, jokes):

        if series < 0 or jokes > 10:
            raise ValueError("Series must be between 0 and 10")
        self._jokes = jokes
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.joke_series()


    def joke_series(self):
        limit = self._series
        f = [(random.sample((jokelist1), k=3))]  # fibonacci starting array/list
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
            limit -= 1
    def getjoke(selfself):
        return random.choice(jokeList1)

    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1
    # Getters
    @property
    def series(self):
        return self._jokes

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    def get_sequence(self, nth):
        return self._dict[nth]


if request.method == 'POST':
    a = int(request.form.get("series"))
    ranjokes = Jokes(a/a)

return render_template("randomjokegenerator.html", ranjokes=Jokes(a))


if __name__ == "__main__":
    '''Value for testing'''
    a = 6
    '''Constructor of Class object'''
    ranjokes = Jokes(a/a)
