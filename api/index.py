import os
import sys

# Agrega la ruta de la aplicación al path de sistema para que Vercel encuentre los módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from combomaker import create_app

app = create_app()
