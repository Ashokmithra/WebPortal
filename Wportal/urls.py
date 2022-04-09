from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("upload/", views.upload_file, name="upload"),
    path("profile/<int:id>", views.profile, name=" profile"),
    # path("allnotes", views.allnotes, name="allnotes"),
    # path("user/<int:id>", views.user, name=" user"),
    path("upload/", views.upload, name="upload"),
    path("filter/", views.filters, name="filter"),
    path("search", views.searchs, name="search")
]
