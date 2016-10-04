from django.contrib import admin
from .models import Alumno
from .models import Curso
from .models import Nota
from .models import Docente
from .models import CriterioNota

admin.site.register(Docente)
admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Nota)
admin.site.register(CriterioNota)