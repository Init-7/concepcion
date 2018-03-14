import os
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.db import models
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

areaVerde_mapping = {
    'rol_manzan' : 'ROL_MANZAN',
    'numero_pre' : 'NUMERO_PRE',
    'otro' : 'OTRO',
    'objectid' : 'OBJECTID',
    'geom' : 'MULTIPOLYGON',
}

areaVerde_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'area_verde.shp'),
)

centrosDeportivos_mapping = {
    'id' : 'ID',
    'desc' : 'DESC',
    'geom' : 'MULTIPOINT',
}

centrosDeportivos_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'centros_deportivos.shp'),
)


centrosPoliciales_mapping = {
    'id' : 'ID',
    'desc' : 'DESC',
    'geom' : 'MULTIPOINT',
}

centrosPoliciales_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'centros_policiales.shp'),
)

    
centrosReligiosos_mapping = {
    'id' : 'ID',
    'desc' : 'DESC',
    'geom' : 'MULTIPOINT',
}

centrosReligiosos_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'centros_religiosos.shp'),
)


cotasDeElevacion_mapping = {
    'desc' : 'DESC',
    'cota' : 'COTA',
    'geom' : 'MULTIPOINT',
}

cotasDeElevacion_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'cotas_de_elevacion.shp'),
)

  
curvasDeNivel_mapping = {
    'desc' : 'DESC',
    'cota' : 'COTA',
    'geom' : 'MULTILINESTRING',
}

curvasDeNivel_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'curvas_de_nivel.shp'),
)

  
edificacionPoligonos_mapping = {
    'elevation' : 'ELEVATION',
    'geom' : 'MULTIPOLYGON',
}

edificacionPoligonos_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'edificacion_poligonos.shp'),
)


Edificaciones_mapping = {
    'nombre_field' : 'NOMBRE_',
    'desc' : 'DESC',
    'geom' : 'MULTIPOINT',
}

Edificaciones_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'edificaciones.shp'),
)

    
ejercitoArmada_mapping = {
    'id' : 'ID',
    'desc' : 'DESC',
    'geom' : 'MULTIPOINT',
}

ejercitoArmada_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'ejercito_armada.shp'),
)

    
Ejes_mapping = {
    'tipo' : 'TIPO',
    'material' : 'MATERIAL',
    'estado' : 'ESTADO',
    'id' : 'ID',
    'via' : 'VIA',
    'nombre' : 'NOMBRE',
    'desde' : 'DESDE',
    'hasta' : 'HASTA',
    'length' : 'LENGTH',
    'geom' : 'MULTILINESTRING',
}

Ejes_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'ejes.shp'),
)

    
Electrificacion_mapping = {
    'desc' : 'DESC',
    'geom' : 'MULTIPOINT',
}

Electrificacion_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'electrificacion.shp'),
)

    
Ferrocaril_mapping = {
    'desc' : 'DESC',
    'geom' : 'MULTIPOLYGON',
}

Ferrocaril_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'ferrocaril.shp'),
)

    
Ffcc_mapping = {
    'desc' : 'DESC',
    'ffp' : 'FFP',
    'geom' : 'MULTILINESTRING',
}

Ffcc_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'ffcc.shp'),
)

   
Hidrografia_mapping = {
    'subzona' : 'SUBZONA',
    'tipo' : 'TIPO',
    'achu' : 'ACHU',
    'zona' : 'ZONA',
    'geom' : 'MULTIPOLYGON',
}

Hidrografia_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'hidrografia.shp'),
)

    
limiteComunal_mapping = {
    'zona' : 'ZONA',
    'geom' : 'MULTIPOLYGON',
}

limiteComunal_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'limite_comunal.shp'),
)

    
Manzanas_mapping = {
    'rol_manzan' : 'ROL_MANZAN',
    'geom' : 'MULTIPOLYGON',
}

Manzanas_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'manzanas.shp'),
)

    
obrasCivilesViales_mapping = {
    'desc' : 'DESC',
    'geom' : 'MULTIPOLYGON',
}

