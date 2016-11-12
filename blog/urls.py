from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # (?P<pk>\d+) this part is trickier. It means that Django will take
    # everything that you place here and transfer it to a view as a variable
    # called pk. \d also tells us that it can only be a digit, not a letter (so
    # everything between 0 and 9). + means that there needs to be one or more
    # digits there.
    # pk is an abbreviation for primary key. This name is often used in Django
    # projects.
]
