# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis.db import models


class areaVerde(models.Model):
    rol_manzan = models.CharField(max_length=11)
    numero_pre = models.CharField(max_length=250)
    otro = models.CharField(max_length=50)
    objectid = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

class centrosDeportivos(models.Model):
    id_cd = models.IntegerField()
    desc = models.CharField(max_length=20)
    geom = models.MultiPointField(srid=4326)

class centrosPoliciales(models.Model):                                                              
    id_cp = models.IntegerField()                                                               
    desc = models.CharField(max_length=50)                                                   
    geom = models.MultiPointField(srid=4326)
    
class centrosReligiosos(models.Model):
    id_cr = models.IntegerField()
    desc = models.CharField(max_length=20)
    geom = models.MultiPointField(srid=4326)
    
class cotasDeElevacion(models.Model):
    desc = models.CharField(max_length=50)
    cota = models.FloatField()
    geom = models.MultiPointField(srid=4326)

class curvasDeNivel(models.Model):
    desc = models.CharField(max_length=50)
    cota = models.BigIntegerField()
    geom = models.MultiLineStringField(srid=4326)
    
class edificacionPoligonos(models.Model):
    elevation = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

class Edificaciones(models.Model):
    nombre_field = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    geom = models.MultiPointField(srid=4326)
    
class ejercitoArmada(models.Model):
    id_ea = models.IntegerField()
    desc = models.CharField(max_length=20)
    geom = models.MultiPointField(srid=4326)

class Ejes(models.Model):
    tipo = models.CharField(max_length=8)
    material = models.CharField(max_length=12)
    estado = models.CharField(max_length=9)
    id_ejes = models.IntegerField()
    via = models.CharField(max_length=13)
    nombre = models.CharField(max_length=100)
    desde = models.CharField(max_length=30)
    hasta = models.CharField(max_length=30)
    length = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    
class Electrificacion(models.Model):
    desc = models.CharField(max_length=50)
    geom = models.MultiPointField(srid=4326)

class Ferrocaril(models.Model):
    desc = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)

class Ffcc(models.Model):
    desc = models.CharField(max_length=20)
    ffp = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)

class Hidrografia(models.Model):
    subzona = models.CharField(max_length=6)
    tipo = models.IntegerField()
    achu = models.BigIntegerField()
    zona = models.CharField(max_length=100)
    geom = models.MultiPolygonField(srid=4326)

class limiteComunal(models.Model):
    zona = models.CharField(max_length=6)
    geom = models.MultiPolygonField(srid=4326)

class Manzanas(models.Model):
    rol_manzan = models.CharField(max_length=11)
    geom = models.MultiPolygonField(srid=4326)
    
class obrasCivilesViales(models.Model):
    desc = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)

class plantaTratamientoDeAguas(models.Model):
    desc = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)

class Predios(models.Model):
    rol_manzan = models.CharField(max_length=11)
    numero_pre = models.CharField(max_length=250)
    otro = models.CharField(max_length=50)
    fid = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

class puntosDeControlTerrestre(models.Model):
    nombre = models.IntegerField()
    utmn84 = models.FloatField()
    utme84 = models.FloatField()
    alt_snmm = models.FloatField()
    geom = models.MultiPointField(srid=4326)

class recintoDeEjercitoYArmada(models.Model):
    desc = models.CharField(max_length=20)
    geom = models.MultiPolygonField(srid=4326)

class recintosDeportivos(models.Model):
    desc = models.CharField(max_length=20)
    geom = models.MultiPolygonField(srid=4326)

class recintosEducacionales(models.Model):
    desc = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)

class recintosPoliciales(models.Model):
    desc = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    
class recintosReligiosos(models.Model):
    desc = models.CharField(max_length=20)
    geom = models.MultiPolygonField(srid=4326)

class recintosSalud(models.Model):
    desc = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    
class Salud(models.Model):
    id_salud = models.IntegerField()
    desc = models.CharField(max_length=50)
    geom = models.MultiPointField(srid=4326)

class Soleras(models.Model):
    desc = models.CharField(max_length=30)
    geom = models.MultiLineStringField(srid=4326)

class textoDescriptivo(models.Model):
    desc = models.CharField(max_length=50)
    geom = models.MultiPointField(srid=4326)

class Vialidad(models.Model):
    desc = models.CharField(max_length=20)
    geom = models.MultiPolygonField(srid=4326)

class viasEstructurantes(models.Model):
    id_ve = models.IntegerField()
    categoria = models.CharField(max_length=23)
    n_via = models.CharField(max_length=54)
    desde = models.CharField(max_length=31)
    hasta = models.CharField(max_length=63)
    faja_exi = models.CharField(max_length=30)
    faja_pro = models.CharField(max_length=30)
    condicion = models.CharField(max_length=31)
    observa = models.CharField(max_length=215)
    atrib_esp = models.CharField(max_length=143)
    geom = models.MultiLineStringField(srid=4326)

class Zonificacion(models.Model):
    subzona = models.CharField(max_length=6)
    tipo = models.IntegerField()
    achu = models.BigIntegerField()
    zona = models.CharField(max_length=100)
    geom = models.MultiPolygonField(srid=4326) 
