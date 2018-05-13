pages={}


class Page:
    def __init__(self, name, translated, views, length=None, translations=[]):
        self.__name = name
        self.__translated = translated
        self.__views = views
        self.__length = length
        self.__translations = translations

    @property
    def name(self):
        return self.__name

    @property
    def prettyName(self):
        return self.__name.replace("_", " ")

    @property
    def translated(self):
        return self.__translated

    @property
    def views(self):
        return self.__views

    @property
    def bounty(self):
        return self.__views // 10000

    @property
    def length(self):
        return self.__length

    @property
    def translations(self):
        return self.__translations

    def add_translation(self, submission):
        self.__translations.append(submission)
        self.__translated = True

    def pretty(self):
        return "<Page>(" + self.__name + ")"

    def __str__(self):
        return "{\"name\": \"" + self.__name + "\", \"translated\": " + str(self.__translated) + ", \"views\": " + str(self.__views) + ", \"length\": " + str(self.__length) + ", \"translations\": " + str(self.__translations) + "}"

    __repr__ = __str__
