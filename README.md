
![Logo](https://www.een.com/wp-content/uploads/2021/03/EEN-logo-440x150-1.png)

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

### Ver las Credenciales de Cliente (Client Credentials)

Una aplicación cliente puede tener varios conjuntos de Client Credentials.

Para ver las credenciales de cliente asociadas a una aplicación, haga clic en el botón **See client credentials** junto al nombre de la aplicación.

![](https://files.readme.io/4559c27-See_Client_Creds.png)

### Crear Credenciales de Cliente (Client Credentials)

Para asociar las credenciales de cliente (Client Credentials) con su aplicación, incluya en la lista blanca las URL de redireccionamiento que va a utilizar para solicitar tokens OAuth.

![](https://files.readme.io/2785175-image.png)

**Resultado:** Ha creado correctamente el primer conjunto de Client Credentials. 

![](https://files.readme.io/45db7b2-image.png)

En la sección **Quick API Testing** puede obtener acceso al **Token de acceso** y la **Base URL**.

## API URLs
### URL de Autenticación

EEN utiliza un dominio único para la autenticación:
[https://auth.eagleeyenetworks.com](https://auth.eagleeyenetworks.com). Con este dominio, puede iniciar sesión, cerrar sesión o renovar su token de acceso.

Al iniciar sesión, los usuarios pueden ser redirigidos a un dominio diferente. Para las cuentas de Eagle Eye, este es el enlace: [https://id.eagleeyenetworks.com](https://id.eagleeyenetworks.com)

### Recuperando la Base URL con Postman

Todas las solicitudes de API deben realizarse con la Base URL.

La Base URL garantiza que te comuniques directamente con la plataforma Eagle Eye Video API, lo que garantiza una latencia más baja.

Para recuperar esta Base URL en Postman sigue los siguientes pasos:

## Recuperar la Base URL con Postman

Sigue estos pasos para recuperar la **Base URL** de la API de **Eagle Eye Networks** utilizando **Postman**.

### 1. Abrir Postman
Abre la aplicación de Postman en tu computadora.

---

### 2. Configurar la solicitud
- **Método:** `GET`
- **URL:** `https://api.eagleeyenetworks.com/api/v3.0/clientSettings`

  ![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img1.png?raw=true)

---

### 3. Añadir los Headers
En la pestaña **Headers** agrega los siguientes headers a la solicitud:

- **Header 1:**
  - **Key:** `Accept`
  - **Value:** `application/json`

  ![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img2.png?raw=true)
    
---

### 3. Añadir Authorization
En la pestaña **Authorization** abre el dropdown **Auth Type** y selecciona **Bearer Token**:

En el campo de texto Token escribe el **token de acceso** que se te dió en la sección Quick API Testing.

- **Authorization:**
  - **Token:** `tu_token_de_acceso`
 
  ![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img3.png?raw=true)
    
---


### 4. Enviar la solicitud
Haz clic en **Send** para enviar la solicitud.

---

### 5. Ver la respuesta
Si la solicitud es exitosa, recibirás una respuesta en formato JSON como esta:

```json
{
  "httpsBaseUrl": {
    "hostname": "api.c000.eagleeyenetworks.com",
    "port": 443
  }
}


