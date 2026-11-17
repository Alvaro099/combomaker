# Combo Maker 🕹️

Combo Maker es una suite web visual e interactiva diseñada para la **Fighting Game Community (FGC)**. Permite a jugadores, creadores de contenido, organizadores de torneos y casters generar, editar, personalizar y compartir secuencias de combos con la **iconografía gráfica oficial** de las franquicias más populares de juegos de pelea.

---

## 🎮 Franquicias y Juegos Soportados (9 Teclados)

- 🥊 **Street Fighter 6 (SF6):** Layout clásico de 6 botones (LP, MP, HP / LK, MK, HK) y comandos del Drive System (Impact, Parry, Rush).
- ⚡ **Tekken 8 (T8):** Esquema de 4 extremidades (1, 2, 3, 4), pulsaciones simultáneas (`1+2`, `3+4`, `1+4`) y mecánicas de Heat System.
- 💥 **2XKO:** Notación oficial del tag fighter de Riot: Light, Medium, Heavy, Special 1, Special 2 y mecánicas de Tag / Assist.
- 🎸 **Guilty Gear -Strive- (GGST):** Disposición de anime fighter con iconos para Punch (P), Kick (K), Slash (S), Heavy Slash (HS) y Dust (D).
- 🐉 **Dragon Ball FighterZ (DBFZ):** Inputs de Light, Medium, Heavy, Special, Super Dash, Dragon Rush y Follow-up.
- 👑 **The King of Fighters XV (KOF XV):** Cuadrante arcade clásico de 4 botones (A, B, C, D) y Blowback.
- 🐺 **Fatal Fury: City of the Wolves:** Botones A, B, C, D junto al sistema REV (REV Arts, REV Blow y REV Guard).
- ⚔️ **Anime Fighting Games (Universal):** Iconografía A, B, C, D para BlazBlue, Under Night In-Birth, Melty Blood y airdashers.
- 🔢 **Notación Genérica (NumPad):** Teclado numérico direccional 1-9 tradicional y botones universales P/K.

---

## ✨ Novedades y Características Principales

### 🏷️ Ficha de Combo Personalizable (Metadatos para Streamers y Guías)
- Despliega el panel **"Personalizar Ficha de Combo"** para incluir:
  - **Personaje:** (ej. *Luke*, *Reina*, *Sol Badguy*).
  - **Título / Situación:** (ej. *Optimal Corner Carry*, *Punish Counter 2-Bar*).
  - **Daño / Costo de Recursos:** (ej. *4,850 DMG • 2 Drive Bars*).
- Los metadatos se renderizan en una cabecera estilizada directamente dentro del canvas y se integran en la imagen exportada.

### 📋 Copiar PNG Directo al Portapapeles (1-Clic para Discord y X)
- Gracias a la **Clipboard API**, el botón **"📋 Copiar PNG"** genera la imagen en memoria y la deposita en tu portapapeles.
- Puedes pegarla al instante con `Ctrl+V` en Discord, Twitter/X, Reddit o WhatsApp Web sin llenar tu disco duro de descargas.

### 🧩 Edición No Lineal con Chips Interactivos
- Cada input dentro del canvas es un **chip interactivo independiente**.
- Al pasar el cursor por encima, se resalta y muestra un botón `×`. **Haz clic en cualquier token intermedio para borrar solo ese golpe** sin tener que reiniciar ni borrar toda la secuencia posterior.

### ↶ Pila de Historial y Deshacer (`Ctrl+Z`)
- Historial en memoria de hasta 40 acciones.
- Soporta el atajo universal **`Ctrl+Z`** (o `Cmd+Z`) en cualquier momento para deshacer borrados accidentales o modificaciones.
- **Prevención de pérdida de datos:** Si pulsas "Limpiar todo" en un combo de más de 4 inputs, se solicita confirmación y se puede deshacer con `Ctrl+Z`.

