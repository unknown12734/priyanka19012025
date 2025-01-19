class MyAddition:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f"the value are {self.a}, {self.b}")

    def my_addition_func(self):
        return self.a + self.b
    
    def myadd_new(self):
        sum = self.my_addition_func()
        return sum + 10