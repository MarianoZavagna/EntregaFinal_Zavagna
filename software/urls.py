from django.urls import path

from software import views


app_name='software'
urlpatterns = [
    path('softwares', views.SoftwareListView.as_view(), name='software-list'),
    path('software/add/', views.SoftwareCreateView.as_view(), name='software-add'),
    path('software/<int:pk>/detail', views.SoftwareDetailView.as_view(), name='software-detail'),
    path('software/<int:pk>/update', views.SoftwareUpdateView.as_view(), name='software-update'),
    path('software/<int:pk>/delete', views.SoftwareDeleteView.as_view(), name='software-delete'),
]
