from django.contrib.sitemaps import Sitemap
from django.urls import reverse

# creating a sitemap for the site. contain home, privacy, and terms pages.
class HomeSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'privacy', 'terms', 'job_application']

    def location(self, item):
        return reverse(item)