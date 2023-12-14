## Preparar AWS
### Crear bucket S3
Esto lo hicimos durante clases. Puede consutar más detalles en la [documentación oficial](https://docs.aws.amazon.com/es_es/AmazonS3/latest/userguide/creating-bucket.html)

### Instancia EC2
Se recomienda trabajar con instancia de Ubuntu. Su creación la puede realizar según lo hicimos en clases pero abriendo puertos adicionales para poder acceder a su aplicación Web.

#### Apertura de puertos
Una vez creada su instancia EC2, dirijase a pestaña de Seguridad para poder acceder a su grupo de seguridad ([referencia](https://drive.google.com/file/d/10p6fVgc1APWSkPADpxA95bBHRiSb-AyW/view?usp=sharing)).

En la vista de su grupo de seguridad, dirijase al apartado de **Reglas de entrada**, y de click en **Editar reglas de entrada**.

Debe agregar reglas para los puertos 80 y 8080 como se muestra [aquí](https://drive.google.com/file/d/1WgT6GSTtC5FFcTSe8mx7BWFdZepUFOuB/view?usp=sharing).

> [!CAUTION]
> Esta configuración es solo didáctica, no se recomienda dejar abiertos estos puertos para todas las IPs a menos que su app implemente mecanismos de seguridad robustos.

#### Conguración de AWS
Antes de poder usar las funciones de S3, debe configurar AWS en la instancia EC2 donde desplegará su app según se especifica en la [sección de configuración](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration).

Para crear su clave de acceso, debe seguir las instrucciones de **To create an access key** especificada en la [documentación oficial](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html?icmpid=docs_iam_console#Using_CreateAccessKey).

## Sobre esta App

Esta app se ha escrito como una Prueba de Concepto solamente.

Al ser una aplicación en Flask, se ha usado el AWS SDK para Python, boto3, puede acceder a código de ejemplo que satisface los requerimientos de proyecto en la [documentación oficial del SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html).

La aplicación provee una interfaz sin estilos ya que no es parte de los requerimientos para la elaboración de su proyecto. Esta versión solo muestra archivos en un bucket S3 y permite cargar nuevos, para su proyecto se debe agregar la opción de descarga.

Para ejecutar esta app, se debe especificar el puerto sobre el que se levantará el servidor en ambiente de desarrollo:

### Ejecutar en ambiente de desarrollo
Se asume que tiene instalado **Python3** y **pip**, los siguientes comandos deben ejecutarse en a carpeta de este proyecto.

```sh
# Instalar virtualenv
pip install virtualenv

# Crear ambiente virtual
virtualenv venv

# Inicializar virtualenv
source ./venv/bin/activate

# Instalar Flask y boto3
pip install Flask
pip install boto3

# Iniciar web server
flask run --host=0.0.0.0 --port=8080
```