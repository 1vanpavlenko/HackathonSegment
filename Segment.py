class Segment:
    def __init__(self, a, b, in_a=True, in_b=True):
        assert type(a) is int or type(a) is float
        assert type(b) is int or type(b) is float
        assert a <= b

        segment = [a, b]
        segment.sort()

        self.__segment = segment
        self.__in_a = in_a
        self.__in_b = in_b

    def __str__(self):
        return f"{self.__segment}"

    # def

r = Segment(4, 4.0, )