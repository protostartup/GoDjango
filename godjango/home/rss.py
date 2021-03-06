from django.contrib.syndication.views import Feed
from datetime import datetime
from home.models import *
from email import utils
import time


class LatestVideos(Feed):
        title = "GoDjango Screencasts"
        link = "http://godjango.com"
        description = "Weekly screencast covering some topic about Django."

        def items(self):
            return Video.objects.filter(publish_date__lte=datetime.now()).order_by('-publish_date')[:10]

        def item_title(self, item):
            return item.title

        def item_description(self, item):
            return item.description + ("<br /><a href='http://godjango.com/%s-%s'>Watch Now...</a>" % (item.id, item.slug))

        def item_link(self, item):
            return "http://godjango.com/%s-%s/" % (item.id, item.slug)

        def item_pubdate(self, item):
            return item.publish_date
