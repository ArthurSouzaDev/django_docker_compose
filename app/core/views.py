from django.shortcuts import render
from django.http import HttpResponse
from .models import Documento
from django.views.decorators.csrf import csrf_exempt 

@csrf_exempt 

def upload_arquivo(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        arquivo_enviado = request.FILES.get('documento')
        
        if titulo and arquivo_enviado:
            Documento.objects.create(titulo=titulo, arquivo=arquivo_enviado)
            return HttpResponse("<h2>Arquivo salvo com sucesso no Volume do Docker!</h2><a href='/'>Enviar outro</a>")
    html = """
    <html>
        <body style="font-family: Arial; padding: 50px;">
            <h2>Envie seu arquivo para o servidor</h2>
            <form method="post" enctype="multipart/form-data">
                <input type="text" name="titulo" placeholder="Nome do arquivo" required><br><br>
                <input type="file" name="documento" required><br><br>
                <button type="submit">Fazer Upload</button>
            </form>
        </body>
    </html>
    """
    return HttpResponse(html)