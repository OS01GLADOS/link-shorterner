from django.urls import path

from short_link_user import views
from short_link_user.views import UserShortLinkListView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('my-shorted-links/', UserShortLinkListView.as_view(), name='user_shorted_links')
]
