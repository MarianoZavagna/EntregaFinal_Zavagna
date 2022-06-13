from django.urls import path

from hardware import views


app_name='hardware'
urlpatterns = [
    path('hardwares', views.HardwareListView.as_view(), name='hardware-list'),
    path('hardware/add/', views.HardwareCreateView.as_view(), name='hardware-add'),
    path('hardware/<int:pk>/detail', views.HardwareDetailView.as_view(), name='hardware-detail'),
    path('hardware/<int:pk>/update', views.HardwareUpdateView.as_view(), name='hardware-update'),
    path('hardware/<int:pk>/delete', views.HardwareDeleteView.as_view(), name='hardware-delete'),
]
