from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(template_name='short_link_user/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='short_link_user/logout.html'),
         name='logout'),
    path('shorted-links/', include('short_link_user.urls')),
    path('admin/', admin.site.urls),
    path('', include('short_link_worker.urls'))
]
