# Chat Cliente-Servidor con Sockets TCP 🐍🌐

## Descripción

Este proyecto consiste en la implementación de una arquitectura **Cliente-Servidor** básica utilizando la librería `socket` de Python. Fue desarrollado como parte del **Trabajo Práctico N.º 7** para la materia **Redes de Computadoras** en la **Universidad Nacional de Hurlingham (UNAHUR)**.

El objetivo principal fue comprender el funcionamiento de los sockets, la asignación de puertos y la verificación de estados de conexión en el sistema operativo mediante herramientas de diagnóstico.

---

## 🛠️ Tecnologías y Herramientas

* **Lenguaje:** Python 3.x
* **Protocolo de Transporte:** TCP (Stream Sockets)
* **Herramientas de diagnóstico:** Comando `netstat` de Windows/PowerShell

---

## 🚀 Cómo ejecutar el proyecto

Para probar la comunicación, seguí estos pasos en dos terminales diferentes:

### 1. Iniciar el Servidor

```bash
python servidor.py
```

El servidor quedará en estado **LISTENING** en el puerto `7777`.

### 2. Iniciar el Cliente

```bash
python cliente.py
```

Una vez conectado, podrás enviar mensajes al servidor. Para finalizar, podés cerrar la conexión enviando el mensaje `quit`.

---

## 📊 Análisis de Red (Networking Insights)

Durante la actividad, se utilizó `netstat -ano` para auditar la tabla de conexiones y comparar los estados con y sin conexión activa.

**Resultados del análisis:**

* **Estado LISTENING:** El servidor reserva el puerto 7777 y queda a la espera de peticiones.
* **Estado ESTABLISHED:** Se confirma la conexión cuando el cliente se vincula exitosamente al puerto del servidor (ej: puerto remoto 59475).

---

## 🎓 Contexto Académico

**Institución:** Universidad Nacional de Hurlingham (UNAHUR)  
**Materia:** Redes de Computadoras  
**Trabajo Práctico:** N.º 7  
**Autor:** Sebastián Castignani
