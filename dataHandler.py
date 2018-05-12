from cryption import *
from user import *

class Handler:
    def __init__(self, file):
        self.__file = file

    @property
    def file(self):
        return self.__file

    def evaluated(self):
        filetext = "{'users': []}"
        try:
            with open(self.__file, "r") as f:
                filetext = decrypt(f.read())
        except FileNotFoundError:
            pass
        dic = eval(filetext)
        for x, elem in enumerate(dic["users"]):
            dic["users"][x] = User(*list(elem.values()), True)
        return dic

    def add_user(self, user):
        if self.get_user(user.name) is None:
            dic = self.evaluated()
            dic["users"].append(user)
            with open(self.__file, "w") as f:
                f.write(encrypt(str(dic)))
            return True
        return False

    def edit_user(self, name, user):
        dic = self.evaluated()
        for x, elem in enumerate(dic["users"]):
            if elem.name == name:
                dic["users"][x] = user
        with open(self.__file, "w") as f:
            f.write(encrypt(str(dic)))

    def get_user(self, name):
        for x in self.evaluated()["users"]:
            if x.name == name:
                return x
        return None

    def remove_user(self, name):
        dic = self.evaluated()
        for x, elem in enumerate(dic["users"]):
            if elem.name == name:
                del dic["users"][x]
        with open(self.__file, "w") as f:
            f.write(encrypt(str(dic)))
