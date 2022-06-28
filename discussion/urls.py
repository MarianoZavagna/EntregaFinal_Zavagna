from django.urls import path
from discussion import views


app_name='discussion'
urlpatterns = [
    path('discussions', views.DiscussionListView.as_view(), name='discussion-list'),
    path('discussion/add/', views.DiscussionCreateView.as_view(), name='discussion-add'),
    path('discussion/<int:pk>/detail', views.DiscussionDetailView.as_view(), name='discussion-detail'),
    path('discussion/<int:pk>/update', views.DiscussionUpdateView.as_view(), name='discussion-update'),
    path('discussion/<int:pk>/delete', views.DiscussionDeleteView.as_view(), name='discussion-delete'),
    path('/discussion/<int:pk>/comment', views.CommentCreateView.as_view(), name='comment-add'),

]
