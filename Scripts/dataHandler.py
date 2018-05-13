from Scripts.user import *
from Scripts.submission import *
from Scripts.infoFetch import *


class Handler:
    def __init__(self, user_file, submission_file, page_file, top_page_file):
        self.__uFile = user_file
        self.__sFile = submission_file
        self.__pFile = page_file
        self.__tpFile = top_page_file
        try:
            with open(top_page_file, "r") as f:
                for x in list(eval(f.read()).values()):
                    pages[x["name"]] = Page(x["name"], x["translated"], x["views"])
        except FileNotFoundError:
            updatePages()
        self.__top_pages = pages

    @property
    def file(self):
        return self.__uFile

    @property
    def submission_file(self):
        return self.__sFile

    @property
    def top_pages(self):
        return self.__top_pages

    def update_top_pages(self):
        #return self.__top_pages
        try:
            with open(self.__tpFile, "r") as f:
                for x in list(eval(f.read()).values()):
                    pages[x["name"]] = Page(x["name"], x["translated"], x["views"])
        except FileNotFoundError:
            updatePages()
        self.__top_pages = pages
        return self.__top_pages

    def set_top_pages(self, tPages):
        self.__top_pages = tPages

    def evaluated_users(self):
        filetext = "{'users': []}"
        try:
            with open(self.__uFile, "r") as f:
                filetext = decrypt(f.read())
        except FileNotFoundError:
            pass
        dic = eval(filetext)
        for x, elem in enumerate(dic["users"]):
            dic["users"][x] = User(*list(elem.values()), True)
        return dic

    def evaluated_pages(self):
        page_dic = {"pages": []}
        try:
            with open(self.__pFile, "r") as f:
                page_dic = eval(f.read())
        except FileNotFoundError: pass
        return page_dic

    def evaluated_submissions(self):
        submissions = {"max_id": 0, "submissions": []}
        try:
            with open(self.__sFile, "r") as f:
                submissions = eval(f.read())
        except FileNotFoundError: pass
        return submissions

    def add_user(self, user):
        if self.get_user(user.name) is None:
            dic = self.evaluated_users()
            dic["users"].append(user)
            with open(self.__uFile, "w") as f:
                f.write(encrypt(str(dic)))
            return True
        return False

    def edit_user(self, name, user):
        dic = self.evaluated_users()
        for x, elem in enumerate(dic["users"]):
            if elem.name == name:
                dic["users"][x] = user
        with open(self.__uFile, "w") as f:
            f.write(encrypt(str(dic)))

    def get_user(self, name):
        for x in self.evaluated_users()["users"]:
            if x.name == name:
                return x
        return None

    def remove_user(self, name):
        dic = self.evaluated_users()
        for x, elem in enumerate(dic["users"]):
            if elem.name == name:
                del dic["users"][x]
        with open(self.__uFile, "w") as f:
            f.write(encrypt(str(dic)))

    def add_page(self, page):
        for x in list(self.__top_pages.values()):
            if x.name == page.name:
                return None
        dic = self.evaluated_pages()
        for x in dic["pages"]:
            if x["name"] == page.name:
                return None
        dic["pages"].append(page)
        with open(self.__pFile, "w") as f:
            f.write(str(dic))

    def get_page(self, name):
        try:
            return self.__top_pages[name]
        except KeyError: pass
        dic = self.evaluated_pages()
        for x in dic["pages"]:
            if x["name"] == name:
                return Page(*list(x.values()))
        return None

    def edit_page(self, name, page):
        try:
            self.__top_pages[name]
            self.__top_pages[name] = Page(
                name,
                self.__top_pages[name].translated,
                self.__top_pages[name].views,
                self.__top_pages[name].length if self.__top_pages[name].length is not None else page.length,
                page.translations
            )
            with open(self.__tpFile, "w") as f:
                f.write(str(self.__top_pages))
            self.update_top_pages()
        except KeyError: pass

        dic = self.evaluated_pages()
        for x, elem in enumerate(dic["pages"]):
            if elem["name"] == name:
                dic["pages"][x] = page
        with open(self.__pFile, "w") as f:
            f.write(str(dic))

    def add_submission(self, name, submission):
        submissions = self.evaluated_submissions()
        submission.set_id(submissions["max_id"])
        submissions["max_id"]+=1
        submissions["submissions"].append(submission.ugly())
        user = self.get_user(name)
        user.add_submission(submission.id)
        self.edit_user(name, user)
        page = self.get_page(submission.page.name)
        page.add_translation(submission.id)
        self.edit_page(page.name, page)
        with open(self.__sFile, "w") as f:
            f.write(str(submissions))

    def get_submission(self, ID):
        try:
            submissions = self.evaluated_submissions()
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
