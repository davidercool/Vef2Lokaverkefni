class Submission:
    def __init__(self, text, page, user):
        self.__text = text
        self.__page = page
        self.__user = user

    @property
    def text(self):
        return self.__text

    @property
    def page(self):
        return self.__page

    @property
    def user(self):
        return self.__user

    def __str__(self):
        return "<Submission>(Translator: " + self.__user.pretty() + ", Page: " + self.__page + ")"
