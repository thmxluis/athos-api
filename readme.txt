Repositorio Git:

git clone https://github.com/thmxluis/athos-api.git

### Entorno virtual
py -m venv venv

### Activamos el entorno virtual
.\venv\Scripts\activate

### Instalmos las dependencias
pip install -r requirements.txt

### Instalamos el servidor
uvicorn main:app --reload

### Docs
http://localhost:8001/docs#/
http://localhost:8000/redoc#/