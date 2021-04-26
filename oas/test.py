class A:
    def foo(self):
        pass


class B(A):
    def foo(self):
        pass

    def bar(self):
        print('b')
        return self.foo()


class C(A):
    def foo(self):
        pass

    def bar(self):
        print('c')
        return self.foo()


class D(B, C):
    def foo(self):
        pass

D().bar()

