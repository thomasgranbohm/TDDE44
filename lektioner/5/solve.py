# Övning 1
class Contact(object):

    def __init__(self, name):
        self.name = name
        self.phone_num = ""

    
    def append_to_name(self, string_to_append):
        self.name += string_to_append

    def __str__(self):
        return "{}, {}".format(self.name, self.phone_num)

c1 = Contact("c1")
c2 = Contact("c2")

# Övning 2
c1.phone_num = "0701-111111"
c2.phone_num = "0702-222222"

print(c1.name, c1.phone_num)
print(c2.name, c2.phone_num)

# Övning 3
c1.append_to_name(", Efternamn")
c2.append_to_name(", Efternamn")

print(c1.name)
print(c2.name)

# Övning 4
contact_list = [c1, c2, Contact("c3")]
for c in contact_list:
    print(c)