### ⌨️ Atajos de Teclado Físico (Notación NumPad 1 al 9)
- Introduce direcciones usando el teclado numérico de tu PC o laptop:
  - `1` = ↙ (Abajo-Atrás) | `2` = ↓ (Abajo) | `3` = ↘ (Abajo-Adelante)
  - `4` = ← (Atrás) | `5` = Neutral | `6` = → (Adelante)
  - `7` = ↖ (Arriba-Atrás) | `8` = ↑ (Arriba) | `9` = ↗ (Arriba-Adelante)
  - *Ejemplo:* Presiona `2`, `3`, `6` para ingresar un cuarto de círculo (*Hadoken*) en segundos.
  - `Backspace`: Borra el último input añadido.

### 🎨 Diseño "Arcade Fightstick HUD" (WCAG AA)
- Estética oscura de torneo (`#0B0E14` / `#121722`), tipografía arcade display `Bebas Neue` combinada con `IBM Plex Mono`.
- Disposición de botones ergonómica basada en mandos y arcade sticks reales (filas de puñetazos sobre patadas en SF6).
- Contraste riguroso accesible (certificación `impeccable detect` con 0 advertencias).
- Favicon SVG de palanca arcade y metadatos sociales Open Graph para previsualizaciones en redes.
- Pantalla temática de error 404 (*"ROUND LOST — K.O."*).

---

## 🚀 Guía Rápida de Uso

1. **Selecciona un juego:** En la portada del sitio o en el menú superior, elige tu franquicia de pelea preferida.
2. **Arma tu secuencia:** Haz clic en los botones en pantalla o utiliza tu teclado numérico físico (`1` al `9`).
3. **Corrige o afina:**
   - Haz clic sobre cualquier botón en el canvas para eliminarlo individualmente.
   - Pulsa `Ctrl+Z` si te equivocas o `Backspace` para borrar el último golpe.
4. **Personaliza (Opcional):** Abre el menú `🏷️ Personalizar Ficha de Combo` para añadir personaje, daño y título.
5. **Comparte:**
   - Haz clic en **"📋 Copiar PNG"** para pegarlo directamente en tu chat o red social.
   - O haz clic en **"⭳ Descargar PNG"** para guardarlo como archivo `combo.png`.

---

## 🛠️ Instalación y Desarrollo Local

Requiere **Python 3.10+** y `pip`.

1. **Clonar el repositorio:**
   ```bash
   git clone <tu-repo-url>
   cd combomaker
   ```

2. **Crear y activar un entorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv .venv
   
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el servidor local:**
   ```bash
   python run.py
   ```
   Abre [http://127.0.0.1:5000/](http://127.0.0.1:5000/) en tu navegador.

---

## ☁️ Despliegue en Vercel

Configurado para arquitectura Serverless en Vercel:

1. Conecta tu repositorio de GitHub en el panel de Vercel.
2. Selecciona **"Other"** como Framework Preset.
3. Vercel detectará automáticamente `vercel.json` y desplegará la función en `@vercel/python` a través de `api/index.py`.

---

## 📁 Estructura del Proyecto

```
combomaker/
├── api/
│   └── index.py            # Entrypoint serverless para Vercel
├── combomaker/
│   ├── static/             # PNGs y WebP oficiales clasificados por franquicia
│   ├── templates/          # Plantillas HTML/Jinja2 (base, home, 404 y combos_*.html)
│   ├── __init__.py         # App factory y manejador de error 404
│   └── home.py             # Diccionarios de inputs y rutas de los 9 juegos
├── .gitignore              # Reglas de exclusión Git (incluye carpetas de agentes IA)
├── DESIGN.md               # Sistema visual normativo (Arcade Fightstick HUD)
├── PRODUCT.md              # Contexto duradero y principios de producto
├── README.md               # Documentación y manual de uso
├── requirements.txt        # Dependencias Python (Flask, Werkzeug)
├── run.py                  # Servidor de desarrollo local
└── vercel.json             # Configuración de despliegue en Vercel
```

---

## ⚖️ Licencia y Uso Justo (Fair Use)

Este proyecto es una herramienta comunitaria sin fines de lucro desarrollada por **Alvaro Bustos**. 
Los assets e iconos de botones pertenecen a sus respectivos creadores y titulares de derechos de autor (Capcom, Bandai Namco, SNK, Arc System Works, Riot Games). Se utilizan bajo la doctrina de **Uso Legítimo (Fair Use)** con fines educativos, de documentación y de apoyo a la comunidad competitiva.
