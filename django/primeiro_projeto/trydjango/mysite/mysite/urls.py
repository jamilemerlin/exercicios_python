"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from pages.views import home_view, contact_view, about_view, social_view
from products.views import product_list_view, product_detail_view, product_create_view, product_edit_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('about/', about_view),
    path('social/', social_view),

    # Products - CRUD (Create, Retrieve, Update, Delete)
    path('products/', product_list_view),
    path('products/create/', product_create_view),
    path('products/<int:id>/', product_detail_view),
    path('products/<int:id>/edit', product_edit_view),

    # path('product/', product_detail_view),
    # path('create/', product_create_view),
    # path('edit/', product_edit_view),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
