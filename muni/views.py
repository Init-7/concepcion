# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.http import HttpResponse
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

from djgeojson.views import GeoJSONLayerView

class SimpleMapLayer(GeoJSONLayerView):
    # Options
    precision = 4   # float
    simplify = 0.5  # generalization

def areasVerdes(request):
    areasVerdes = areaVerde.objects.all()
#    contenidos = []

    data = GeoJSONSerializer().serialize(areasVerdes, use_natural_keys=True, with_modelname=False)

    return HttpResponse(data)

def areasVerde(request, aidi):
    areasVerde = areaVerde.objects.get(id = id_av)
    #Agregar envio de centro para el mapa
    lat = pais.geom.centroid.y
    lon = pais.geom.centroid.x
    return render(request, 'muni/areaVerde.html',{'qs_results': areasVerde,
                                             'latitude':lat,
                                             'longitude': lon}
                 )
