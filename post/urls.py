from django.urls import path
from . import views

urlpatterns = [
    path("post/<str:post_suffix>/", views.viewpost, name="viewpost"),
    path("manage/", views.manage, name="manage"),
    path("manage/post/", views.post_manage, name="post_manage"),
    path("manage/post/config/", views.post_config, name="post_config"),
    path("manage/post/edit/", views.post_edit, name="post_edit"),
    path("manage/post/create/", views.post_create, name="post_create"),
    path("manage/category/", views.category_manage, name="category_manage"),
    path("manage/category/config/", views.category_config, name="category_config"),
    path("manage/image/", views.image_manage, name="image_manage"),
    path("manage/image/config/", views.image_config, name="image_config"),
    path("category/", views.category, name="category"),
    path("denied/", views.denied, name="denied")
]
