from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name="welcome"),
    url(r'blog/',views.blog,name="allBlog"),
    url(r'^today/',views.newsOfTheDay,name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.pastDaysNews,name='pastNews'),
    url(r'^search/',views.search_results,name="search_results"),
    url(r'^article/(\d+)',views.article,name ='article'),
    url(r'^news/articles$',views.new_article,name='new-article')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
