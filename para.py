class Addition:
    first = 0
    second = 0
    answer = 0


    def __init__(self, first, second):
        self.first = first
        self.second = second

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def cal(self):
        self.answer = self.first + self.second

obj1 = Addition(10, 20)
obj2 = Addition(100, 200)


obj1.cal()
obj2.cal()

obj1.display()
obj2.display()
