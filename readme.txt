Repositorio Git:

git clone https://github.com/thmxluis/athos-api.git

### Entorno virtual
py -m venv venv

### Activamos el entorno virtual
.\venv\Scripts\activate

### Instalmos las dependencias
pip install -r requirements.txt

### Instalamos el servidor 
# le cambiamos el puerto por defecto de 8000 a 8001
uvicorn main:app --port 8001 --reload

### Docs
http://localhost:8001/docs#/
http://localhost:8001/redoc#/