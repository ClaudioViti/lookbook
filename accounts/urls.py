from django.urls import include, path
from accounts.views import signup

urlpatterns = [

    path('signup/', signup, name="signup")
]
