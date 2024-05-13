# aws-batch-demo

Este repositorio contiene un script de Python que suma dos números y almacena el resultado en un archivo JSON en un bucket de AWS S3. El script está diseñado para ser ejecutado en un contenedor Docker.

## Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente:

- Docker instalado en tu máquina. [Instalar Docker](https://docs.docker.com/get-docker/)
- Credenciales de AWS configuradas en tu máquina o en el entorno en el que ejecutarás el contenedor. [Configurar AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

## Construcción de la Imagen

Para construir la imagen de Docker, sigue estos pasos:

1. Clona el repositorio:

git clone [URL_DEL_REPOSITORIO] cd [NOMBRE_DEL_REPOSITORIO]


2. Construye la imagen de Docker:
bash
```
docker build -t sumar-s3 .

```

## Ejecución del Contenedor

Para ejecutar el contenedor, necesitarás proporcionar algunos argumentos de línea de comando requeridos por el script `sumar.py`. Los argumentos son:

- `numero1`: Primer número a sumar.
- `numero2`: Segundo número a sumar.
- `bucket`: Nombre del bucket de S3 donde se almacenará el resultado.
- `key`: Clave del archivo en el bucket de S3.

Ejemplo de comando para ejecutar el contenedor:

bash
```
docker run sumar-s3 numero1 numero2 bucket key
```

Reemplaza `numero1`, `numero2`, `bucket` y `key` con los valores reales que deseas utilizar.

## Cómo Contribuir

Si deseas contribuir al proyecto, considera lo siguiente:

- **Reporta Bugs**: Utiliza la sección de Issues para reportar cualquier bug.
- **Solicita Funcionalidades**: ¿Hay algo que te gustaría añadir? ¡Abre un nuevo Issue!
- **Envía Pull Requests**: Si deseas agregar o mejorar el proyecto, realiza tus cambios en una rama y envía un Pull Request.



