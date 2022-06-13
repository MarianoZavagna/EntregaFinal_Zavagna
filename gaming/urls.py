from django.urls import path

from gaming import views


app_name='gaming'
urlpatterns = [
    path('gamings', views.GamingListView.as_view(), name='gaming-list'),
    path('gaming/add/', views.GamingCreateView.as_view(), name='gaming-add'),
    path('gaming/<int:pk>/detail', views.GamingDetailView.as_view(), name='gaming-detail'),
    path('gaming/<int:pk>/update', views.GamingUpdateView.as_view(), name='gaming-update'),
    path('gaming/<int:pk>/delete', views.GamingDeleteView.as_view(), name='gaming-delete'),
]
