from django.urls import path, include

from blog.views import postagens
from django.contrib.auth.models import User

from rest_framework import routers, viewsets, serializers

from blog.viewsets import PostagemViewSet, PostagemSemCurtidaViewSet
from blog.views import ListUsuarios

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'postagens', PostagemViewSet)
#router.register(r'muitacurtida', PostagemSemCurtidaViewSet, basename='sucesso')

urlpatterns = [
    path('', include(router.urls)),
    path('usernames/', ListUsuarios.as_view()),
]
