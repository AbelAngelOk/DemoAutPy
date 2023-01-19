@echo off
echo
cd ".\src\test"
echo EL REPORTE SE GUARDARA EN ./src/allure-results/{una_carpeta}
echo  POR FAVOR, INGRESE UN NOMBRE A LA CARPETA EL REPORTE.
set/p carpeta= 
echo EJECUTANDO PRUEBAS...
python -m pytest --alluredir "..\allure-results\%carpeta%"
pause