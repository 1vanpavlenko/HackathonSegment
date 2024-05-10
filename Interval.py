class SegmentSet:
    def __init__(self, segments=None):
        """
        Конструктор класу для створення об'єкта SegmentSet.

        :param segments: Список відрізків/інтервалів, які утворюють множину.
                         За замовчуванням - порожній список.
        """
        self.segments = segments if segments else []

    def __add__(self, other):
        """
        Перевантажений оператор "+" для об'єднання множин.

        :param other: Екземпляр класу SegmentSet, Segment або дійсне число.
        :return: Новий екземпляр класу SegmentSet, який представляє об'єднану множину.
        """
        if isinstance(other, SegmentSet):
            return SegmentSet(self.segments + other.segments)
        elif isinstance(other, Segment):
            return SegmentSet(self.segments + [other])
        elif isinstance(other, (int, float)):
            return self.union_with_single_number(other)

    def __sub__(self, other):
        """
        Перевантажений оператор "-" для різниці множин.

        :param other: Екземпляр класу SegmentSet, Segment або дійсне число.
        :return: Новий екземпляр класу SegmentSet, який представляє різницю множин.
        """
        if isinstance(other, SegmentSet):
            return self.difference_with_segment_set(other)
        elif isinstance(other, Segment):
            return self.difference_with_single_segment(other)
        elif isinstance(other, (int, float)):
            return self.difference_with_single_number(other)

    def __mul__(self, other):
        """
        Перевантажений оператор "*" для перетину множин.

        :param other: Екземпляр класу SegmentSet, Segment або дійсне число.
        :return: Новий екземпляр класу SegmentSet, який представляє перетин множин.
        """
        if isinstance(other, SegmentSet):
            return self.intersection_with_segment_set(other)
        elif isinstance(other, Segment):
            return self.intersection_with_single_segment(other)
        elif isinstance(other, (int, float)):
            return self.intersection_with_single_number(other)

    def __truediv__(self, other):
        """
        Перевантажений оператор "/" для симетричної різниці множин.

        :param other: Екземпляр класу SegmentSet, Segment або дійсне число.
        :return: Новий екземпляр класу SegmentSet, який представляє симетричну різницю множин.
        """
        if isinstance(other, SegmentSet):
            return self.symmetric_difference_with_segment_set(other)
        elif isinstance(other, Segment):
            return self.symmetric_difference_with_single_segment(other)
        elif isinstance(other, (int, float)):
            return self.symmetric_difference_with_single_number(other)
