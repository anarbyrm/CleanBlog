from django.urls import path
from .views import IndexPage, PostDetail, AboutPage, CreatePost, PostUpdate, PostDelete


urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('about/', AboutPage.as_view(), name='about'),
    path('post/create/', CreatePost.as_view(), name='create'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='update'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='delete')
]