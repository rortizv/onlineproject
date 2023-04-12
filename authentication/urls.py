from django.urls import path
from .views import VRegister, logout, login


urlpatterns = [
    path('', VRegister.as_view(), name='Register'),
    path('logout', logout_session, name='logout'),
    path('login', login_session, name='login'),
]