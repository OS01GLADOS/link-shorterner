from django.urls import path

from short_link_worker import views

urlpatterns = [
    path('<identifier>', views.resolve_link, name='resolve-link'),
    path('generate/', views.generate_link, name='generate-link')
]