obrasCivilesViales_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'obras_civiles_viales.shp'),
)

    
plantaTratamientoDeAguas_mapping = {
    'desc' : 'DESC',
    'geom' : 'MULTIPOLYGON',
}

plantaTratamientoDeAguas_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'planta_tratamiento_de_aguas.shp'),
)

    
Predios_mapping = {
    'rol_manzan' : 'ROL_MANZAN',
    'numero_pre' : 'NUMERO_PRE',
    'otro' : 'OTRO',
    'fid' : 'FID',
    'geom' : 'MULTIPOLYGON',
}

Predios_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'predios.shp'),
)

    
puntosDeControlTerrestre_mapping = {
    'nombre' : 'NOMBRE',
    'utmn84' : 'UTMN84',
    'utme84' : 'UTME84',
    'alt_snmm' : 'ALT_SNMM',
    'geom' : 'MULTIPOINT',
}

puntosDeControlTerrestre_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'puntos_de_control_terrestre.shp'),
)

    
recintoDeEjercitoYArmada_mapping = {
    'desc' : 'DESC',
    'geom' : 'MULTIPOLYGON',
}

recintoDeEjercitoYArmada_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'recinto_de_ejercito_y_armada.shp'),
)

    
recintosDeportivos_mapping = {
    'desc' : 'DESC',
    'geom' : 'MULTIPOLYGON',
}

recintosDeportivos_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'recintos_deportivos.shp'),
)

    
recintosEducacionales_mapping = {
    'desc' : 'DESC',
    'geom' : 'MULTIPOLYGON',
}

recintosEducacionales_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'recintos_educacionales.shp'),
)

    
recintosPoliciales_mapping = {
    'desc' : 'DESC',
    'geom' : 'MULTIPOLYGON',
}

recintosPoliciales_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'recintos_policiales.shp'),
)

    
recintosReligiosos_mapping = {
    'desc' : 'DESC',
    'geom' : 'MULTIPOLYGON',
}

recintosReligiosos_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'recintos_religiosos.shp'),
)

    
recintosSalud_mapping = {
    'desc' : 'DESC',
    'geom' : 'MULTIPOLYGON',
}

recintosSalud_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'recintos_salud.shp'),
)

    
Salud_mapping = {
    'id' : 'ID',
    'desc' : 'DESC',
    'geom' : 'MULTIPOINT',
}

Salud_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'salud.shp'),
)

    
Soleras_mapping = {
    'desc' : 'DESC',
    'geom' : 'MULTILINESTRING',
}

Soleras_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'soleras.shp'),
)

    
textoDescriptivo_mapping = {
    'desc' : 'DESC',
    'geom' : 'MULTIPOINT',
}

textoDescriptivo_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'texto_descriptivo.shp'),
)

    
Vialidad_mapping = {
    'desc' : 'DESC',
    'geom' : 'MULTIPOLYGON',
}

Vialidad_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'vialidad.shp'),
)

    
viasEstructurantes_mapping = {
    'id' : 'ID',
    'categoria' : 'CATEGORIA',
    'n_via' : 'N_VIA',
    'desde' : 'DESDE',
    'hasta' : 'HASTA',
    'faja_exi' : 'FAJA_EXI',
    'faja_pro' : 'FAJA_PRO',
    'condicion' : 'CONDICION',
    'observa' : 'OBSERVA',
    'atrib_esp' : 'ATRIB_ESP',
    'geom' : 'MULTILINESTRING',
}

viasEstructurantes_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'vias_estructurantes.shp'),
)

    
Zonificacion_mapping = {
    'desc' : 'DESC',
    'geom' : 'MULTIPOLYGON',
}

Zonificacion_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'zonificacion.shp'),
)


def run1(verbose=True):
    lm = LayerMapping(
        areaVerde, areaVerde_shp, areaVerde_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)

