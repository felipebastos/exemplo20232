from rest_framework.serializers import HyperlinkedModelSerializer

from blog.models import Postagem

class PostagemSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Postagem
        fields = ['url', 'titulo', 'texto', 'curtidas']
