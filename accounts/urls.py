from django.urls import include, path
from accounts.views import signup,  activate, UserUpdate

urlpatterns = [

    path('signup/', signup, name="signup"),
    path('userupdate/', UserUpdate.as_view(), name="UserUpdate"),
    
    path('activate/<uidb64>/<token>/', activate, name='activate'),  
]
