class Submission:
    def __init__(self, text, page, user, ID=None):
        self.__text = text
        self.__page = page
        self.__user = user
        self.__id = ID

    @property
    def text(self):
        return self.__text

    @property
    def page(self):
        return self.__page

    @property
    def user(self):
        return self.__user

    @property
    def id(self):
        return self.__id

    def pretty(self):
        return "<Submission>(Translator: " + self.__user.pretty() + ", Page: " + self.__page + ")"

    def ugly(self):
        return {"id": self.__id, "text": self.__text, "page": self.__page, "user": self.__user.name}

    def set_id(self, new_id):
        self.__id = new_id

    def __str__(self):
        return str(self.__id)

    __repr__ = __str__
