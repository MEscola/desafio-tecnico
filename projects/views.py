from django.shortcuts import render

def home(request):
    contexto = {
        "meu_texto": "<p>Olá! Este é um <strong>teste prático</strong> para ver o filtro funcionando no navegador.</p>",
        "hello_world": "<p>O famoso Hello World</p>"
    }
    return render(request, 'index.html', contexto)
