import urllib.request
from datetime import datetime
from Scripts.page import *


def indexOfNth(container, elem = " ", nth = 1):
    if nth == 0:
        return 0
    occ = 0
    for i, x in enumerate(container):
        if container[i:len(elem)+i] == elem:
            occ += 1
        if occ == nth:
            return i
    if occ < nth:
        return len(container)


def get_searches(s,l,o):
    results=[]
    sPage = urllib.request.urlopen("https://en.wikipedia.org/w/index.php?title=Special:Search&limit=" + str(l) + "&offset=" + str(o) + "&profile=default&search=" + s.replace(" ", "+")).read().decode()
    sstr = "<div class='mw-search-result-heading'><a href=\"/wiki/"
    sstr2 = "KB ("
    sstr3 = "<div class=\"mw-pvi-month\">"
    sstr4 = "<div class=\"mw-pvi-month\"><a href=\"#\">"
    for x in range(sPage.count(sstr)):
        sind = indexOfNth(sPage, sstr, x + 1)
        eind = indexOfNth(sPage[sind:], "</li>", 1)
        sind2 = indexOfNth(sPage, sstr2, x + 1)
        eind2 = indexOfNth(sPage[sind2:], " words)", 1)
        name = sPage[sind + len(sstr):sind + len(sstr) + indexOfNth(sPage[sind + len(sstr):], "\" title=\"")]
        words = sPage[sind2 + len(sstr2):sind2 + eind2].replace(",", "")
        month = str([datetime.now().month - 1, 12][datetime.now().month == 1])
        views = eval(urllib.request.urlopen("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/" + name + "/monthly/" + str(datetime.now().year - [0, 1][datetime.now().month == 1]) + ["0", ""][len(month) > 1] + month + "01/" + str(datetime.now().year) + ["0", ""][len(str(datetime.now().month)) > 1] + str(datetime.now().month) + "01").read().decode())["items"][0]["views"]
        results.append(Page(name, None, views, words))
    return results
