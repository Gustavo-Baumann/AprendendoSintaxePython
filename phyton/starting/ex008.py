class numeros:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a < 1000:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

classe = numeros()
iterador =  iter(classe)

while 10 > 5:
    print(next(iterador))