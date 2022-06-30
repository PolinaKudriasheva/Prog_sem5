class FibonachiList:

    def __iter__(self): # при создании итератора для объекта
        self.lst = [0, 1] # в список добавляется два элемента 0 и 1
        return self

    def __next__(self): # при вызове метода next объекта
        self.lst.append(self.lst[-1] + self.lst[-2]) # в список добавляется элемент
        return self.lst # который равен сумме двух последних
