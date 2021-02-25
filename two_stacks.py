
class TwoStacks:

    def __init__(self, n):
        self.stack = [None]*n
        self.top1 = -1
        self.top2 = n

    def stack_overflow(self):
        return self.top2 - self.top1 <= 1

    def push1(self, element):
        if not self.stack_overflow():
            self.top1 += 1
            self.stack[self.top1] = element
        else:
            print('Stack Overflow')

    def push2(self, element):
        if not self.stack_overflow():
            self.top2 -= 1
            self.stack[self.top2] = element
        else:
            print('Stack Overflow')

    def pop1(self):
        if self.top1 > 0:
            res = self.stack[self.top1]
            self.top1 -= 1
            return res
        else:
            print('Stack Underflow')

    def pop2(self):
        if self.top2 < len(self.stack):
            res = self.stack[self.top2]
            self.top2 += 1
            return res
        else:
            print('Stack Underflow')


ts = TwoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)
print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is " + str(ts.pop2()))