
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

![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img4.png?raw=true)

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

Sigue los siguientes pasos para recuperar la **Base URL** de la API de **Eagle Eye Networks** utilizando **Postman**.

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
  1. En la pestaña **Authorization** abre el dropdown **Auth Type** y selecciona **Bearer Token**:

  2. En el campo de texto Token escribe el **token de acceso** que se te dió en la sección Quick API Testing.

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
```

## Logging in

La API de Eagle Eye Networks utiliza el estándar "Código de Autorización" de OAuth2 para autenticar a un usuario y obtener un conjunto de tokens.

Estos tokens pueden ser utilizados por una aplicación de terceros y también pueden utilizarse para llamadas de API de back-end a back-end.

### Fase 1: Conceder acceso a una aplicación de terceros

> [!NOTE]
> Sólo la autorización inicial (Fase 1) requiere acción humana, la autorización de máquina a máquina (Fase 2) puede automatizarse completamente.

### Procedimiento
1. Con el siguiente enlace, realice una solicitud en Postman como HTTP POST o HTTP GET o accede directamente desde el navegador.

```
https://auth.eagleeyenetworks.com/oauth2/authorize?scope=vms.all&client_id={clientId}&response_type=code&redirect_uri={RedirectURL}
```

> [!NOTE]
> Reemplaza la parte de {clientId} por el valor que se obtuvo en la página de [My Application](https://developer.eagleeyenetworks.com/page/my-application).
> 
> Reemplaza la parte de {Redirect URL} por la URI que se establecio anteriormente en la lista blanca en la página.
> 
> No olvides borrar los corchetes `{}`

Ejemplo:
```
https://auth.eagleeyenetworks.com/oauth2/authorize?scope=vms.all&client_id=c5ad678ac8ea4f9ca0775da8f779a1e1&response_type=code&redirect_uri=http://localhost:4200
```

2. Como resultado, se obtendrá un código 200 OK, y el usuario será redirigido a la página de inicio de sesión `auth.eagleeyenetworks.com`.

3. Si el usuario aún no ha iniciado sesión, deberá iniciar sesión en Eagle Eye Networks en la siguiente pantalla:

![](https://files.readme.io/a3accba-image.png)

Después de iniciar sesión, el usuario es redirigido a la URI de redireccionamiento (http://localhost:4200) junto un parámetro nuevo denominado **code**: 
`<redirect_uri>?code=<code parameter>`

![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img5.png?raw=true)

> [!CAUTION]
> Tenga en cuenta que el código (code) solo dura 5 minutos.

4. Utilice este código (code) para obtener el **token de acceso** y el **token de actualización**. 

Para ello puede ejecutar un HTTP POST o un código de Python:

## Método con HTTP POST

### 1. Abrir Postman
Abre la aplicación de Postman en tu computadora.

---

### 2. Configurar la solicitud
- **Método:** `POST`
- **URL:** `https://auth.eagleeyenetworks.com/oauth2/token`

  ![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img6.png?raw=true)

---

### 3. Añadir los Parámateros
En la pestaña **Parámetros** agrega los siguientes parámetros a la solicitud:

- **Parámetro 1:**
  - **Key:** `grant_type`
  - **Value:** `authorization_code`

- **Parámetro 2:**
  - **Key:** `scope`
  - **Value:** `vms.all`

- **Parámetro 3:**
  - **Key:** `code`
  - **Value:** `El código obtenido junto a la URI de redireccionamiento `

  - **Parámetro 4:**
  - **Key:** `redirect_uri`
  - **Value:** `La URI de redireccionamiento con http(s)://`

  ![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img7.png?raw=true)
    
---

### 4. Añadir los Headers
En la pestaña **Headers** agrega los siguientes headers a la solicitud:

- **Header 1:**
  - **Key:** `accept`
  - **Value:** `application/json`

- **Header 2:**
  - **Key:** `content-type`
  - **Value:** `application/x-www-form-urlencoded`

  ![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img8.png?raw=true)
    
---

### 3. Añadir Authorization
  1. En la pestaña **Authorization** abre el dropdown **Auth Type** y selecciona **Basic Auth**:

  2. En el campo de texto Username escribe el **client_id** y en el campo de texto Password escribe el **client_secret**.

- **Authorization:**
  - **Username** `client_id`
  - **Password** `client_secret`
 
  ![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img9.png?raw=true)
    
---


### 4. Enviar la solicitud
Haz clic en **Send** para enviar la solicitud.

---

### 5. Resultado
En respuesta, se obtendrá un token de acceso y un token de actualización. 

