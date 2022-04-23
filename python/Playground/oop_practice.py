class someRandomClass:

    def __init__(self, idkParameter):
        self.idk = idkParameter

    def displayIdk(self):
        print(self.idk)

    def nestedClass(self):
        class InnerClass:

            def __init__(self, number):
                self.number = number

            def square(self):
                return self.number**2

        ic = InnerClass(3)
        print(ic.square())


someObject1 = someRandomClass("BABABOII")

someObject1.displayIdk()
someObject1.nestedClass()
