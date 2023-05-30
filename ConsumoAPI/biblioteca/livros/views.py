from django.forms import Form
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    response = requests.get('https://andersonlima.pythonanywhere.com/livros/')
    livros = response.json()
    context = {
        'livros': livros
    }
    return render(request, 'index.html', context)

def adicionar(request):
    if request.method == "POST":
        dados = request.POST
        novo_livro = {
            "titulo": dados["titulo"],
            "autor": dados["autor"],
            "ano_lancamento": dados["ano_lancamento"],
            "estado": dados["estado"],
            "paginas": dados["paginas"],
            "editora": dados["editora"],
        }
        post_response = requests.post('https://andersonlima.pythonanywhere.com/livros/', json=novo_livro)
        return redirect("index")

    context = {}
    return render(request, 'adicionar.html', context)

def patch(request, id):
    if request.method == "POST":
        dados = request.POST
        novo_livro = {
            "titulo": dados["titulo"],
            "autor": dados["autor"],
            "ano_lancamento": dados["ano_lancamento"],
            "estado": dados["estado"],
            "paginas": dados["paginas"],
            "editora": dados["editora"],
        }
        post_response = requests.put(f'https://andersonlima.pythonanywhere.com/livros/{id}/', json=novo_livro)
        return redirect("index")
    
    response = requests.get(f'https://andersonlima.pythonanywhere.com/livros/{id}/')
    livro = response.json()
    context = {
        'livro': livro
    }
    return render(request, 'patch.html', context)




def delete(request, id):
    response = requests.delete(f'https://andersonlima.pythonanywhere.com/livros/{id}/')
    return redirect("index")
