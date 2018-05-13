from Scripts.user import *
from Scripts.submission import *
from Scripts.page import *

class Handler:
    def __init__(self, file, submission_file=None):
        self.__file = file
        self.__sFile = submission_file

    @property
    def file(self):
        return self.__file

    @property
    def submission_file(self):
        return self.__sFile

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

    def add_submission(self, name, submission):
        submissions = {"max_id": 0, "submissions": []}
        try:
            with open(self.__sFile, "r") as f:
                submissions = eval(f.read())
        except FileNotFoundError: pass
        submission.set_id(submissions["max_id"])
        submissions["max_id"]+=1
        submissions["submissions"].append(submission.ugly())
        user = self.get_user(name)
        user.add_submission(submission.id)
        self.edit_user(name, user)
        with open(self.__sFile, "w") as f:
            f.write(str(submissions))

    def get_submission(self, ID):
        try:
            submissions=None
            with open(self.__sFile, "r") as f:
                submissions = eval(f.read())
            for x in submissions["submissions"]:
                if x["id"] == ID:
                    return Submission(
                        x["text"],
                        Page(
                            x["page"]["name"],
                            x["page"]["translated"],
                            x["page"]["views"],
                            x["page"]["length"]
                        ),
                        self.get_user(x["user"]),
                        x["id"]
                    )
        except FileNotFoundError:
            return None
