class LikeString:
    def __init__(self, internalStr=""):
        self.iStr = internalStr

    def __eq__(self, other):
        return other.lower() in self.iStr.lower()

    def __str__(self):
        return self.iStr

    def __repr__(self):
        return "ls'" + self.iStr + "'"


class LikeDict:
    def __init__(self):
        self.__keys = []
        self.__values = []

    def keys(self):
        return self.__keys

    def values(self):
        return self.__values

    def items(self):
        return [[self.__keys[x], self.__values[x]] for x in range(len(self.__keys))]

    def __getitem__(self, key):
        for x, elem in enumerate(self.__keys):
            if key == elem:
                return self.__values[x]
        raise KeyError(key)

    def __setitem__(self, key, value):
        for x, elem in enumerate(self.__keys):
            if key == elem:
                self.__values[x] = value
                return
        key = LikeString(key)
        self.__keys.append(key)
        self.__values.append(value)

    def __str__(self):
        if len(self.__keys):
            ans = "ld{ "
            for x, elem in enumerate(self.__keys):
                ans += repr(elem) + " : " + repr(self.__values[x]) + (", " if x != len(self.__keys) - 1 else "")
            return ans + " }"
        return "{}"
    __repr__ = __str__