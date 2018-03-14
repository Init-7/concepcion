# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis import admin

#modelos
from .models import areaVerde
from .models import centrosDeportivos
from .models import centrosPoliciales
from .models import centrosReligiosos
from .models import cotasDeElevacion
from .models import curvasDeNivel
from .models import edificacionPoligonos
from .models import Edificaciones
from .models import ejercitoArmada
from .models import Ejes
from .models import Electrificacion
from .models import Ferrocaril
from .models import Ffcc
from .models import Hidrografia
from .models import limiteComunal
from .models import Manzanas
from .models import obrasCivilesViales
from .models import plantaTratamientoDeAguas
from .models import Predios
from .models import puntosDeControlTerrestre
from .models import recintoDeEjercitoYArmada
from .models import recintosDeportivos
from .models import recintosEducacionales
from .models import recintosPoliciales
from .models import recintosReligiosos
from .models import recintosSalud
from .models import Salud
from .models import Soleras
from .models import textoDescriptivo
from .models import Vialidad
from .models import viasEstructurantes
from .models import Zonificacion

admin.site.register(areaVerde)
admin.site.register(centrosDeportivos)
admin.site.register(centrosPoliciales)
admin.site.register(centrosReligiosos)
admin.site.register(cotasDeElevacion)
admin.site.register(curvasDeNivel)
admin.site.register(edificacionPoligonos)
admin.site.register(Edificaciones)
admin.site.register(ejercitoArmada)
admin.site.register(Ejes)
admin.site.register(Electrificacion)
admin.site.register(Ferrocaril)
admin.site.register(Ffcc)
admin.site.register(Hidrografia)
admin.site.register(limiteComunal)
admin.site.register(Manzanas)
admin.site.register(obrasCivilesViales)
admin.site.register(plantaTratamientoDeAguas)
admin.site.register(Predios)
admin.site.register(puntosDeControlTerrestre)
admin.site.register(recintoDeEjercitoYArmada)
admin.site.register(recintosDeportivos)
admin.site.register(recintosEducacionales)
admin.site.register(recintosPoliciales)
admin.site.register(recintosReligiosos)
admin.site.register(recintosSalud)
admin.site.register(Salud)
admin.site.register(Soleras)
admin.site.register(textoDescriptivo)
admin.site.register(Vialidad)
admin.site.register(viasEstructurantes)
admin.site.register(Zonificacion)
