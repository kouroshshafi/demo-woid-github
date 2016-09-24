# coding: utf-8

from unipath import Path
import sys
import os

PROJECT_DIR = Path(os.path.abspath(__file__)).parent.parent
sys.path.append(PROJECT_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'woid.settings')

import django
from django.utils import timezone
django.setup()


from twisted.internet import task
from twisted.internet import reactor

from woid.apps.services import crawlers


FIVE_MINUTES = 1 * 60
THIRTY_MINUTES = 1 * 60

#(crawlers.NyTimesCrawler(), THIRTY_MINUTES)
def main():
    service_crawlers = (
    	(crawlers.RedditCrawler(), THIRTY_MINUTES),
        (crawlers.MediumCrawler(), THIRTY_MINUTES),
        (crawlers.DiggCrawler(), THIRTY_MINUTES),
        (crawlers.TwitterCrawler(), THIRTY_MINUTES),
        (crawlers.HackerNewsCrawler(), THIRTY_MINUTES),
        (crawlers.GithubCrawler(), THIRTY_MINUTES)
        )

    for crawler in service_crawlers:
        task.LoopingCall(crawler[0].run).start(crawler[1])

    reactor.run()

if __name__ == '__main__':
    main()
