import math

class Pet:
    def __init__(self, name = "", kind = ""):
        self.name = name
        self.kind = kind
        self.toys = []
    
    def add_toy(self, toy_name):
        self.toys.append(toy_name)

    def __str__(self):
        output = "{} är en {} som ".format(self.name, self.kind)
        if len(self.toys) > 0:
            output += "har följande leksaker: {}".format(", ".join(self.toys))
        else: 
            output += "inte har några leksaker."
        return output

class Vector2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
    
    def get_length(self):
        return math.sqrt(math.pow(self._x, 2) + math.pow(self._y, 2))

    def add(self, v1):
        self._x += v1._x
        self._y += v1._y
    
    def add_to_new(self, v1):
        return Vector2D(self._x + v1._x, self._y + v1._y)
    
    def is_longer_than(self, v1):
        return self.get_length() > v1.get_length()
    
    def create_unit_vector(self):
        l = self.get_length()
        return Vector2D(self._x / l, self._y / l)
    
    def __str__(self):
        return "({}, {})".format(self._x, self._y)

if __name__ == "__main__":
    def test_pet():
        fido = Pet("Fido", "pinne")
        fido.add_toy("boll")
        print(fido)

        nemo = Pet("Nemo", "fisk")
        print(nemo)

        hund1 = Pet()
        hund1.name = "Pluto"
        hund1.kind = "hund"
        print(hund1)
        hund1.add_toy("boll")
        print(hund1)

        katt1 = Pet("Misse")
        katt1.kind = "katt"
        katt1.add_toy("fjäder")
        print(katt1)
        katt1.add_toy("fjäder")
        print(katt1)
        katt1.add_toy("tygråtta")
        print(katt1)
    # test_pet()

    def test_vector():
        v1 = Vector2D(5, 2)
        print(v1)
        v2 = Vector2D(3, 2)
        print("Is v1 longer than v2:", v1.is_longer_than(v2))
        v2.add(v1)
        print("Is v1 longer than v2:", v1.is_longer_than(v2))
        v3 = v1.add_to_new(v2)
        print(v1, v2, v3)
        e1 = v1.create_unit_vector()
        assert e1.get_length() == 1

    test_pet()
    # test_vector()