El token de acceso se puede utilizar para autenticar llamadas de API, mientras que el token de actualización se puede almacenar para su uso futuro. 

Respuesta de ejemplo:

```json
{
    "access_token": "eyJraWQiOiI2ODYxYjBjYS0wZjI2LTExZWQtODYxZC0wMjQyYWMxMjAwMDIiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJjYTBmNjFhYiIsImF1ZCI6InZtcy5hcGkiLCJpc3MiOiJ2bXMuYXV0aC52MSIsInZtc19hY2NvdW50IjoiMDAwMDExMDYiLCJleHAiOjE2NjAzNjA0ODksImlhdCI6MTY2MDMxNzI4OSwianRpIjoiODJlNWMyMDQ1OTM1OTczNGYyOTU4NjlkZDhlYzIyMDMiLCJjbGllbnRfaWQiOiJCTVRPLVRFU1QiLCJ2bXNfY2x1c3RlciI6ImMwMDAifQ.",
    "expires_in": 43198,
    "httpsBaseUrl": {
        "hostname": "api.c001.eagleeyenetworks.com",
        "port": 443
    },
    "refresh_token": "w1P0nwA7NEZmo5tEd76cco3y5bi4Js6QNgZsXnFNBDRepnJmA2F73tGJ4G_eA0WttI_8xsovsFLvd5uOUayqrNwu7PZ1SH0DAWVZ3",
    "scope": "vms.all",
    "token_type": "Bearer"
}
```

> [!NOTE]
>Obtuviste el token de acceso y la URL base. El token de acceso obtenido se puede utilizar para acceder a los datos del usuario. Por ejemplo, para obtener una descripción general de la cámara o una grabación.

## Método con Python

