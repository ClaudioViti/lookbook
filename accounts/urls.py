from django.urls import include, path
from accounts.views import signup,  signup_sent_view

urlpatterns = [

    path('signup/', signup, name="signup"),
    path('signup_sent/', signup_sent_view, name="signup_sent")
]
