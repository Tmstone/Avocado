from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('new', views.new, name="new"),
    path("create", views.create, name="create"),
    path('<int:blog_number>', views.show, name="show"),
    path('<int:blog_number>/edit', views.edit, name="edit"),
    path('<int:blog_number>/delete', views.destroy, name="destroy"),
]
