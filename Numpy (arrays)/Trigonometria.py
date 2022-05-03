import numpy as np

# funciones trigonometricas

angulos = np.array([0, 30, 45, 60, 90])

# radianes
angulos_en_radianes = angulos*np.pi/180
#angulos_en_radianes= np.radians(angulos_en_radianes)
print(angulos_en_radianes)

# seno
seno = np.sin(angulos_en_radianes)

# inversa del seno
seno_inverso = np.arcsin(seno)

# Angulos asociados a la inversa de seno.
print(np.degrees(seno_inverso))

# coseno
coseno = np.cos(angulos_en_radianes)

# Inversa del coseno
coseno_inverso = np.arccos(coseno)

# tangente
tangente = np.tan(angulos_en_radianes)

# Inversa de tangente
tangente_inverse = np.arctan(tangente)
