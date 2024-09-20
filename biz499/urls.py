from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from blog.views import index,blog,post,search,about,portfolio,portfolio_detail
from marketing.views import contacts,ordersuccess,paybutton,privacypolicy,termsandconditions,cancellationpolicy,developmentservice,adsservice,designservice
from django.conf.urls import include
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import BlogSitemap, StaticSitemap,PortfolioSitemap,ListingSitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'post': BlogSitemap,
    'static': StaticSitemap,
    'portfolio_detail': PortfolioSitemap,
    'listing' : ListingSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='home'),
    path('blog/',blog,name='blog'),
    path('post/<slug>/',post,name='post' ),
    path('search/',search,name='search' ),
    path('about/',about,name='about' ),
    # path('blog_detail/',blog_detail,name='portfolio'),
    path('portfolio/',portfolio,name='portfolio'),
    # path('portfolio_detail_1/',portfolio_detail_1,name='portfolio'),
    path('portfolio_detail/<slug>/',portfolio_detail,name='portfolio_detail'),
    path('contacts/',contacts,name='contacts'),
    path('privacypolicy/',privacypolicy),
    path('termsandconditions/',termsandconditions),
    path('cancellationpolicy/',cancellationpolicy),
    path('development/',developmentservice),
    path('marketing/',adsservice),
    path('design/',designservice),
    path('tinymce/', include('tinymce.urls')),
    path("paybutton/", paybutton),
    path("ordersuccess/", ordersuccess),


    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
        path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
