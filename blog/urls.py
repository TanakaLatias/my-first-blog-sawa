from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/edit/<int:pk>', views.post_edit, name='post_edit'),
]

"""
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostEditView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/edit/<int:pk>', PostEditView.as_view(), name='post_edit'),
]
"""