def run2(verbose=True):
    lm = LayerMapping(
        centrosDeportivos, centrosDeportivos_shp, centrosDeportivos_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run3(verbose=True):
    lm = LayerMapping(
        centrosPoliciales, centrosPoliciales_shp, centrosPoliciales_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run4(verbose=True):
    lm = LayerMapping(
        centrosReligiosos, centrosReligiosos_shp, centrosReligiosos_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)

def run5(verbose=True):
    lm = LayerMapping(
        cotasDeElevacion, cotasDeElevacion_shp, cotasDeElevacion_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)

def run6(verbose=True):
    lm = LayerMapping(
        curvasDeNivel, curvasDeNivel_shp, curvasDeNivel_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
  
def run7(verbose=True):
    lm = LayerMapping(
        edificacionPoligonos, edificacionPoligonos_shp, edificacionPoligonos_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
  
def run8(verbose=True):
    lm = LayerMapping(
        Edificaciones, Edificaciones_shp, Edificaciones_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run9(verbose=True):
    lm = LayerMapping(
        ejercitoArmada, ejercitoArmada_shp, ejercitoArmada_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run10(verbose=True):
    lm = LayerMapping(
        Ejes, Ejes_shp, Ejes_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run11(verbose=True):
    lm = LayerMapping(
        Electrificacion, Electrificacion_shp, Electrificacion_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run12(verbose=True):
    lm = LayerMapping(
        Ferrocaril, Ferrocaril_shp, Ferrocaril_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run13(verbose=True):
    lm = LayerMapping(
        Ffcc, Ffcc_shp, Ffcc_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run14(verbose=True):
    lm = LayerMapping(
        Hidrografia, Hidrografia_shp, Hidrografia_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run15(verbose=True):
    lm = LayerMapping(
        limiteComunal, limiteComunal_shp, limiteComunal_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run16(verbose=True):
    lm = LayerMapping(
        Manzanas, Manzanas_shp, Manzanas_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run17(verbose=True):
    lm = LayerMapping(
        obrasCivilesViales, obrasCivilesViales_shp, obrasCivilesViales_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run18(verbose=True):
    lm = LayerMapping(
        plantaTratamientoDeAguas, plantaTratamientoDeAguas_shp, plantaTratamientoDeAguas_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run19(verbose=True):
    lm = LayerMapping(
        Predios, Predios_shp, Predios_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run20(verbose=True):
    lm = LayerMapping(
        puntosDeControlTerrestre, puntosDeControlTerrestre_shp, puntosDeControlTerrestre_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run21(verbose=True):
    lm = LayerMapping(
        recintoDeEjercitoYArmada, recintoDeEjercitoYArmada_shp, recintoDeEjercitoYArmada_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run22(verbose=True):
    lm = LayerMapping(
        recintosDeportivos, recintosDeportivos_shp, recintosDeportivos_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run23(verbose=True):
    lm = LayerMapping(
        recintosEducacionales, recintosEducacionales_shp, recintosEducacionales_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run24(verbose=True):
    lm = LayerMapping(
        recintosPoliciales, recintosPoliciales_shp, recintosPoliciales_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run25(verbose=True):
    lm = LayerMapping(
        recintosReligiosos, recintosReligiosos_shp, recintosReligiosos_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run26(verbose=True):
    lm = LayerMapping(
        recintosSalud, recintosSalud_shp, recintosSalud_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run27(verbose=True):
    lm = LayerMapping(
        Salud, Salud_shp, Salud_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run28(verbose=True):
    lm = LayerMapping(
        Soleras, Soleras_shp, Soleras_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run29(verbose=True):
    lm = LayerMapping(
        textoDescriptivo, textoDescriptivo_shp, textoDescriptivo_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run30(verbose=True):
    lm = LayerMapping(
        Vialidad, Vialidad_shp, Vialidad_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run31(verbose=True):
    lm = LayerMapping(
        viasEstructurantes, viasEstructurantes_shp, viasEstructurantes_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
    
def run32(verbose=True):
    lm = LayerMapping(
        Zonificacion, Zonificacion_shp, Zonificacion_mapping,
        transform=True, encoding='utf-8', source_srs='32718',
    )
    lm.save(strict=False, verbose=verbose)
