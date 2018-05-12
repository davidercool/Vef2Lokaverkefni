from Scripts.cryption import *


class User:
    def __init__(self, name, mail, passw, submissions=[], created=False):
        self.__name = name
        self.__mail = mail
        self.__passw = encrypt(passw) if not created else passw
        self.__submissions = submissions

    @property
    def name(self):
        return self.__name

    @property
    def mail(self):
        return self.__mail

    @property
    def passw(self):
        return self.__passw

    @property
    def submissions(self):
        return self.__submissions

    def add_submission(self, submission):
        self.__submissions.append(submission)



    def __str__(self):
        return "{'name':'" + self.__name + "', 'mail': '" + self.__mail + "', 'passw': '" + self.__passw + "', 'submissions': " + str(self.__submissions) + "}"

    __repr__ = __str__
