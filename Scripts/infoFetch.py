import urllib.request, os, json, threading
from Scripts.page import *

topSites=[]
threadLock = threading.Lock()
threads = []
finished = 0

def updatePages():
    def fetchLanguageDataLanglinks(elem):
        try:
            with urllib.request.urlopen("https://commons.wikimedia.org/w/api.php?action=query&titles=" + elem[0] + "&lllimit=500&rawcontinue&prop=langlinks&format=json") as url:
                results = json.loads(url.read().decode())
                try:
                    list(results["query"]["pages"].values())[0]["missing"]
                except KeyError:
                    try:
                        global pages
                        list(results["query"]["pages"].values())[0]["langlinks"]
                        iceland=False
                        for y in list(results["query"]["pages"].values())[0]["langlinks"]:
                            if y["lang"] == "is":
                                iceland=True
                                break
                        pages[elem[0]] = Page(elem[0], iceland, elem[1])
                    except KeyError: pass
        except UnicodeEncodeError: pass #print("Includes non ascii characters")


    def fetchLanguageDataScrape(elem):
        try:
            print("https://en.wikipedia.org/wiki/" + elem[0])
            with urllib.request.urlopen("https://en.wikipedia.org/wiki/" + elem[0]) as url:
                pages[elem[0]] = Page(elem[0], "interwiki-is" in url.read().decode(), elem[1])
        except UnicodeEncodeError: pass #print("Includes non ascii characters")


    class DataThread (threading.Thread):
        def __init__(self, elem):
            threading.Thread.__init__(self)
            self.elem = elem
            self.name = elem[0]


        def run(self):
            print("Starting " + self.name)
            threadLock.acquire()
            fetchLanguageDataScrape(self.elem)
            threadLock.release()
            global finished
            finished += 1
            print("finished " + self.name + (" " * (80 - len(self.name))) + str(finished) + "/" + str(len(threads)))
    for x in json.load(open(os.path.join(os.path.realpath(__file__), "..\\..\\UserData\\viewData.json"))):
        topSites.append([x["article"].replace(" ", "_"), int(x["views"])])

    for x in topSites:
        thread = DataThread(x)
        thread.start()
        threads.append(thread)

    for x in threads:
        x.join()

    with open(os.path.join(os.path.realpath(__file__), "..\\..\\UserData\\pages.json"), "w") as f:
        print(pages)
        f.write(str(pages))
