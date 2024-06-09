# Detección de Colores en Tiempo Real

Este proyecto, creado por Jr Santiago Ravelo, utiliza Flask y OpenCV para detectar colores en tiempo real a través de la cámara web. El software detecta varios colores en un flujo de video y dibuja rectángulos alrededor de los objetos detectados, etiquetándolos con su color correspondiente.

## Requisitos

- Python 3.x
- Flask
- OpenCV
- NumPy

## Instalación

1. **Clona el repositorio:**

    ```sh
    git clone <https://github.com/JunniorRavelo/color-detector.git>
    cd <color-detector>
    ```

2. **Crea un entorno virtual:**

    ```sh
    python -m venv env_colors
    ```

3. **Activa el entorno virtual:**

    - En Windows:
        ```sh
        .\env_colors\Scripts\activate
        ```
    - En macOS y Linux:
        ```sh
        source env_colors/bin/activate
        ```

4. **Instala las dependencias:**

    Asegúrate de tener un archivo `requirements.txt` con las siguientes dependencias:

    ```txt
    blinker==1.8.2
    click==8.1.7
    colorama==0.4.6
    Flask==3.0.3
    itsdangerous==2.2.0
    Jinja2==3.1.4
    MarkupSafe==2.1.5
    numpy==1.26.4
    opencv-python==4.10.0.82
    Werkzeug==3.0.3
    ```

    Luego, instala las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

## Uso

### Versión Web

1. **Ejecuta la aplicación Flask:**

    ```sh
    python app.py
    ```

2. **Abre tu navegador web y ve a `http://0.0.0.0:5000` para ver la detección de colores en tiempo real.**

### Versión de Escritorio

Para la versión de escritorio, se encuentra en desktop\desktop.py la cual no usa flask.

