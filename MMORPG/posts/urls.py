from allauth.account.views import LoginView
from django.urls import path
from .views import PostsList, PostDetail, ProfileView

urlpatterns = [
    path('', PostsList.as_view(), name='posts'),
    # path('add_post/', AddPostView.as_view(), name='add_post'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
