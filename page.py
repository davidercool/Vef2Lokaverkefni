pages={}


class Page:
    def __init__(self, name, translated, views):
        self.__name = name
        self.__translated = translated
        self.__views = views

    @property
    def name(self):
        return self.name

    @property
    def translated(self):
        return self.__translated

    @property
    def views(self):
        return self.__views

    @property
    def bounty(self):
        return self.__views // 1000

    def pretty(self):
        return "<Page>(" + self.__name + ")"

    def __str__(self):
        return "{\"name\": \"" + self.__name + "\", \"translated\": " + str(self.__translated) + ", \"views\": " + str(self.__views) + "}"

    __repr__ = __str__
