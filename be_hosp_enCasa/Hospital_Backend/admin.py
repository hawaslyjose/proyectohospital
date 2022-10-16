from django.contrib import admin

from .models.usuario import Usuario
from .models.medico import Medico
from .models.paciente import Paciente
from .models.familiar import Familiar
from .models.hist_clinica import Historia_clinica 
from .models.signos import Signos_vitales
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Familiar)
admin.site.register(Historia_clinica)
admin.site.register(Signos_vitales)