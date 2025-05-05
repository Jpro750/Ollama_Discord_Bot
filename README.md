# Ollama Discord Bot

## Descripción
Bot de Discord que utiliza Ollama para integrar un modelo de lenguaje grande (LLM) y responder a tus mensajes de forma inteligente.

## Prerrequisitos
- Python 3.8 o superior
- Cuenta y acceso al CLI de Ollama
- Bot de Discord y token de aplicación

## Instalación

1. **Instalar Ollama**
   - Descarga e instala Ollama desde https://ollama.com/ siguiendo las instrucciones para tu sistema operativo.

2. **Descargar un modelo**
   - En la terminal, ejecuta:
     ```
     ollama pull <nombre-del-modelo>
     ```
     para descargar el modelo que desees.

3. **Instalar dependencias**
   ```bash
   pip install ollama discord.py
   ```

## Configuración

1. **Especificar el modelo**
   - Abre `functions.py` y modifica la línea:
     ```python
     model = "<nombre-del-modelo>"
     ```
     reemplazando `<nombre-del-modelo>` por el nombre del modelo descargado.

2. **Configurar el token de Discord**
   - Accede al [Portal de Desarrolladores de Discord](https://discord.com/developers/applications).
   - Selecciona tu aplicación, ve a **Bot** y copia el **Token**.
   - en bot.run("") pon tu bot token

## Uso

- Para iniciar el bot, ejecuta:
  ```bash
  python bot.py
  ```

- Invita el bot a tu servidor usando la URL de OAuth2 generada en el portal de desarrolladores de Discord.

## Contribuciones

¡Contribuciones bienvenidas! Si deseas colaborar:

1. Abre un **issue** para discutir cambios.
2. Crea un **pull request** con tus mejoras.

## Licencia

Este proyecto está bajo la licencia MIT.
