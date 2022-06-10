Repositorio Git:

git clone https://github.com/thmxluis/athos-api.git

### Version de python
### Python 3.6.8 > Desintalar otras versiones de python
https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe

### Entorno virtual
py -m venv venv

### Activamos el entorno virtual
.\venv\Scripts\activate

### Instalmos las dependencias
pip --no-cache-dir install -r requirements.txt

### Instalamos el servidor 
# le cambiamos el puerto por defecto de 8000 a 8001
uvicorn main:app --port 8001 --reload

### Docs
http://localhost:8001/docs#/
http://localhost:8001/redoc#/