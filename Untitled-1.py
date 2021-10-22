import numpy as np
import matplotlib.pyplot as plt

angulo = [0,2.5,45,67.5,90,112.5,135,157.5,180,202.5,225,247.5,270,270,292.5,315,337.5,360]
potenciarecibida = [-33.2,-34.3,-37.8,-43.3,-55.7,-58.4,-60.1,-60.4,-63.7,-61.9,-52.2,-49.5,-47.8,-47.8,-41.2,-39.2,-34.2,-33.2]
Ganaciarecibida = []
Radianes = []

for Pr in potenciarecibida:
    Gt = Pr - 0.8 - 0 + (20 * np.log10( (4 * np.pi * 2.01 )/ 0.125))
    Ganaciarecibida.append(Gt)
    print(Gt)

for an in angulo:
    Radianes.append(an*(np.pi/180))
    
max_value = None
for num in Ganaciarecibida:
    if (max_value is None or num > max_value):
        max_value = num

normalizado = []

for val in Ganaciarecibida:
    normalizado.append(val-max_value)

fig = plt.figure()
graf = fig.add_subplot(111, projection="polar")
graf.plot(Radianes,normalizado)
graf.set_theta_offset(np.pi/2)
plt.show()

