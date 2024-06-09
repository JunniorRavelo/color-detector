# Real-time Color Detection

This project, created by Jr Santiago Ravelo, uses Flask and OpenCV to detect colors in real-time through the webcam. The software detects various colors in a video stream and draws rectangles around the detected objects, labeling them with their corresponding color.

## Note about Language

- 'main' : English
- 'spanish' : Spanish

## Requirements

- Python 3.x
- Flask
- OpenCV
- NumPy

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/JunniorRavelo/color-detector.git
    cd color-detector
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv env_colors
    ```

3. **Activate the virtual environment:**

    - On Windows:
        ```sh
        .\env_colors\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source env_colors/bin/activate
        ```

4. **Install the dependencies:**

    Make sure you have a `requirements.txt` file with the following dependencies:

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

    Then, install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Web Version

1. **Run the Flask application:**

    ```sh
    python app.py
    ```

2. **Open your web browser and go to `http://0.0.0.0:5000` to see the real-time color detection.**

### Desktop Version

For the desktop version, it's located in desktop\desktop.py, which does not use Flask.