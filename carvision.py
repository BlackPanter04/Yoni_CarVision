import serial
import time
import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

# Configura la conexión serial con Arduino
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)  # Cambia 'COM3' por el puerto serial correcto

def send_motor_control(speed, direction):
    control_data = f"{speed} {direction}\n"  # Velocidad y dirección separados por un espacio
    arduino.write(control_data.encode())      # Enviar la información al Arduino
    time.sleep(0.05)

azulBajo = np.array([90, 100, 20], np.uint8)
azulAlto = np.array([120, 255, 255], np.uint8)
                    
while True:
    ret,frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    speed =  150
    direction = 1 # Dirección del motor
    
    if speed.isdigit() and direction in ['0', '1']:
        send_motor_control(speed, direction)
    else:
        print("Introduce valores válidos para la velocidad y dirección.")

# cv2.imshow('mascaraAzul', mascara)
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('s'):
        arduino.close()
        break

cap.release()
cv.destroyAllWindows()
