# 🚀 Plataforma de Gestión de Transacciones (Entorno Local)

Este documento detalla los pasos para levantar el entorno de desarrollo local utilizando Docker. 
La infraestructura está diseñada para funcionar bajo una estructura unificada, 
donde los repositorios independientes de frontend y backend conviven en una misma carpeta raíz 
y son orquestados por un único archivo `docker-compose.yml`.

## 🛠️ Prerrequisitos

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) (o Docker Engine con Docker Compose).
* Git.
* Python 3.12+ (Para el bot RPA).

---

## ⚙️ Instrucciones de Instalación

### 1. Preparar el espacio de trabajo (Root Folder)
Crea la carpeta principal que contendrá todo el ecosistema y entra en ella:

```bash
mkdir transacciones
cd transacciones

# Clonar el Backend
git clone https://github.com/Charlyssde/transactions-backend.git backend

# Clonar el Frontend
git clone https://github.com/Charlyssde/transactions-frontend.git frontend

# Clonar el rpa
git clone https://github.com/Charlyssde/rpa.git rpa

# Se debería ver de la siguiente forma la estructura de las carpetas
# transacciones/
# ├── backend/
# └── frontend/
# └── rpa/

# Copiar el docker-compose al directorio raíz desde el /backend
cp backend/docker-compose.yml .

# Ejecutar el comando de docker para levantar todos los servicios 
docker-compose up --build

```

Una vez que los contenedores estén corriendo, los servicios estarán disponibles en los siguientes puertos locales:

* 🌐 Frontend (React / Vite): http://localhost:5173
* ⚙️ Backend API (Django): http://localhost:8000
* 🔌 WebSockets (Channels): ws://localhost:8000/transactions/stream/


## RPA
Para ejecutar el RPA, deberás seguir los siguientes pasos:
```bash
# Cambiar de directorio
cd rpa

# Activar el venv dentro de la terminal
python -m venv venv
source venv/bin/activate

# Instalar dependencias del proyecto
pip install -r requirements.txt

# Ejecutar el bot
python bot.py
```