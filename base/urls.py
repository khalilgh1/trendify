from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.home, name="home"),
    path("categories/", views.categories, name="categories"),
    path("about/", views.about, name="about"),
    path("product/<str:pk>", views.product, name="product"),
    path("add-product/", views.add_product, name="add_product"),
    path("edit-product/<str:pk>", views.edit_product, name="edit_product"),
    path("delete-product/<str:pk>", views.delete_product, name="delete_product"),
    path("fast-render/", views.fast_render, name="fast_render"),
    
]
