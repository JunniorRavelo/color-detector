import cv2
import numpy as np

# Definir rangos de colores en HSV y los colores que deseas que detecte
colores = {
    "Rojo": ([0, 100, 100], [10, 255, 255]),            
    "Rojo": ([160, 100, 100], [180, 255, 255]),        
    "Naranja": ([10, 100, 100], [20, 255, 255]),       
    "Amarillo": ([15, 100, 100], [35, 255, 255]),      
    "Verde": ([40, 100, 100], [80, 255, 255]),         
    "Azul": ([90, 100, 100], [130, 255, 255]),          
    "Violeta": ([120, 100, 100], [160, 255, 255])
    #,"Blanco": ([0, 0, 200], [180, 20, 255]),            
    #"Negro": ([0, 0, 0], [180, 255, 30])              
}

# Rango de colores opcionales
mas_colores = {
    "Rojo": ([0, 100, 100], [10, 255, 255]),
    "Rojo oscuro": ([0, 50, 50], [10, 255, 255]),
    "Rojo claro": ([0, 100, 100], [10, 200, 255]),
    "Rojo pálido": ([0, 50, 100], [10, 150, 255]),
    "Azul": ([100, 100, 100], [130, 255, 255]),
    "Azul oscuro": ([100, 50, 50], [130, 255, 255]),
    "Azul claro": ([100, 100, 100], [130, 200, 255]),
    "Azul pálido": ([100, 50, 100], [130, 150, 255]),
    "Amarillo": ([20, 100, 100], [30, 255, 255]),
    "Amarillo oscuro": ([20, 50, 50], [30, 255, 255]),
    "Amarillo claro": ([20, 100, 100], [30, 200, 255]),
    "Amarillo pálido": ([20, 50, 100], [30, 150, 255]),
    "Verde": ([50, 100, 100], [70, 255, 255]),
    "Verde oscuro": ([50, 50, 50], [70, 255, 255]),
    "Verde claro": ([50, 100, 100], [70, 200, 255]),
    "Verde pálido": ([50, 50, 100], [70, 150, 255]),
    "Naranja": ([10, 100, 100], [20, 255, 255]),
    "Naranja oscuro": ([10, 50, 50], [20, 255, 255]),
    "Naranja claro": ([10, 100, 100], [20, 200, 255]),
    "Naranja pálido": ([10, 50, 100], [20, 150, 255]),
    "Violeta": ([130, 100, 100], [160, 255, 255]),
    "Violeta oscuro": ([130, 50, 50], [160, 255, 255]),
    "Violeta claro": ([130, 100, 100], [160, 200, 255]),
    "Violeta pálido": ([130, 50, 100], [160, 150, 255]),
    "Amarillo anaranjado": ([15, 100, 100], [25, 255, 255]),
    "Amarillo anaranjado oscuro": ([15, 50, 50], [25, 255, 255]),
    "Amarillo anaranjado claro": ([15, 100, 100], [25, 200, 255]),
    "Amarillo anaranjado pálido": ([15, 50, 100], [25, 150, 255]),
    "Rojo anaranjado": ([5, 100, 100], [15, 255, 255]),
    "Rojo anaranjado oscuro": ([5, 50, 50], [15, 255, 255]),
    "Rojo anaranjado claro": ([5, 100, 100], [15, 200, 255]),
    "Rojo anaranjado pálido": ([5, 50, 100], [15, 150, 255]),
    "Rojo violeta": ([160, 100, 100], [180, 255, 255]),
    "Rojo violeta oscuro": ([160, 50, 50], [180, 255, 255]),
    "Rojo violeta claro": ([160, 100, 100], [180, 200, 255]),
    "Rojo violeta pálido": ([160, 50, 100], [180, 150, 255]),
    "Azul violeta": ([130, 100, 100], [145, 255, 255]),
    "Azul violeta oscuro": ([130, 50, 50], [145, 255, 255]),
    "Azul violeta claro": ([130, 100, 100], [145, 200, 255]),
    "Azul violeta pálido": ([130, 50, 100], [145, 150, 255]),
    "Azul verdoso": ([80, 100, 100], [100, 255, 255]),
    "Azul verdoso oscuro": ([80, 50, 50], [100, 255, 255]),
    "Azul verdoso claro": ([80, 100, 100], [100, 200, 255]),
    "Azul verdoso pálido": ([80, 50, 100], [100, 150, 255]),
    "Amarillo verdoso": ([25, 100, 100], [35, 255, 255]),
    "Amarillo verdoso oscuro": ([25, 50, 50], [35, 255, 255]),
    "Amarillo verdoso claro": ([25, 100, 100], [35, 200, 255]),
    "Amarillo verdoso pálido": ([25, 50, 100], [35, 150, 255]),
    "Blanco": ([0, 0, 200], [180, 20, 255]),
    "Blanco oscuro": ([0, 0, 100], [180, 20, 255]),
    "Blanco claro": ([0, 0, 200], [180, 20, 200]),
    "Blanco pálido": ([0, 0, 100], [180, 20, 200]),
    "Negro": ([0, 0, 0], [180, 255, 30]),
    "Negro oscuro": ([0, 0, 0], [180, 255, 100]),
    "Negro claro": ([0, 0, 0], [180, 255, 200]),
    "Negro pálido": ([0, 0, 0], [180, 255, 150]),
}

# Iniciar la captura de video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Leer frame de la cámara
    if not ret:
        break

    # Convertir frame de BGR a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color, (lower, upper) in colores.items():
        lower = np.array(lower, dtype=np.uint8)  # Límite inferior del color
        upper = np.array(upper, dtype=np.uint8)  # Límite superior del color
        mask = cv2.inRange(hsv, lower, upper)    # Crear máscara para el color

        # Encontrar contornos en la máscara
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:  # Filtrar pequeños contornos por área
                x, y, w, h = cv2.boundingRect(contour)
                # Dibujar rectángulo alrededor del objeto detectado
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
                # Poner texto con el nombre del color detectado
                cv2.putText(frame, color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    # Mostrar el frame con detección de colores
    cv2.imshow("Detección de Color", frame)

    # Salir del loop si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()