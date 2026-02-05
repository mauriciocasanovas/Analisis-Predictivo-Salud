======================================================================================
ANALISIS PREDICTIVO DE SALUD - DETECCION EPIDURAL
======================================================================================

DESCRIPCION:
Este proyecto nace de la necesidad de transformar datos clinicos complejos 
en informacion visual accionable. Desarrolle una herramienta que procesa 
registros medicos (como temperaturas y niveles de dilatacion) para 
identificar automaticamente pacientes en riesgo, permitiendo una 
intervencion medica mas rapida. Utiliza tecnicas de analisis predictivo 
para asistir en el diagnostico y monitoreo de condiciones epidurales, 
combinando el poder de procesamiento de Python con la capacidad visual 
de Power BI para ofrecer un tablero de control de alta precision.

ESTRUCTURA DEL PROYECTO:

1. Epidural.xlsx (Base de Datos):
   Archivo de origen que contiene los datos clinicos, parametros medicos 
   y registros de pacientes necesarios para el analisis.

2. deteccion.pro.py (Script de Procesamiento):
   Motor de calculo encargado del ciclo de vida del dato medico:
   - Limpieza y normalizacion de registros clinicos.
   - Recodificacion de variables de edad y analisis de temperatura media.
   - Aplicacion de modelos de regresion para detectar tendencias de dilatacion.
   - Generacion automatica de alertas de fiebre mediante formato condicional.

3. Reporte_Epidural.pbix (Dashboard):
   Tablero interactivo en Power BI que consume los resultados procesados. 
   Permite visualizar tendencias de salud, alertas de riesgo y 
   distribucion de casos de forma grafica y profesional.

4. Carpeta Resultados:
   - Resultado_Epidural.xlsx: Archivo exportado con indicadores resaltados y 
     mapa de calor aplicado a las variables de riesgo.
   
TECNOLOGIAS UTILIZADAS:
- Python 3.x (Motor de procesamiento y analitica)
- Pandas & NumPy (Limpieza de registros y calculo estadistico)
- Power BI Desktop (Visualizacion de datos / Healthcare Analytics)
- Excel / Openpyxl (Persistencia de datos y estilizado de reportes)

VALOR AGREGADO:
- Integracion del Stack Tecnologico: Uso de Python para el backend de datos 
  y Power BI para el storytelling visual, facilitando la toma de decisiones.
- Analisis Preventivo: Identificacion automatica de patrones de riesgo (fiebre 
  y correlacion de temperatura) antes de complicaciones clinicas.
- Reportabilidad Profesional: Entrega de reportes estilizados directamente 
  desde el codigo, optimizando el tiempo de interpretacion medica.

======================================================================================