@echo off
echo INGRESE LA RUTA ABSOLUTA DEL REPORTE ENTRE COMILLAS
set/p ruta=Ruta:
echo ruta ingresada: %ruta%
allure serve %ruta%