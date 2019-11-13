from django.shortcuts import render
from django.http import FileResponse, Http404

# Create your views here.
def home(request):
    return render(request, 'home.html')

def pdf_view(request):
    try:
        return FileResponse(open('KNH_Resume.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
