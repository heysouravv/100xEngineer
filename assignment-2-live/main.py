class FizzBuzz:
    def __init__(self, n):
        self.n = n
    
    def fizz_buzz(self):
        for num in range(1, self.n + 1):
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print(num)

if __name__ == "__main__":
    n = 100
    fb = FizzBuzz(n)
    fb.fizz_buzz()
