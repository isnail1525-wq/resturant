from django.urls import path
from . import views

app_name = "customers"

urlpatterns = [
    path("", views.customer_list, name="customer-list"),
    path("add/", views.customer_add, name="customer-add"),
    path("<int:pk>/", views.customer_detail, name="customer-detail"),
    path("<int:pk>/edit/", views.customer_edit, name="customer-edit"),
    path("<int:pk>/delete/", views.customer_delete, name="customer-delete"),
]
