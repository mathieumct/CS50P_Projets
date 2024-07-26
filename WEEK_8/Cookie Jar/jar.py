class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
            self.number_in_jar = 0

    def __str__(self):
        result_cookie = "🍪" * self.number_in_jar
        return result_cookie

    def deposit(self, n):
        if self.number_in_jar + n > self.capacity:
            raise ValueError()
        else:
            self.number_in_jar += n

    def withdraw(self, n):
        if self.number_in_jar - n < 0:
            raise ValueError()
        else:
            self.number_in_jar -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.number_in_jar
