class MyRange:
    def __init__(self, start, end, steps=1):

        self.start = start
        self.end = end
        self.steps = steps
        self.current = self.start - self.steps

    def __iter__(self):
        return(self)

    def __next__(self):

        self.current += self.steps

        if self.current >= self.end:
            raise StopIteration

        return(self.current)


for i in MyRange(2, 12):
    print(i)

print('----------')

for i in MyRange(2, 12, 3):
    print(i)