from django.urls import path
from .views import home, profile, RegisterView,qr_gen,signup

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('signup/', signup, name='users-signup'),

    path('profile/', RegisterView.as_view(), name='users-profile'),
    path('index/', qr_gen, name='index'),
]
