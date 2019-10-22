import json
import requests
import praw

def examineLink(lin):
    #returns bias of url
    if "breitbart.com" in lin or "spectator.org" in lin or "theblaze.com" in lin \
    or "cbn.com" in lin or "dailycaller.com" in lin or "dailymail.co.uk" in lin \
    or "dailywire.com" in lin or "thefederalist.com" in lin or "nationalreview.com" in lin \
    or "nypost.com" in lin or "newsmax.com" in lin:
        print('RR')

    if "reason.com" in lin or "wsj.com/news/opinion" in lin or "washingtonexaminer.com" in lin \
    or "washingtontimes.com" in lin or "foxnews.com" in lin:
        print('R')

    if "alternet.org" in lin or "cnn.com/opinions" in lin or "democracynow.org" in lin \
    or "thedailybeast.com" in lin or "huffingtonpost.com" in lin or "theintercept.com" in lin \
    or "jacobinmag.com" in lin or "motherjones.com" in lin or "msnbc.com" in lin or "newyorker.com" in lin \
    or "thenation.com" in lin or "slate.com" in lin or "vox.com" in lin:
        print('LL')

    if "abcnews.go.com" in lin or "theatlantic.com" in lin or "buzzfeednews.com" in lin \
    or "cbs.com" in lin or "economist.com" in lin or "theguardian.com" in lin \
    or "nbc.com" in lin or "politico.com" in lin or "time.com" in lin \
    or "www.washingtonpost.com" in lin:
        print('L')

    if "ap.org" in lin or "bbc.com" in lin or "bloomberg.com" in lin or "csmonitor.com" in lin \
    or "npg.org" in lin or "reuters.com" in lin or "thehill.com" in lin or "usatoday.com" in lin:
        print('C')

reddit = praw.Reddit(client_id = 'oew7-0GWFaoDoQ',
                     client_secret = 'zWM2yRQc_v0Tk4bdq7xsEGmrmgg',
                     user_agent = 'asdf reddit apapap',
                     user_name = 'ffatty')

numPosts = 20

subNames = ['sandersforpresident','news','worldnews','politics']
linkLists = list()
for i in range(len(subNames)):
    linkLists.append(reddit.subreddit(subNames[i]).top(time_filter='year', limit=numPosts))



print('______________')

for l in range(len(subNames)):
    print(subNames[l])

    print('______________')
    for s in linkLists[l]:
        examineLink(s.url)    #gets bias
    print('______________')

#worldNewsTop = worldNews.top(time_filter="year", limit=20)

#for submissions in worldNewsTop:
    #print(submissions.url)


