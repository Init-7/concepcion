from django.conf.urls import url, include
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import Predios, limiteComunal
from .views import SimpleMapLayer
from djgeojson.views import TiledGeoJSONLayerView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='muni/areaVerde.html'), name='muni'),
    url(r'^areaVerde/$', GeoJSONLayerView.as_view(model=areaVerde, properties=('rol_manzan', 'numero_pre')), name='areaVerde-hq'),
    url(r'^areaVerde.simple/$', SimpleMapLayer.as_view(model=ce, properties=('rol_manzan', 'numero_pre')), name='areaVerde'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/centrosDeportivos.html'), name='muni'),
    url(r'^centrosDeportivos/$', GeoJSONLayerView.as_view(model=centrosDeportivos, properties=('id_cd'), name='centrosDeportivos-hq'),
    url(r'^centrosDeportivos.simple/$', SimpleMapLayer.as_view(model=centrosDeportivos, properties=('id_cd')), name='centrosDeportivos'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/centrosPoliciales.html'), name='muni'),
    url(r'^centrosPoliciales/$', GeoJSONLayerView.as_view(model=centrosPoliciales, properties=('id_cp')), name='centrosPoliciales-hq'),
    url(r'^centrosPoliciales.simple/$', SimpleMapLayer.as_view(model=centrosPoliciales, properties=('id_cp')), name='centrosPoliciales'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/centrosReligiosos.html'), name='muni'),
    url(r'^centrosReligiosos/$', GeoJSONLayerView.as_view(model=centrosReligiosos, properties=('id_cr')), name='centrosReligiosos-hq'),
    url(r'^centrosReligiosos.simple/$', SimpleMapLayer.as_view(model=centrosReligiosos, properties=('id_cr')), name='centrosReligiosos'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/cotasDeElevacion.html'), name='muni'),
    url(r'^cotasDeElevacion/$', GeoJSONLayerView.as_view(model=cotasDeElevacion, properties=('desc')), name='cotasDeElevacion-hq'),
    url(r'^cotasDeElevacion.simple/$', SimpleMapLayer.as_view(model=cotasDeElevacion, properties=('desc')), name='cotasDeElevacion'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/curvasDeNivel.html'), name='muni'),
    url(r'^curvasDeNivel/$', GeoJSONLayerView.as_view(model=curvasDeNivel, properties=('desc')), name='curvasDeNivel-hq'),
    url(r'^curvasDeNivel.simple/$', SimpleMapLayer.as_view(model=curvasDeNivel, properties=('desc')), name='curvasDeNivel'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/edificacionPoligonos.html'), name='muni'),
    url(r'^edificacionPoligonos/$', GeoJSONLayerView.as_view(model=edificacionPoligonos, properties=('elevation'), name='edificacionPoligonos-hq'),
    url(r'^edificacionPoligonos.simple/$', SimpleMapLayer.as_view(model=edificacionPoligonos, properties=('elevation')), name='edificacionPoligonos'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/edificaciones.html'), name='muni'),
    url(r'^edificaciones/$', GeoJSONLayerView.as_view(model=Edificaciones, properties=('nombre_field')), name='edificaciones-hq'),
    url(r'^edificaciones.simple/$', SimpleMapLayer.as_view(model=Edificaciones, properties=('nombre_field')), name='edificaciones'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/ejercitoArmada.html'), name='muni'),
    url(r'^ejercitoArmada/$', GeoJSONLayerView.as_view(model=ejercitoArmada, properties=('id_ea')), name='ejercitoArmada-hq'),
    url(r'^ejercitoArmada.simple/$', SimpleMapLayer.as_view(model=ejercitoArmada, properties=('id_ea')), name='ejercitoArmada'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/ejes.html'), name='muni'),
    url(r'^ejes/$', GeoJSONLayerView.as_view(model=Ejes, properties=('nombre', 'tipo', 'material')), name='ejes-hq'),
    url(r'^ejes.simple/$', SimpleMapLayer.as_view(model=Ejes, properties=('nombre', 'tipo', 'material')), name='ejes'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/electrificacion.html'), name='muni'),
    url(r'^electrificacion/$', GeoJSONLayerView.as_view(model=Electrificacion, properties=('desc')), name='electrificacion-hq'),
    url(r'^electrificacion.simple/$', SimpleMapLayer.as_view(model=Electrificacion, properties=('desc')), name='electrificacion'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/ferrocaril.html'), name='muni'),
    url(r'^ferrocaril/$', GeoJSONLayerView.as_view(model=Ferrocaril, properties=('desc')), name='ferrocaril-hq'),
    url(r'^ferrocaril.simple/$', SimpleMapLayer.as_view(model=Ferrocaril, properties=('desc')), name='ferrocaril'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/ffcc.html'), name='muni'),
    url(r'^ffcc/$', GeoJSONLayerView.as_view(model=Ffcc, properties=('desc')), name='ffcc-hq'),
    url(r'^ffcc.simple/$', SimpleMapLayer.as_view(model=Ffcc, properties=('desc')), name='ffcc'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/hidrografia.html'), name='muni'),
    url(r'^hidrografia/$', GeoJSONLayerView.as_view(model=Hidrografia, properties=('subzona', 'tipo')), name='hidrografia-hq'),
    url(r'^hidrografia.simple/$', SimpleMapLayer.as_view(model=Hidrografia, properties=('subzona', 'tipo')), name='hidrografia'),
    
    url(r'^conce/$', TemplateView.as_view(template_name='muni/limites.html'), name='conce'),
    url(r'^limites/$', GeoJSONLayerView.as_view(model=limiteComunal, properties=('zona')), name='limites-hq'),
    url(r'^limites.simple/$', SimpleMapLayer.as_view(model=limiteComunal, properties=('zona')), name='limites'),
    url(r'^limites/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).geojson$',
    TiledGeoJSONLayerView.as_view(model=limiteComunal), name='limites-tiled'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/manzanas.html'), name='muni'),
    url(r'^manzanas/$', GeoJSONLayerView.as_view(model=Manzanas, properties=('rol_manzan')), name='manzanas-hq'),
    url(r'^manzanas.simple/$', SimpleMapLayer.as_view(model=Manzanas, properties=('rol_manzan')), name='manzanas'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/obrasCivilesViales.html'), name='muni'),
    url(r'^obrasCivilesViales/$', GeoJSONLayerView.as_view(model=obrasCivilesViales, properties=('desc')), name='obrasCivilesViales-hq'),
    url(r'^obrasCivilesViales.simple/$', SimpleMapLayer.as_view(model=obrasCivilesViales, properties=('desc')), name='obrasCivilesViales'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/plantaTratamientoDeAguas.html'), name='muni'),
    url(r'^plantaTratamientoDeAguas/$', GeoJSONLayerView.as_view(model=plantaTratamientoDeAguas, properties=('desc')), name='plantaTratamientoDeAguas-hq'),
    url(r'^plantaTratamientoDeAguas.simple/$', SimpleMapLayer.as_view(model=plantaTratamientoDeAguas, properties=('desc')), name='plantaTratamientoDeAguas'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/predios.html'), name='muni'),
    url(r'^predios/$', GeoJSONLayerView.as_view(model=Predios, properties=('rol_manzan', 'numero_pre')), name='predios-hq'),
    url(r'^predios.simple/$', SimpleMapLayer.as_view(model=Predios, properties=('rol_manzan', 'numero_pre')), name='predios'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/puntosDeControlTerrestre.html'), name='muni'),
    url(r'^puntosDeControlTerrestre/$', GeoJSONLayerView.as_view(model=puntosDeControlTerrestre, properties=('nombre')), name='puntosDeControlTerrestre-hq'),
    url(r'^puntosDeControlTerrestre.simple/$', SimpleMapLayer.as_view(model=puntosDeControlTerrestre, properties=('nombre')), name='puntosDeControlTerrestre'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/recintoDeEjercitoYArmada.html'), name='muni'),
    url(r'^recintoDeEjercitoYArmada/$', GeoJSONLayerView.as_view(model=recintoDeEjercitoYArmada, properties=('desc')), name='recintoDeEjercitoYArmada-hq'),
    url(r'^recintoDeEjercitoYArmada.simple/$', SimpleMapLayer.as_view(model=recintoDeEjercitoYArmada, properties=('desc')), name='recintoDeEjercitoYArmada'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/recintosDeportivos.html'), name='muni'),
    url(r'^recintosDeportivos/$', GeoJSONLayerView.as_view(model=recintosDeportivos, properties=('desc')), name='recintosDeportivos-hq'),
    url(r'^recintosDeportivos.simple/$', SimpleMapLayer.as_view(model=recintosDeportivos, properties=('desc')), name='recintosDeportivos'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/recintosEducacionales.html'), name='muni'),
    url(r'^recintosEducacionales/$', GeoJSONLayerView.as_view(model=recintosEducacionales, properties=('desc')), name='recintosEducacionales-hq'),
    url(r'^recintosEducacionales.simple/$', SimpleMapLayer.as_view(model=recintosEducacionales, properties=('desc')), name='recintosEducacionales'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/recintosPoliciales.html'), name='muni'),
    url(r'^recintosPoliciales/$', GeoJSONLayerView.as_view(model=recintosPoliciales, properties=('desc')), name='recintosPoliciales-hq'),
    url(r'^recintosPoliciales.simple/$', SimpleMapLayer.as_view(model=recintosPoliciales, properties=('desc')), name='recintosPoliciales'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/recintosReligiosos.html'), name='muni'),
    url(r'^recintosReligiosos/$', GeoJSONLayerView.as_view(model=recintosReligiosos, properties=('desc')), name='recintosReligiosos-hq'),
    url(r'^recintosReligiosos.simple/$', SimpleMapLayer.as_view(model=recintosReligiosos, properties=('desc')), name='recintosReligiosos'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/recintosSalud.html'), name='muni'),
    url(r'^recintosSalud/$', GeoJSONLayerView.as_view(model=recintosSalud, properties=('desc')), name='recintosSalud-hq'),
    url(r'^recintosSalud.simple/$', SimpleMapLayer.as_view(model=recintosSalud, properties=('desc')), name='recintosSalud'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/salud.html'), name='muni'),
    url(r'^salud/$', GeoJSONLayerView.as_view(model=Salud, properties=('id_salud')), name='salud-hq'),
    url(r'^salud.simple/$', SimpleMapLayer.as_view(model=Salud, properties=('id_salud')), name='salud'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/soleras.html'), name='muni'),
    url(r'^soleras/$', GeoJSONLayerView.as_view(model=Soleras, properties=('desc')), name='soleras-hq'),
    url(r'^soleras.simple/$', SimpleMapLayer.as_view(model=Soleras, properties=('desc')), name='soleras'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/textoDescriptivo.html'), name='muni'),
    url(r'^textoDescriptivo/$', GeoJSONLayerView.as_view(model=textoDescriptivo, properties=('desc')), name='textoDescriptivo-hq'),
    url(r'^textoDescriptivo.simple/$', SimpleMapLayer.as_view(model=textoDescriptivo, properties=('desc')), name='textoDescriptivo'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/vialidad.html'), name='muni'),
    url(r'^vialidad/$', GeoJSONLayerView.as_view(model=Vialidad, properties=('desc')), name='vialidad-hq'),
    url(r'^vialidad.simple/$', SimpleMapLayer.as_view(model=Vialidad, properties=('desc')), name='vialidad'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/viasEstructurantes.html'), name='muni'),
    url(r'^viasEstructurantes/$', GeoJSONLayerView.as_view(model=viasEstructurantes, properties=('id_ve', 'categoria')), name='viasEstructurantes-hq'),
    url(r'^viasEstructurantes.simple/$', SimpleMapLayer.as_view(model=viasEstructurantes, properties=('id_ve', 'categoria')), name='viasEstructurantes'),
    
    url(r'^$', TemplateView.as_view(template_name='muni/zonificacion.html'), name='muni'),
    url(r'^zonificacion/$', GeoJSONLayerView.as_view(model=Zonificacion, properties=('subzona', 'tipo')), name='zonificacion-hq'),
    url(r'^zonificacion.simple/$', SimpleMapLayer.as_view(model=Zonificacion properties=('subzona', 'tipo')), name='zonificacion'),
]
