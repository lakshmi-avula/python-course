class Sampleclass:
    count = 0       #class attribute(variable)
    def increase(self):
        Sampleclass.count+=1



s1 = Sampleclass()
s1.increase()
print(s1.count)

s2 = Sampleclass()
s2.increase()
print(s2.count)