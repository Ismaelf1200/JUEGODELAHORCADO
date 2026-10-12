Intregrante: Ismael FLores
Juego del ahorcado
# 🎮 Juego del Ahorcado Interactivo (Pygame)

Un clásico juego del ahorcado rediseñado con una interfaz moderna de estilo **Dark UI**, soporte para categorías temáticas, teclado en pantalla interactivo y estadísticas de juego en tiempo real. Desarrollado en Python utilizando la librería **Pygame**.

---

## ✨ Características Principales

* **🎨 Interfaz Dark UI:** Diseño limpio y moderno inspirado en interfaces web actuales (tonos oscuros, bordes redondeados y colores de acento claros).
* **📂 Selector de Categorías:** Juega con palabras aleatorias de diferentes temas (*Tecnología*, *Animales*, *Países*) o selecciona la opción *"Todas"*.
* **⌨️ Doble Entrada (Teclatua y Clic):** Puedes jugar usando tu teclado físico o haciendo clic directamente sobre el teclado virtual en pantalla.
* **📊 Panel de Estadísticas:** Contador persistente de partidas ganadas y perdidas durante la sesión.
* **💡 Sistema de Pistas:** Cada palabra viene acompañada de una breve descripción para facilitar el juego.

---

## 🛠️ Requisitos del Sistema

* **Python** (versión 3.7 o superior recomendada)
* **Pygame**

---

## 📦 Instalación y Configuración

1. **Clona el repositorio o descarga los archivos:**
   ```bash
   git clone [https://github.com/tu-usuario/ahorcado-pygame.git](https://github.com/tu-usuario/ahorcado-pygame.git)
   cd ahorcado-pygame
* Instalar la librería Pygame:
Si no la tienes instalada, puedes hacerlo mediante pip:
   pip install pygame
* 🚀 Cómo Ejecutar el Juego
python main.py
*🕹️ Controles del Juego
#accion: adivinar letra, cambiar categoria, reiniicar partida
# control teclado fisico: teclas de la A a la Z, Tecla Tab, Tecla espacio (al terminar)
control mouse/interfaz clic izquierdo en las teclas virtuales, clic en los botones de categorias superiores, automatico/nueva ronda
📂 Estructura del Código
#El proyecto está organizado de forma orientada a objetos mediante la clase principal HangmanGame, la cual gestiona:

-El estado del juego (victorias, derrotas, intentos fallidos).

-La selección aleatoria de palabras y pistas según la categoría.

-El dibujado dinámico de la horca, los elementos gráficos y la interfaz de usuario.

-La detección de eventos (clics y pulsaciones de teclas).
🤝 Contribuciones
#¡Las contribuciones son bienvenidas! Si deseas agregar nuevas palabras, categorías o mejoras visuales:

-Haz un Fork del proyecto.

-Crea una rama para tu nueva característica (git checkout -b feature/nueva-caracteristica).

-Realiza tus cambios y haz commit (git commit -m 'Agregada nueva categoría de ciencia').

-Sube tus cambios (git push origin feature/nueva-caracteristica).

-Abre un Pull Request.
#**📄 Licencia
Este proyecto está bajo la Licencia MIT. Siéntete libre de usarlo, modificarlo y compartirlo.
