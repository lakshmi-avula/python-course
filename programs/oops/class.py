class Computer:
    def config(self):
        print("i5 16gb 1Tb")



com1 = Computer()
com2 = Computer()
Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()