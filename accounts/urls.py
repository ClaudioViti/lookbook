from django.urls import include, path
from accounts.views import signup,  activate, UserUpdate, confirm_mail_change

urlpatterns = [

    path('signup/', signup, name="signup"),
    path('userupdate/', UserUpdate.as_view(), name="UserUpdate"),
    path('userupdate/confirm/<token>/', confirm_mail_change, name="email_change"),
    
    path('activate/<uidb64>/<token>/', activate, name='activate'),  
]
