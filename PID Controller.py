# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import control
# from control import TransferFunction, tf, feedback, pid , step_response

# Definimos el modelo del sistema (en este caso, un sistema de primer orden)
num = [1]
den = [1, 1]  # Sistema de primer orden
system_tf = control.TransferFunction(num, den)

# Diseñamos el controlador PID con los parámetros deseados
Kp = 2.0
Ki = 5.0
Kd = 0.05
controller = control.tf([Kd, Kp, Ki], [1, 0])

# Conectamos el controlador al sistema y obtenemos el sistema en lazo cerrado
system_closed_loop = control.feedback(system_tf * controller, 1)

# Generamos una señal de referencia constante y calculamos la respuesta del sistema en lazo cerrado
t = np.linspace(0, 10, 1000)
r = np.ones_like(t)  # Señal de referencia constante
t_out, y_out = control.step_response(system_closed_loop, T=t)

# Visualizamos los resultados
plt.plot(t_out, r, 'r--', label='Referencia')
plt.plot(t_out, y_out, 'b-', label='Salida')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.legend()
plt.grid()
plt.show()