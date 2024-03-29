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
            all_val = self.__segment + other.__segment
            all_val.sort()

            all_val = all_val[1:len(all_val) - 1]

            if all_val[0] not in self or all_val[1] not in self:
                return None

            return Segment(*all_val)

    def __add__(self, other):
        assert type(other) is Segment

        if other.__segment[0] not in self and self.__segment[0] not in other:
            return None

        max_val = max(*other.__segment, *self.__segment)
        min_val = min(*other.__segment, *self.__segment)

        return min_val, max_val

    def __contains__(self, item):
        assert type(item) is int or type(item) is float

        return self.__segment[0] <= item <= self.__segment[1]