### 1. Instalar Python: 
Puedes descargar Python desde [python.org](https://www.python.org/downloads/).

### 2. Instalar la biblioteca `requests`:
   - Abre una terminal (o PowerShell en Windows).
   - Ejecuta el siguiente comando para instalar la biblioteca `requests`:
     ```bash
     pip install requests
     ```

### 3. Ejecuta el código Python

A continuación utiliza el siguiente código para realizar una solicitud `POST` para obtener un **access_token** y un **refresh_token**:

```python
import requests

url = "https://auth.eagleeyenetworks.com/oauth2/token"
data = {
  "grant_type": "authorization_code",
  "scope": "vms.all",
  "code": "{code}",  # Reemplaza con tu código de autorización
  "redirect_uri": "{URI with http(s)://}"  # Reemplaza con tu URI de redirección
}
headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded"
}
response = requests.post(
  url,
  headers=headers,
  auth=(
    'CLIENT_ID',       # Reemplaza con tu CLIENT_ID
    'CLIENT_SECRET'    # Reemplaza con tu CLIENT_SECRET
  ),
  data=data
)

print(response.text)
```

### 4. Respuesta

Una vez ejecutado el código de Python, en consola se obtendrá una respuesta indicando el `accesss_token` y el `refresh_token`:

```python
PS D:\Proyectos Eagle Eye Networks> & C:/Users/killt/AppData/Local/Programs/Python/Python313/python.exe

{"access_token":"eyJraWQiOiI2ODYxYjBjYS0wZjI2LTExZWQtODYxZC0wMjQyYWMxMjAw...",
"refresh_token":"Av4xEFcNriL_gi_eTnJO8-CAz7iMcTVZlkOpCNpY_8ECy1rubQFXW-VO...",
"httpsBaseUrl":{"hostname":"api.c028.eagleeyenetworks.com","port":443},
"scope":"vms.all",
"token_type":
"Bearer",
"expires_in":43173}
```

## Fase 2: Machine-to-machine (M2M) authentication

### M2M Authentication with an expiring refresh token

Una vez obtenido el `refresh_token`, se puede utilizar para iniciar sesión nuevamente. 
El `refresh_token` reemplaza el nombre de usuario y la contraseña debido a que la base de datos almacena los `refresh_token`. De esta manera, la contraseña del cliente nunca se almacena en ningún lugar ni puede quedar expuesta.

> [!CAUTION]
> Se recomienda almacenar el token de actualización en un lugar seguro. El token de actualización nunca debe quedar expuesto.

## Iniciar sesión con un HTTP POST

### 1. Configurar la solicitud
- **Método:** `POST`
- **URL:** `https://auth.eagleeyenetworks.com/oauth2/token`

![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img10.png?raw=true)

---

### 2. Añadir los Parámetros
En la pestaña **Params** agrega los siguientes parámetros para la solicitud:

- **Parámetro 1:**
    - **Key:** `grant_type`
    - **Value:** `refresh_token`

- **Parámetro 2:**
    - **Key:** `scope`
    - **Value:** `vms.all`

- **Parámetro 3:**
    - **Key:** `refresh_token`
    - **Value:** `Kq5j2TP-IXWIz3qwOUkK7xLQjUZyXKCUSDWENz8EQ8MUGuJ2QOke9So5MCbKwajpl2Jv86rZoUxU-NUhR7UQO1KsobswLyBfiOhDO4Zp6V9efF4S5dxigVRBeUA4-_K8`

![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img11.png?raw=true)

---

### 3. Añadir los Headers
En la pestaña **Headers**, agrega los siguientes headers a la solicitud:

- **Header 1:**
  - **Key:** `accept`
  - **Value:** `application/json`

- **Header 2:**
  - **Key:** `content-Type`
  - **Value:** `application/x-www-form-urlencoded`

![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img12.png?raw=true)

---

### 4. Añadir Authorization
En la pestaña **Authorization**, selecciona **Basic Auth** como el tipo de autenticación y añade las credenciales:

- **Username:** `client_id`
- **Password:** `client_secret`

![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img13.png?raw=true)

---

### 5. Enviar la solicitud
Haz clic en **Send** para enviar la solicitud.

---

### 6. Resultado
Una vez configurado y enviado el HTTP POST, la respuesta debería incluir el token de acceso y el token de actualización, entre otros datos.

```json
{
    "access_token": "eyJraWQiOiI2ODYxYjBjYS0wZjI2LTExZWQtODYxZC0wMjQyYWMxMjAwMDIiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJjYTBmNjFhYiIsImF1ZCI6InZtcy5hcGkiLCJpc3MiOiJ2bXMuYXV0aC52MSIsInZtc19hY2NvdW50IjoiMDAwMDExMDYiLCJleHAiOjE2NjAzNjA0ODksImlhdCI6MTY2MDMxNzI4OSwianRpIjoiODJlNWMyMDQ1OTM1OTczNGYyOTU4NjlkZDhlYzIyMDMiLCJjbGllbnRfaWQiOiJCTVRPLVRFU1QiLCJ2bXNfY2x1c3RlciI6ImMwMDAifQ.",
    "expires_in": 43198,
    "httpsBaseUrl": {
        "hostname": "api.c001.eagleeyenetworks.com",
        "port": 443
    },
    "refresh_token": "w1P0nwA7NEZmo5tEd76cco3y5bi4Js6QNgZsXnFNBDRepnJmA2F73tGJ4G_eA0WttI_8xsovsFLvd5uOUayqrNwu7PZ1SH0DAWVZ3",
    "scope": "vms.all",
    "token_type": "Bearer"
}
```

## Logging out

* Si cierra sesión en el navegador, se cerrará la sesión de todas las aplicaciones.

* Si cierra sesión a través de una integración de terceros, solo se cerrará la sesión de esa aplicación específica.

## Deleting the token

Para cerrar sesión, envíe una llamada API a `https://auth.eagleeyenetworks.com/oauth2/revoke` con el token que desea revocar. 
Si revoca un token de actualización, también se eliminará el token de acceso correspondiente.

> [!NOTE]
> La llamada a la API debe realizarse como una solicitud HTTP POST con el token en el cuerpo de la solicitud. El content_type debe ser application/x-www-form-urlencoded.

### 1. Configurar la solicitud
- **Método:** `POST`
- **URL:** `https://auth.eagleeyenetworks.com/oauth2/revoke`

![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img14.png?raw=true)

---

### 2. Añadir el Header
En la pestaña **Headers**, agrega los siguientes headers a la solicitud:

- **Header 1:**
  - **Key:** `Content-Type`
  - **Value:** `application/x-www-form-urlencoded`

![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img15.png?raw=true)

---

### 3. Añadir el Body
En la pestaña **Body** marca la opción **x-www-form-urlencoded** y agrega el access_token:

- **Body 1:**
  - **Key:** `token`
  - **Value:** `access_token`

![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img16.png?raw=true)

---

### 4. Añadir Authorization
En la pestaña **Authorization**, selecciona **Bearer Token** como el tipo de autenticación y añade las credenciales codificadas en **Base64**:

- **Authorization:**
  - **Token:** `<clientid:clientsecrets>.base64()`

![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img17.png?raw=true)

---

### 5. Enviar la solicitud
Haz clic en **Send** para enviar la solicitud.

---

### 6. Resultado
Una vez configurado y enviado el HTTP POST, se obtendrá como respuesta un código de estado **200 OK**.

![](https://github.com/killthmxall/EEN-API/blob/main/assets/imagenes/img18.png?raw=true)

