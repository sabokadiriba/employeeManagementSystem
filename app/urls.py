from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("homepage",views.homepage,name="homepagedff"),
    path("password_reset",views.password_reset_request,name="password_reset"),
]