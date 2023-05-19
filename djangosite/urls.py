from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_emp/', views.add_emp, name="add_emp"),
    path("login_view/", views.login_view, name="login_view"),
    path('signup/', views.signup, name="signup"),
    path('search/', views.search, name="search"),
    path('emp_update/<slug>/',  views.emp_update, name="emp_update"),
    path('logout_view/', views.logout_view, name="logout_view"),
    path('verify/<token>', views.verify, name="verify"),
]
