class Bot:
    def __init__(self, name):
        self.name = name
    def hi(self):
        print('Hello {self.name}')
    
obj = Bot('Taki')
obj.hi()
