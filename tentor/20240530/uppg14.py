class PictureData:
    def __init__(self, _filename, _width, _height):
        self.filename = _filename
        self.width = _width
        self.height = _height

    def get_area(self):
        return self.width * self.height

    def copy(self):
        return PictureData(self.filename, self.width, self.height)


if __name__ == "__main__":
    a = PictureData("strand.jpg", 1600, 900)
    print(a.filename, a.width, a.height)
    print(a.get_area())

    b = a.copy()
    print(a, b)
