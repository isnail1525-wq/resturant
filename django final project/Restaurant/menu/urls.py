from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("", views.item_list, name="item-list"),
    path("add/", views.item_add, name="item-add"),
    path("<int:pk>/", views.item_detail, name="item-detail"),
    path("<int:pk>/edit/", views.item_edit, name="item-edit"),
    path("<int:pk>/delete/", views.item_delete, name="item-delete"),
]
