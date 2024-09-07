class Multiply3:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        if isinstance(other, Multiply3):
            return self.x * other.x * 3

    def __str__(self):
        return str(self.x)

    def __repr__(self):
        return str(self.x)


m1 = Multiply3(10)
m2 = Multiply3(3)
m3 = Multiply3(4)

print(m1 * m3)  # 18
print(m1)  # 2
print(m2)  # 3
print(2 * 3)
