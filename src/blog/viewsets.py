from rest_framework.viewsets import ModelViewSet

from blog.models import Postagem

from blog.serializers import PostagemSerializer

class PostagemViewSet(ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer

class PostagemSemCurtidaViewSet(ModelViewSet):
    queryset = Postagem.objects.all().exclude(curtidas__lte=50)
    serializer_class = PostagemSerializer