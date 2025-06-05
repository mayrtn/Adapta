# Traductor de textos para personas con trastornos del lenguaje

**Trabajo Práctico Final – Programación Avanzada – UNAB**

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![POO](https://img.shields.io/badge/Paradigma-POO-informational)

## Descripción del proyecto

Este proyecto consiste en una aplicación de escritorio diseñada para adaptar textos y facilitar su lectura a personas con trastornos del lenguaje. En esta primera versión, el enfoque está puesto en la dislexia. Utilizando técnicas de procesamiento de lenguaje natural, el programa transforma textos comunes en versiones simplificadas que siguen pautas de accesibilidad cognitiva, con el objetivo de mejorar la comprensión lectora.

## Equipo

Trabajo realizado por estudiantes de la Universidad Nacional Guillermo Brown en el marco de la materia Programación Avanzada:

- Artoni Mayra  
- Leandro Terrazas  
- Thomas Sagredo

## Tecnologías y herramientas utilizadas

**Lenguaje:**  
- Python 3.10+

**Librerías:**  
- `nltk` – Natural Language Toolkit (procesamiento del lenguaje natural)  
- `customtkinter` – Interfaz gráfica personalizada basada en Tkinter

## Estructura del proyecto

El proyecto está dividido en los siguientes archivos principales:

- `interfaz.py` → Implementación de la interfaz gráfica con customtkinter  
- `adaptador.py` → Contiene las clases y métodos que procesan y transforman el texto  
- `main.py` → Ejecuta la aplicación y conecta la interfaz con la lógica  
- `requirements.txt` → Lista de dependencias necesarias para instalar y ejecutar el proyecto

## Funcionamiento general

1. El usuario ingresa un texto desde la interfaz gráfica  
2. El sistema procesa ese texto aplicando transformaciones específicas para mejorar su comprensión  
3. El resultado se muestra en pantalla en un formato visualmente accesible

## Estado del desarrollo

- Actualmente en etapa inicial de implementación  
- La primera versión contará con funciones básicas de entrada, procesamiento y salida de texto  

## Escalabilidad y futuras versiones

Este proyecto está diseñado para ser escalable. Entre las futuras mejoras se prevé:

- Inclusión de protocolos de traducción específicos para otros trastornos del lenguaje (afasia, dislalia, etc.)  
- Posibilidad de exportar el texto adaptado en distintos formatos  
- Mejoras en la interfaz gráfica (personalización de estilos, tamaños, fuentes, colores)  
- Desarrollo de una aplicación nativa para dispositivos móviles  
- Incorporación de escaneo y extracción de texto desde imágenes mediante OCR (Reconocimiento Óptico de Caracteres)

## Instalación

1. Cloná el repositorio:

   ```bash
   git clone https://github.com/usuario/proyecto-traductor-dislexia.git
   cd proyecto-traductor-dislexia

2. Instalá las dependencias

   ```bash
   pip install -r requirements.txt

3. Ejecuta

    ```bash
   python main.py
