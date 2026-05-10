# 🏢 Software FJ - Sistema de Gestión de Reservas 🚀

¡Hola! Bienvenido al repositorio de nuestro proyecto para la **Fase 4: Prácticas Simuladas** del curso de Programación (213023) de la UNAD. 🎓

## 📝 Descripción del Proyecto
Este es un sistema integral orientado a objetos diseñado para gestionar clientes, servicios y reservas de la empresa **Software FJ** (reservas de salas, alquiler de equipos y asesorías). 

El objetivo principal de este sistema es demostrar estabilidad y robustez. **No utiliza bases de datos**, toda la información se maneja en memoria mediante listas internas y objetos. Además, cuenta con un sistema de registro de eventos (`logs.txt`) y un manejo avanzado de excepciones.

## ✨ Características Principales
- **Arquitectura Modular:** El código está dividido en múltiples archivos lógicos para facilitar su mantenimiento.
- **POO Avanzada:** Implementación estricta de Abstracción, Herencia, Polimorfismo y Encapsulación.
- **Tipado Estricto (Type Hinting):** Uso de la librería `typing` de Python para asegurar la integridad de los datos.
- **Sobrecarga de Métodos:** Simulación de sobrecarga utilizando parámetros opcionales (`Optional`).
- **Manejo de Excepciones a Prueba de Fallos:** Uso intensivo de bloques `try/except/else/finally`, excepciones personalizadas y encadenamiento de errores (`raise from`).

## 📂 Estructura del Código
El sistema está dividido en los siguientes módulos:
* `main.py`: Archivo principal que orquesta y simula las 10 operaciones de prueba.
* `sistema.py`: Administra las listas internas de clientes y reservas.
* `entidades.py`: Define la clase abstracta base.
* `clientes.py`: Contiene la lógica del cliente con validaciones y encapsulamiento.
* `servicios.py`: Contiene la clase abstracta de servicio y sus clases hijas (Sala, Equipo, Asesoría).
* `reservas.py`: Conecta clientes con servicios y procesa el cálculo de costos.
* `excepciones.py`: Define los errores personalizados del sistema.
* `gestion_logs.py`: Se encarga de escribir el historial de eventos en el archivo de texto.

## 🚀 Cómo ejecutar el proyecto
1. Asegúrate de tener **Python 3** instalado en tu computadora.
2. Clona este repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/fase-4-practica-simulada.git
   ```
3. Abre una terminal en la carpeta del proyecto y ejecuta el simulador:
   ```bash
   python main.py
   ```
4. Revisa el archivo generado `logs.txt` para ver el registro de eventos y errores capturados.

## 👥 Equipo de Desarrollo (Grupo 213023_403)
* Sindy Grisela Bedoya Camargo
* Majurehy Lilian Coy Ruiz
* Juan Andres Salazar Beltran

---
*Proyecto desarrollado con fines académicos para la Universidad Nacional Abierta y a Distancia (UNAD).*
