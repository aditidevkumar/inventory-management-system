from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    #landing page
    path('', views.custom_login, name='login'),
    path('', views.product_list, name='product_list'),    
    path('new/', views.product_create, name='product_create'),
    path('<int:pk>/edit/', views.product_update, name='product_update'),
    path("category-stock/", views.category_stock, name="category_stock"),
    path('products/decrease-stock/<int:pk>/', views.decrease_stock, name='decrease_stock'),
    
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),    
    path('dashboard/', views.dashboard, name='dashboard'),
 
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    path('', LoginView.as_view(template_name='inventory/login.html'), name='login'),  
    path('products/', views.product_list, name='product_list'),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

