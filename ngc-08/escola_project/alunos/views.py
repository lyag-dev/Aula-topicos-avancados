import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Aluno

# Tela inicial (Renderiza index.html)
def pagina_inicial(request):
    return render(request, 'index.html')