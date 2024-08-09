from django.shortcuts import render
from django.http import JsonResponse
from blog.models import Postagem
from django.contrib.auth.models import User

# Create your views here.
def postagens(request):
    """
        GET - Requer um recurso. GET /alunos?id=3 -> SELECT -> cRud
        POST - Inserir dados novos num recurso. POST /alunos -> INSERT -> Crud
        PUT - Atualizar uma entidade no recurso. PUT /alunos?id=3 -> UPDATE [total] -> crUd
        PATCH - Atualização parcial no recurso. PATCH /alunos?id=3 -> UPDATE [parcial] -> crUd
        DELETE - DELETE /alunos?id=3 -> DELETE -> cruD
        HEAD
        TRACE
        OPTIONS
    """
    if request.method == 'GET':
        posts = Postagem.objects.all() # select * from blog_postagem;

        p_dict = {}

        for p in posts:
            p_dict[p.id] = p.titulo

        #lista = ""

        #for p in posts:
        #    lista += p.titulo + '<br/>'

        return JsonResponse(p_dict)
    
    novo_post = Postagem()
    novo_post.titulo = request.POST['TITULO']
    novo_post.texto = "oi oi oi"
    
    novo_post.autor = User.objects.get(pk=2)

    novo_post.save()

    return JsonResponse({'status': 'success'})


# Class based views
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import permissions

import requests as r


class ListUsuarios(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        nomes = [user.username for user in User.objects.all()]

        luke = r.get('https://swapi.dev/api/people/1/')

        nome = luke.json()['name']
        nomes.append(nome)

        return Response(nomes)

    def post(self, request):
        json = request.data

        nome = json['username']
        senha = json['password']

        novo = User.objects.create(username=nome, password=senha)
        

        return Response({ 'status': 'Sucesso', 'usuario_id': novo.id})


    def put(self, request):
        id = request.data['id']
        novo_nome = request.data['new_name']

        user = User.objects.get(pk=id)
        user.username = novo_nome
        user.save()

        return Response('Salvei')

    def delete(self, request):
        id = request.query_params.get('id')

        user = User.objects.get(pk=id)
        user.delete()

        return Response('Removido')

