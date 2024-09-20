from django.contrib.sitemaps import Sitemap
from blog.models import Blog_Post,Portfolio
from django.urls import reverse

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return Blog_Post.objects.all()
    
    def location(self,obj):
        return reverse('post', args=[obj.new_blog_slug])

class PortfolioSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return Portfolio.objects.all()
    
    def location(self,obj):
        return reverse('portfolio_detail', args=[obj.new_portfolio_slug])


class ListingSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return ['blog','portfolio']

    def location(self, item):
        return reverse(item)

class StaticSitemap(Sitemap):
    changefreq = "yearly"

    def items(self):
        return ['home', 'about' ,'contacts' ]

    def location(self, item):
        return reverse(item)