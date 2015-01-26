class IntArray(object):
    """A fast multiplication algorithm implementation.

    The Karatsuba algorithm allows us to compute the product of two large
    numbers x and y using three multiplications of smaller numbers, each with
    about half as many digits as x or y, plus some additions and digit shifts.

    Attributes:
        array: An array representation of a large integer.
        base: A radix or base.
    """
    def __init__(self, array=None, base=10):
        self.array = array if array else []
        self.base = base

    def __mul__(self, x):
        while len(x.array) > len(self.array):
            self.array.insert(0, 0)
        while len(self.array) > len(x.array):
            x.array.insert(0, 0)
        return self.__karatsuba(x, self)

    def __karatsuba(self, x, y):
        m = len(x.array) - 1
        x_1 = IntArray([x.array.pop(0)], self.base)
        y_1 = IntArray([y.array.pop(0)], self.base)
        r = x_1.array[0] * y_1.array[0]
        z_2 = IntArray([r % self.base], self.base)
        carry = int(r / self.base)
        if carry: z_2.array.insert(0, carry)
        if m == 0:
            return z_2
        else:
            x_sum = x + x_1
            y_sum = y + y_1
            z_0 = x * y
            z_1 = x_sum * y_sum
            z_1 = z_1 - z_2
            z_1 = z_1 - z_0
            for i in range(2 * m):
                z_2.array.append(0)
            for i in range(m):
                z_1.array.append(0)
            print 'z_2*B^2m: {0} + z_1*B^m: {1} + z_0: {2}'.format(z_2.array, z_1.array, z_0.array)
            return z_2 + z_1 + z_0

    def __add__(self, x):
        while len(x.array) > len(self.array):
            self.array.insert(0, 0)
        while len(self.array) > len(x.array):
            x.array.insert(0, 0)
        carry = 0
        result = IntArray([], self.base)
        for i in range(len(x.array) - 1, -1, -1):
            r = x.array[i] + self.array[i] + carry
            result.array.insert(0, r % self.base)
            carry = int(r / self.base)
        if carry: result.array.insert(0, carry)
        if len(result.array) > 1 and not r: result.array.pop(0)
        print '{0} + {1} = {2}'.format(self.array, x.array, result.array)
        return result

    def __sub__(self, x):
        while len(x.array) > len(self.array):
            self.array.insert(0, 0)
        while len(self.array) > len(x.array):
            x.array.insert(0, 0)
        if abs(self.array[0]) >= abs(x.array[0]):
            result = self +(-x)
        else:
            result = -(-self + x)
        print '{0} - {1} = {2}'.format(self.array, x.array, result.array)
        return result

    def __neg__(self):
        result = IntArray([], self.base)
        for i in range(len(self.array)):
            result.array.append(-self.array[i])
        return result
