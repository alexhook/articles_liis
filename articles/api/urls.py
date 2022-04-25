from django.urls import path
from . import views

urlpatterns = [
    path('article/create/', views.AuthorToolsViewSet.as_view({'post': 'create'}), name='create-article'),
    path('article/<int:pk>/update/', views.AuthorToolsViewSet.as_view({'put': 'update'}), name='update-article'),
    path('article/<int:pk>/destroy/', views.AuthorToolsViewSet.as_view({'delete': 'destroy'}), name='destroy-article'),

    path('article/list/', views.PublicArticleViewSet.as_view({'get': 'list'}), name='list-public-article'),
    path('article/<int:pk>/', views.PublicArticleViewSet.as_view({'get': 'retrieve'}), name='retrieve-public-article'),

    path('subscription/list/', views.PrivateArticleViewSet.as_view({'get': 'list'}), name='list-private-article'),
    path('subscription/<int:pk>/', views.PrivateArticleViewSet.as_view({'get': 'retrieve'}), name='retrieve-private-article'),
]