from django.urls import include, path
from accounts.views import signup,  activate

urlpatterns = [

    path('signup/', signup, name="signup"),
    
    path('activate/<uidb64>/<token>/', activate, name='activate'),  
]
