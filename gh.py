class Segment:
    def __init__(self, a, b, in_start=True, in_end=True):
        self.a = a
        self.b = b
        self.in_start = in_start
        self.in_end = in_end

    def is_empty(self):
        return self.a > self.b or (self.a == self.b and not self.in_start and not self.in_end)

    def __str__(self):
        if self.is_empty():
            return "Empty Segment"
        bracket_f = "[" if self.in_start else "("
        bracket_s = "]" if self.in_end else ")"
        return f"{bracket_f}{self.a}, {self.b}{bracket_s}"


segment1 = Segment(0, 10)
print(segment1)

segment2 = Segment(0, 15, in_start=False)
print(segment2)

segment3 = Segment(10, 5)
print(segment3.is_empty())
