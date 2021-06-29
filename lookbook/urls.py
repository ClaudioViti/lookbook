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
from shoes.views import ShoeListView, CartUpdateView, FavouriteUpdateView, OrderedUpdateView, minicartView, favouriteView, create_shoe, edit_shoe, ShoeDeleteView, image_view, order_list, UrgentUpdateView, BrandCreate, BrandUpdate, BrandDelete, BrandManage, ShoeListManage, ordersView, terminate_order
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt, csrf_protect


urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', ShoeListView.as_view()),
    path('minicart/', minicartView.as_view(), name='minicart'),
    path('favourite/', favouriteView.as_view(), name='favourites'),
    path('orders/', ordersView.as_view(), name='orders'),
    path('minicart/sendmail/', order_list, name="order_list"),
    path('shoes/<int:pk>/cart/', csrf_exempt(CartUpdateView.as_view()), name='shoe-cart'),
    path('shoes/<int:pk>/favourite/', csrf_exempt(FavouriteUpdateView.as_view()), name='shoe-favourite'),
    path('shoes/<int:pk>/urgent/', csrf_exempt(UrgentUpdateView.as_view()), name='shoe-urgent'),
    path('shoes/<int:pk>/ordered/', csrf_exempt(OrderedUpdateView.as_view()), name='shoe-ordered'),
    path('shoes/<int:pk>/images/', image_view, name='shoe-image'),
    path('brand/', BrandManage.as_view(), name='brand'),
    path('brand/add/', BrandCreate.as_view(), name='brand-add'),
    path('brand/<int:pk>/', BrandUpdate.as_view(), name='brand-update'),
    path('brand/<int:pk>/delete/', BrandDelete.as_view(), name='brand-delete'),
    path('admin/', admin.site.urls),
    path('manage/', ShoeListManage.as_view(), name='manage'),
    path('manage/add/', create_shoe, name='add'),
    path('manage/<int:pk>/', edit_shoe, name='edit'),
    path('manage/<int:pk>/delete/', ShoeDeleteView.as_view(), name='delete'),
    path('minicart/sendmailterminate/', terminate_order, name="terminate_order"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
