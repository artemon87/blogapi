from django.urls import path
#from .views import PostList, PostDetail
from .views import PostViewSet, UserViewset
from rest_framework.routers import SimpleRouter

#urlpatterns = [
    #path('<int:pk>/', PostDetail.as_view()),
    #path('', PostList.as_view()),
#]

router = SimpleRouter()
router.register('users', UserViewset, basename='users')
router.register('', PostViewSet, basename='posts')
#router.register('new', BlogCreateView, basename='post_new')


urlpatterns = router.urls
