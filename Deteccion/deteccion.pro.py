import pandas as pd
import numpy as np
import os # <--- Importamos esto para manejar carpetas

# --- CONFIGURACIÓN DE CARPETAS ---
# Creamos la carpeta 'Resultados' si no existe
if not os.path.exists('Resultados'):
    os.makedirs('Resultados')

# 1. CARGA DE DATOS
data = pd.read_excel('Epidural.xlsx', decimal=',')
filas_iniciales = len(data)

# 2. LIMPIEZA Y CONVERSIÓN
data['edad'] = pd.to_numeric(data['edad'], errors='coerce')
data['TEMP1'] = pd.to_numeric(data['TEMP1'], errors='coerce')
data['TEMP2'] = pd.to_numeric(data['TEMP2'], errors='coerce')
data['DILATACI'] = pd.to_numeric(data['DILATACI'], errors='coerce')

data = data.dropna(subset=['edad', 'TEMP1', 'TEMP2'])
data['edad'] = data['edad'].astype(int)

filas_borradas = filas_iniciales - len(data)
print(f"ATENCIÓN: Se han borrado {filas_borradas} filas por datos inválidos")
print("="*80)

# 3. PROCESAMIENTO ANALÍTICO
data["edad_recodificada"] = pd.cut(data['edad'], bins=[-float('inf'), 24, 25, float('inf')], 
labels=['por debajo', 'por igual', 'por encima']) 

data["TEMP_MEDIA"] = data[['TEMP1', 'TEMP2']].mean(axis=1)
data['TEMP_MEDIA'] = pd.to_numeric(data['TEMP_MEDIA'], errors='coerce')
data['ALERTA_FIEBRE'] = (data['TEMP_MEDIA'] >= 38).astype(int)

# 4. REGRESIÓN Y TENDENCIA
x = data['DILATACI'].fillna(0)
y = data['TEMP2'].fillna(data['TEMP2'].mean())
m, b = np.polyfit(x, y, 1)
data['Tendencia_Regresion'] = (m * x) + b
data['Indice_Correlacion'] = x.corr(y)

# 5. ESTADÍSTICAS PARA TERMINAL
promedio_edad = data['edad'].mean()
promedio_temp = data['TEMP_MEDIA'].mean()
casos_fiebre = len(data[data['TEMP_MEDIA'] >= 38])

print(f"Edad promedio: {promedio_edad:.1f} años")
print(f"Temperatura media: {promedio_temp:.2f} °C")
print(f"Hallazgo: Se detectaron {casos_fiebre} casos con fiebre (>= 38°C)")
print("-" * 30)

# 6. ESTILOS Y GUARDADO EN CARPETA 'Resultados'
def color_rojo(val):
    return 'background-color: red; color: white' if val == 1 else ''

# Aplicamos los colores
estilo = data.style.map(lambda x: 'background-color: yellow', subset=['edad_recodificada', 'TEMP_MEDIA'])
estilo = estilo.map(color_rojo, subset=['ALERTA_FIEBRE'])

# --- CAMBIO CLAVE AQUÍ: Guardamos dentro de la carpeta Resultados ---
ruta_guardado = 'Resultados/Resultado_Epidural.xlsx'
estilo.to_excel(ruta_guardado, engine='openpyxl', index=False)

# 7. RESUMEN FINAL
total_pacientes = len(data)
porcentaje_fiebre = (casos_fiebre / total_pacientes) * 100

print(f"RESUMEN DEL PROCESAMIENTO:")
print(f"- Total de pacientes analizadas: {total_pacientes}")
print(f"- Porcentaje con alerta de fiebre: {porcentaje_fiebre:.1f}%")
print(f"- Estado de la base: {'⚠️ REVISAR' if porcentaje_fiebre > 10 else '✅ ESTABLE'}")

print("="*80)
print(f"✅ ¡PROCESO TERMINADO!")
print(f"Archivo guardado en: {ruta_guardado}")
print("="*80)