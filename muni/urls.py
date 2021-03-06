from django.conf.urls import url, include
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import *
from .views import SimpleMapLayer
from djgeojson.views import TiledGeoJSONLayerView


urlpatterns = [
    url(r'^Areasverdes/$', TemplateView.as_view(template_name='muni/areaVerde.html'), name='area-verde'),
    url(r'^areaVerde/$', GeoJSONLayerView.as_view(model=areaVerde, properties=('rol_manzan', 'numero_pre')), name='areaVerde-hq'),
    url(r'^areaVerde.simple/$', SimpleMapLayer.as_view(model=areaVerde, properties=('rol_manzan', 'numero_pre')), name='areaVerde'),
    url(r'^CentrosDeportivos/$', TemplateView.as_view(template_name='muni/centrosDeportivos.html'), name='deporte'),
    url(r'^centrosDeportivos/$', GeoJSONLayerView.as_view(model=centrosDeportivos, properties=('id_cd')), name='centrosDeportivos-hq'),
    url(r'^centrosDeportivos.simple/$', SimpleMapLayer.as_view(model=centrosDeportivos, properties=('id_cd')), name='centrosDeportivos'), 
    url(r'^CentrosPoliciales/$', TemplateView.as_view(template_name='muni/centrosPoliciales.html'), name='policia'),
    url(r'^centrosPoliciales/$', GeoJSONLayerView.as_view(model=centrosPoliciales, properties=('id_cp')), name='centrosPoliciales-hq'),
    url(r'^centrosPoliciales.simple/$', SimpleMapLayer.as_view(model=centrosPoliciales, properties=('id_cp')), name='centrosPoliciales'), 
    url(r'^CentrosReligiosos/$', TemplateView.as_view(template_name='muni/centrosReligiosos.html'), name='culto'),
    url(r'^centrosReligiosos/$', GeoJSONLayerView.as_view(model=centrosReligiosos, properties=('id_cr')), name='centrosReligiosos-hq'),
    url(r'^centrosReligiosos.simple/$', SimpleMapLayer.as_view(model=centrosReligiosos, properties=('id_cr')), name='centrosReligiosos'),
    url(r'^CotasElevacion/$', TemplateView.as_view(template_name='muni/cotasDeElevacion.html'), name='cotas'),
    url(r'^cotasDeElevacion/$', GeoJSONLayerView.as_view(model=cotasDeElevacion, properties=('desc')), name='cotasDeElevacion-hq'),
    url(r'^cotasDeElevacion.simple/$', SimpleMapLayer.as_view(model=cotasDeElevacion, properties=('desc')), name='cotasDeElevacion'),
    url(r'^CurvasDeNivel/$', TemplateView.as_view(template_name='muni/curvasDeNivel.html'), name='curva-nivel'),
    url(r'^curvasDeNivel/$', GeoJSONLayerView.as_view(model=curvasDeNivel, properties=('desc')), name='curvasDeNivel-hq'),
    url(r'^curvasDeNivel.simple/$', SimpleMapLayer.as_view(model=curvasDeNivel, properties=('desc')), name='curvasDeNivel'),
    url(r'^EdificacionPoligonos/$', TemplateView.as_view(template_name='muni/edificacionPoligonos.html'), name='edi-poli'),
    url(r'^edificacionPoligonos/$', GeoJSONLayerView.as_view(model=edificacionPoligonos, properties=('elevation')), name='edificacionPoligonos-hq'),
    url(r'^edificacionPoligonos.simple/$', SimpleMapLayer.as_view(model=edificacionPoligonos, properties=('elevation')), name='edificacionPoligonos'),
    url(r'^Edificaciones/$', TemplateView.as_view(template_name='muni/edificaciones.html'), name='edi'),
    url(r'^edificaciones/$', GeoJSONLayerView.as_view(model=Edificaciones, properties=('nombre_field')), name='edificaciones-hq'),
    url(r'^edificaciones.simple/$', SimpleMapLayer.as_view(model=Edificaciones, properties=('nombre_field')), name='edificaciones'),
    url(r'^EjercitoArmada/$', TemplateView.as_view(template_name='muni/ejercitoArmada.html'), name='ejercito'),
    url(r'^ejercitoArmada/$', GeoJSONLayerView.as_view(model=ejercitoArmada, properties=('id_ea')), name='ejercitoArmada-hq'),
    url(r'^ejercitoArmada.simple/$', SimpleMapLayer.as_view(model=ejercitoArmada, properties=('id_ea')), name='ejercitoArmada'),
    url(r'^Ejes/$', TemplateView.as_view(template_name='muni/ejes.html'), name='ejes'),
    url(r'^ejes/$', GeoJSONLayerView.as_view(model=Ejes, properties=('nombre', 'tipo', 'material')), name='ejes-hq'),
    url(r'^ejes.simple/$', SimpleMapLayer.as_view(model=Ejes, properties=('nombre', 'tipo', 'material')), name='ejes'),
    url(r'^Electrificacion/$', TemplateView.as_view(template_name='muni/electrificacion.html'), name='postes'),
    url(r'^electrificacion/$', GeoJSONLayerView.as_view(model=Electrificacion, properties=('desc')), name='electrificacion-hq'),
    url(r'^electrificacion.simple/$', SimpleMapLayer.as_view(model=Electrificacion, properties=('desc')), name='electrificacion'),
    url(r'^Ferrocarril/$', TemplateView.as_view(template_name='muni/ferrocaril.html'), name='ferrocarril'),
    url(r'^ferrocaril/$', GeoJSONLayerView.as_view(model=Ferrocaril, properties=('desc')), name='ferrocaril-hq'),
    url(r'^ferrocaril.simple/$', SimpleMapLayer.as_view(model=Ferrocaril, properties=('desc')), name='ferrocaril'),
    url(r'^FFCC/$', TemplateView.as_view(template_name='muni/ffcc.html'), name='ffcc'),
    url(r'^ffcc/$', GeoJSONLayerView.as_view(model=Ffcc, properties=('desc')), name='ffcc-hq'),
    url(r'^ffcc.simple/$', SimpleMapLayer.as_view(model=Ffcc, properties=('desc')), name='ffcc'),
    url(r'^Hidrografia/$', TemplateView.as_view(template_name='muni/hidrografia.html'), name='hidrografia'),
    url(r'^hidrografia/$', GeoJSONLayerView.as_view(model=Hidrografia, properties=('subzona', 'tipo')), name='hidrografia-hq'),
    url(r'^hidrografia.simple/$', SimpleMapLayer.as_view(model=Hidrografia, properties=('subzona', 'tipo')), name='hidrografia'),
    url(r'^conce/$', TemplateView.as_view(template_name='muni/limites.html'), name='limites'),
    url(r'^limites/$', GeoJSONLayerView.as_view(model=limiteComunal, properties=('zona')), name='limites-hq'),
    url(r'^limites.simple/$', SimpleMapLayer.as_view(model=limiteComunal, properties=('zona')), name='limites'),
    url(r'^limites/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).geojson$', TiledGeoJSONLayerView.as_view(model=limiteComunal), name='limites-tiled'),
    url(r'^Manzanas/$', TemplateView.as_view(template_name='muni/manzanas.html'), name='manzanas'),
    url(r'^manzanas/$', GeoJSONLayerView.as_view(model=Manzanas, properties=('rol_manzan')), name='manzanas-hq'),
    url(r'^manzanas.simple/$', SimpleMapLayer.as_view(model=Manzanas, properties=('rol_manzan')), name='manzanas'),
    url(r'^ObrasCiviles$', TemplateView.as_view(template_name='muni/obrasCivilesViales.html'), name='obrasciviles'),
    url(r'^obrasCivilesViales/$', GeoJSONLayerView.as_view(model=obrasCivilesViales, properties=('desc')), name='obrasCivilesViales-hq'),
    url(r'^obrasCivilesViales.simple/$', SimpleMapLayer.as_view(model=obrasCivilesViales, properties=('desc')), name='obrasCivilesViales'),
    url(r'^PlantasTratamientoAguas$', TemplateView.as_view(template_name='muni/plantaTratamientoDeAguas.html'), name='planta-agua'),
    url(r'^plantaTratamientoDeAguas/$', GeoJSONLayerView.as_view(model=plantaTratamientoDeAguas, properties=('desc')), name='plantaTratamientoDeAguas-hq'),
    url(r'^plantaTratamientoDeAguas.simple/$', SimpleMapLayer.as_view(model=plantaTratamientoDeAguas, properties=('desc')), name='plantaTratamientoDeAguas'),
    url(r'^Predios/$', TemplateView.as_view(template_name='muni/predios.html'), name='predio'),
    url(r'^predios/$', GeoJSONLayerView.as_view(model=Predios, properties=('rol_manzan', 'numero_pre')), name='predios-hq'),
    url(r'^predios.simple/$', SimpleMapLayer.as_view(model=Predios, properties=('rol_manzan', 'numero_pre')), name='predios'),
    url(r'^PuntosDeControlTerrestre/$', TemplateView.as_view(template_name='muni/puntosDeControlTerrestre.html'), name='control-terrestre'),
    url(r'^puntosDeControlTerrestre/$', GeoJSONLayerView.as_view(model=puntosDeControlTerrestre, properties=('nombre')), name='puntosDeControlTerrestre-hq'),
    url(r'^puntosDeControlTerrestre.simple/$', SimpleMapLayer.as_view(model=puntosDeControlTerrestre, properties=('nombre')), name='puntosDeControlTerrestre'),
    url(r'^RecintoDeEjercitoYArmada/$', TemplateView.as_view(template_name='muni/recintoDeEjercitoYArmada.html'), name='ejercito'),
    url(r'^recintoDeEjercitoYArmada/$', GeoJSONLayerView.as_view(model=recintoDeEjercitoYArmada, properties=('desc')), name='recintoDeEjercitoYArmada-hq'),
    url(r'^recintoDeEjercitoYArmada.simple/$', SimpleMapLayer.as_view(model=recintoDeEjercitoYArmada, properties=('desc')), name='recintoDeEjercitoYArmada'),
    url(r'^RecintosDeportivos/$', TemplateView.as_view(template_name='muni/recintosDeportivos.html'), name='rec-deporte'),
    url(r'^recintosDeportivos/$', GeoJSONLayerView.as_view(model=recintosDeportivos, properties=('desc')), name='recintosDeportivos-hq'),
    url(r'^recintosDeportivos.simple/$', SimpleMapLayer.as_view(model=recintosDeportivos, properties=('desc')), name='recintosDeportivos'),
    url(r'^RecintosEducacionales/$', TemplateView.as_view(template_name='muni/recintosEducacionales.html'), name='educacion'),
    url(r'^recintosEducacionales/$', GeoJSONLayerView.as_view(model=recintosEducacionales, properties=('desc')), name='recintosEducacionales-hq'),
    url(r'^recintosEducacionales.simple/$', SimpleMapLayer.as_view(model=recintosEducacionales, properties=('desc')), name='recintosEducacionales'),
    url(r'^RecintosPoliciales/$', TemplateView.as_view(template_name='muni/recintosPoliciales.html'), name='rec-policia'),
    url(r'^recintosPoliciales/$', GeoJSONLayerView.as_view(model=recintosPoliciales, properties=('desc')), name='recintosPoliciales-hq'),
    url(r'^recintosPoliciales.simple/$', SimpleMapLayer.as_view(model=recintosPoliciales, properties=('desc')), name='recintosPoliciales'),
    url(r'^RecintosReligiosos/$', TemplateView.as_view(template_name='muni/recintosReligiosos.html'), name='rec-religioso'),
    url(r'^recintosReligiosos/$', GeoJSONLayerView.as_view(model=recintosReligiosos, properties=('desc')), name='recintosReligiosos-hq'),
    url(r'^recintosReligiosos.simple/$', SimpleMapLayer.as_view(model=recintosReligiosos, properties=('desc')), name='recintosReligiosos'),
    url(r'^RecintosSalud/$', TemplateView.as_view(template_name='muni/recintosSalud.html'), name='rec-salud'),
    url(r'^recintosSalud/$', GeoJSONLayerView.as_view(model=recintosSalud, properties=('desc')), name='recintosSalud-hq'),
    url(r'^recintosSalud.simple/$', SimpleMapLayer.as_view(model=recintosSalud, properties=('desc')), name='recintosSalud'),
    url(r'^Salud$', TemplateView.as_view(template_name='muni/salud.html'), name='salud'),
    url(r'^salud/$', GeoJSONLayerView.as_view(model=Salud, properties=('id_salud')), name='salud-hq'),
    url(r'^salud.simple/$', SimpleMapLayer.as_view(model=Salud, properties=('id_salud')), name='salud'),
    url(r'^Soleras$', TemplateView.as_view(template_name='muni/soleras.html'), name='soleras'),
    url(r'^soleras/$', GeoJSONLayerView.as_view(model=Soleras, properties=('desc')), name='soleras-hq'),
    url(r'^soleras.simple/$', SimpleMapLayer.as_view(model=Soleras, properties=('desc')), name='soleras'),
    url(r'^TextoDescriptivo$', TemplateView.as_view(template_name='muni/textoDescriptivo.html'), name='muni'),
    url(r'^textoDescriptivo/$', GeoJSONLayerView.as_view(model=textoDescriptivo, properties=('desc')), name='textoDescriptivo-hq'),
    url(r'^textoDescriptivo.simple/$', SimpleMapLayer.as_view(model=textoDescriptivo, properties=('desc')), name='textoDescriptivo'),
    url(r'^Vialidad/$', TemplateView.as_view(template_name='muni/vialidad.html'), name='vialidad'),
    url(r'^vialidad/$', GeoJSONLayerView.as_view(model=Vialidad, properties=('desc')), name='vialidad-hq'),
    url(r'^vialidad.simple/$', SimpleMapLayer.as_view(model=Vialidad, properties=('desc')), name='vialidad'),
    url(r'^ViasEstructurantes/$', TemplateView.as_view(template_name='muni/viasEstructurantes.html'), name='vias-estruc'),
    url(r'^viasEstructurantes/$', GeoJSONLayerView.as_view(model=viasEstructurantes, properties=('id_ve', 'categoria')), name='viasEstructurantes-hq'),
    url(r'^viasEstructurantes.simple/$', SimpleMapLayer.as_view(model=viasEstructurantes, properties=('id_ve', 'categoria')), name='viasEstructurantes'),
    url(r'^Zonificacion/$', TemplateView.as_view(template_name='muni/zonificacion.html'), name='zonificacion'),
    url(r'^zonificacion/$', GeoJSONLayerView.as_view(model=Zonificacion, properties=('subzona', 'tipo')), name='zonificacion-hq'),
    url(r'^zonificacion.simple/$', SimpleMapLayer.as_view(model=Zonificacion, properties=('subzona', 'tipo')), name='zonificacion'),
]
