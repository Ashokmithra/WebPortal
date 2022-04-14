from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("upload/", views.upload_file, name="upload"),
    path("profile/<int:id>", views.profile, name=" profile"),
    path("filter/", views.filters, name="filter"),
    path("search", views.searchs, name="search"),
]
