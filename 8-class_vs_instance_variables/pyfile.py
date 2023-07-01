class Girl:

    #Class variable: every objects have the same.
    # Objects of the class defaultly have the same value
    gender = "Female"

    def __init__(self, name):
        #instance variable, unique.
        self.name = name



s = Girl("Susan")
r = Girl("Rachel")

print(s.gender)
print(r.gender)

print(s.name)
print(r.name)
