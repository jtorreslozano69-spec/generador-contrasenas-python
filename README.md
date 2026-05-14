# Generador de Contraseñas con Hashing Profesional

Este proyecto es una herramienta de seguridad desarrollada en Python. No solo genera una contraseña aleatoria y segura, sino que también utiliza técnicas de encriptación moderna (**Hashing**) para demostrar cómo se protegen las credenciales en aplicaciones del mundo real.

**Generación Aleatoria:** Mezcla de letras, números y símbolos para máxima seguridad.
**Seguridad con Werkzeug:** Implementa el método `generate_password_hash` para convertir la clave en un código cifrado irreversible.
**Validación de Errores:** Evita cierres inesperados mediante bloques `try-except`.
**Ligero y Rápido:** Ejecución directa desde la terminal.

### 🛠️ Tecnologías Utilizadas
**Python 3.10+**
**Librería Werkzeug:** Para el manejo de seguridad y hashes.
**Módulos Nativos:** `random` y `string`.

### Instalación y Configuración

Si es la primera vez que lo usas, sigue estos pasos en tu terminal para evitar el error de "ModuleNotFoundError":

1. **Clonar el proyecto:**
   ```bash
   git clone [https://github.com/jtorreslozano69-spec/generador-contrasenas-python](https://github.com/jtorreslozano69-spec/generador-contrasenas-python)
   
2. **Como instalar la libreria:**
   ```bash
   pip install werkzeug
   
4. **Ejecutar el generador:**
   ```bash
   python generador-contraseña.py
