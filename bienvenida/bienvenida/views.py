from django.http import HttpResponse

def inicio(request):
    nombre = "AmaraDuque23"
    return HttpResponse(f"Hola mundo desde Django,{nombre}")