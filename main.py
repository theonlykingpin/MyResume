
class Fibonacci:
    def __init__(self):
        self.cache = {}

    def calculate(self, n):
        if n in self.cache:
            return self.cache[n]
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            result = self.calculate(n-1) + self.calculate(n-2)
            self.cache[n] = result
            return result

fib = Fibonacci()
print(fib.calculate(1000))
