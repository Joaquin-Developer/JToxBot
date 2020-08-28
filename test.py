# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
 
# Parseamos los parametros desde linea de comandos
# para almacenar codigos QR en un archivo
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
	help="Nombre del archivo CSV para almacenar los codigos escaneados")
args = vars(ap.parse_args())

# Inicializamos el stream de video
# y dejamos que la camara haga warm-up
print("[INFO] starting video stream...")
# vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
 
# Abrimos el archivo CSV para almacenar los string decodificados
csv = open(args["output"], "w")
found = set()

# Iteramos sobre los frames de video de la camara
while True:
	# Aplicamos resize sobre el frame de video
	# para que sea mas agil su procesamiento
	frame = vs.read()
	frame = imutils.resize(frame, width=600)
 
	# Decodificamos los QR o Barcodes del frame de video
	barcodes = pyzbar.decode(frame)

	# Iteramos sobre los codigos decodigicados
	for barcode in barcodes:
		# Extraemos la posicion del codigo en el frame
		# y dibujamos un recuadro sobre el codigo en el frame
		(x, y, w, h) = barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
		# Convertimos el codigo decodificado a string
		# y tambien extraemos el tipo de codigo (QR o Barcode)
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type
 
		# Dibujamos el string decodificado y el tipo de codigo
		# sobre el frame de video
		text = "{} ({})".format(barcodeData, barcodeType)
		cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
 
		# En caso que el codigo decodificado no este
		# en el archivo CSV, lo almacenamos junto a una
		# marca de tiempo
		if barcodeData not in found:
			csv.write("{},{}\n".format(datetime.datetime.now(),
				barcodeData))
			csv.flush()
			found.add(barcodeData)
		# Dibujamos en pantalla el frame de video
		# con los agregados
	cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# Capturamos la tecla Q para cortar la ejecucion
	if key == ord("q"):
		break
 
# Cerramos el CSV y liberamos recursos
print("[INFO] Saliendo")
csv.close()
cv2.destroyAllWindows()
vs.stop()