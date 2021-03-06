from django.shortcuts import render
from django.utils import timezone
from .models import Docente

def registro_list(request):
	docentes = Docente.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'registro/registro_list.html', {'docentes': docentes})
