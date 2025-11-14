from django.http import HttpResponse
from django.utils import timezone

def fecha(request):
    now = timezone.now()
    
    html_content = f"""
    <h1>Fecha: {now.strftime('%Y-%m-%d')}</h1><br>
    <h1>Hora: {now.strftime('%I:%M:%S %p')}</h1><br>
    """
    
    return HttpResponse(html_content)
