# proyecto

PASOS:

1.Clonar el repositorio con la URL específica: https://github.com/mamola21/proyecto.git
2.Inicializar el contenedor con el siguiente comando: sudo docker build -t proyecto:v01.
3.Ejecutar el servicio: sudo docker run -it -p 80:80 proyecto:v01 python3 app.py. De manera interactiva sudo docker run -d -p 80:80 
proyecto:v01 python3 app.py 
4.Verificar la creación asertiva: sudp docker ps
5.Crear el archivo tipo app.py para: nano app.py
