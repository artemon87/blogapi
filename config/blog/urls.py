from django.urls import path
#from .views import PostList, PostDetail
from .views import BlogCreateView


#urlpatterns = [
    #path('<int:pk>/', PostDetail.as_view()),
    #path('', PostList.as_view()),
#]


urlpatterns = [
    path('', BlogCreateView.as_view(), name='blogpost_new')
]
