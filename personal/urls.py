from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from work.sitemaps import WorkSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'work' : WorkSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('work/', include('work.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
    path('debug', include('debug_toolbar.urls')),
    path('captcha/', include('captcha.urls')),  
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)