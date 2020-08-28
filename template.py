#Importamos librerias
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import os




# Inicializamos el stream de video, y esperamos 2 segundos para
# que la camara haga warm-up
print("Capturando stream de video. Presione Q para salir")
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
 

# Iteramos sobre los frames de video de la camara
while True:

	# Capturamos el frame y le aplicamos resize a
	# un ancho de 600 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=600)

	# Buscamos Codigos de barra/QR en el frame de video
	barcodes = pyzbar.decode(frame)

	# Iteramos sobre los codigos de barra/QR encontrados en el frame
	for barcode in barcodes:

		# Decodificamos el codigo, y extraemos el string en formato UTF-8.
		barcodeText = barcode.data.decode("utf-8")

		# ------------------------------------------
		# Espacio para codigo extra
		# ------------------------------------------




		# ------------------------------------------
		# Fin del espacio para codigo extra
		# ------------------------------------------

		# Dibujamos el cuadro completo en pantalla

	key = cv2.waitKey(1) & 0xFF

	# Si se presiona la tecla "Q", cortamos el loop y salimos
	if key == ord("q"):
		break
 
#Liberamos recursos
print("Liberando recursos")
csv.close()
cv2.destroyAllWindows()
vs.stop()