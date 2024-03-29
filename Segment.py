class Segment:
    def __init__(self, a, b):
        assert type(a) is int or type(a) is float
        assert type(b) is int or type(b) is float

        segment = [a, b]
        segment.sort()

        self.__segment = segment

    def __str__(self):
        return f"{self.__segment}"

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Segment(self.__segment[0] * other, self.__segment[1] * other)

        elif type(other) is Segment:
            pass

    def __add__(self, other):
        assert type(other) is Segment

        if other.__segment[0] not in self:
            return None

        max_val = max(*other.__segment, *self.__segment)
        min_val = min(*other.__segment, *self.__segment)

        return Segment(max_val, min_val)

    def __contains__(self, item):
        assert type(item) is int or type(item) is float

        return self.__segment[0] <= item <= self.__segment[1]

