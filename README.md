
# Introducción

La API de Eagle Eye Video es una API RESTful integral para grabar, indexar y almacenar videos de cámaras.

Se encarga de todo el trabajo pesado de interactuar con las cámaras, grabar videos, transmitir videos de manera segura a la nube, almacenar videos y ponerlos a disposición para que los usen sus aplicaciones.

# Client Credentials

Antes de interactuar con la API de EEN, es necesario obtener ***Credenciales de Cliente*** (Client Credentials).

Estas credenciales están vinculadas a aplicaciones específicas.

## Procedimiento
### Crear una Cuenta de Desarrollador

Antes de crear una aplicación será necesario crear una cuenta de desarrollador de Eagle Eye Networks. La cuenta se crea en la página [My Application](https://developer.eagleeyenetworks.com/page/my-application).

![](https://files.readme.io/5f0a02a-Sign_Up.png)

### Iniciar Sesión en My Application

Una vez confirmada la dirección de correo se debe iniciar sesión en [My Application](https://developer.eagleeyenetworks.com/page/my-application).

![](https://files.readme.io/27d0283-Sign_In.png)

### Añadir una Nueva Aplicación

Dirígete a la sección **Manage applications** y da clic en el botón **Add application**. Es necesario completar el siguiente formulario:

![](https://files.readme.io/72588e2-New_Application_Form.png)

> [!NOTE]
> Si está integrando la API de Eagle Eye con una aplicación móvil o web que no tiene un canal de retorno seguro para almacenar tokens de acceso, habilite la opción Público.

>Para aplicaciones web o en la nube con un canal de retorno seguro, mantenga la opción Público desactivada. Esto establecerá el tipo de credencial de cliente en Confidencial, lo que le permitirá recibir un token de actualización y un token de acceso.



