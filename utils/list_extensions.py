# Add methods to the list class
def first(self):
    if self:
        return self[0]
    raise IndexError("Cannot get the first element of an empty list.")


def last(self):
    if self:
        return self[-1]
    raise IndexError("Cannot get the last element of an empty list.")


# Monkey patch the methods
list.first = first
list.last = last
