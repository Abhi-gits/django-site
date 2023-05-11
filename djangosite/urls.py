from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add_emp', views.add_emp),
    path("login_view/", views.login_view, name="login"),
    path('signup', views.signup),
    path('search_emp', views.search_emp),
    path('logout_view/', views.logout_view),
    path('verify/<token>', views.verify, name="verify"),
]
