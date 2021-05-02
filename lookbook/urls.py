"""lookbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from shoes.views import ShoeListView, FavouriteUpdateView, minicartView, CreateView, UpdateView, DeleteView
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt, csrf_protect

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', ShoeListView.as_view()),
    path('minicart/', minicartView.as_view()),
    path('shoes/<int:pk>/favourite/', csrf_exempt(FavouriteUpdateView.as_view()), name='shoe-favourite'),
    path('admin/', admin.site.urls),
    path('manage/add/', ShoeCreateView.as_view()),
    path('manage/<int:pk>/', ShoeUpdateView.as_view()),
    path('manage/<int:pk>/delete/', ShoeDeleteView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
