**Documentação da API**
----

OBS.:
	Através do software Insomnia, o arquivo `blog_api_requests.json` pode ser importado e o ambiente
	para testes estará configurado, tanto para desenvolvimento quanto para o Heroku, de forma que todas as rotas da API estarão disponíveis.
	Para as rotas que não são de autenticação, o token de acesso está pré-configurado nas preferências dos ambientes,
	de forma que ele atualiza sempre com a rota de login.
	Nas preferências dos ambientes também está configurada a base URL para ser usada em todas as rotas, e caso necessário,
	alterá-la, automaticamente configura todo o ambiente

**Signup**
----
  Cria usuário para fazer uso da API

* **URL**

  /signup

* **Method:**

  `POST`

* **Data Params**

  `{email: "teste@teste.com", password: "123$#45"}`

* **Success Response:**

  * **Code:** 201 CREATED <br />
    **Content:** `{email: test@test.com, password: hash}`
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : {email:["User with this email already exists."]}, }`

  OR

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : {<field>:["This field cannot be empty."]}, }`


**Login**
----
  Gera o token de acesso à api

* **URL**

  /login

* **Method:**

  `POST`

* **Data Params**

  ```{email: "teste@teste.com", password: "123$#45"}```

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:** `{refresh: <refresh_token>, access: <access_token>}`
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{"detail": "No active account found with the given credentials"}`

  OU

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : {<field>:["This field cannot be empty."]}, }`


**Post Index**
----
  Lista os posts

* **URL**

  /post/

* **Method:**

  `GET`

*  **URL Params**

   **Optional:**
 
   `title=[str]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:** `
    ```
    [
      {
        "id": 1,
        "title": "Lorem ipsum dolor sit amet",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing[...].",
        "image_url": "https://miro.medium.com/max/503/0*ff7rFSLGl14Ysjxr.jpeg"
      },
      {
        "id": 2,
        "title": "Lorem ipsum dolor sit amet",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing[...].",
        "image_url": "https://miro.medium.com/max/503/0*ff7rFSLGl14Ysjxr.jpeg"
      },
    ]
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error :{"detail": "Authentication credentials were not provided."}}`


**Show post**
----
  Retorna os dados de um post.

* **URL**

  /post/:id/

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `id=[integer]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    ```
    {
      "id": 1,
      "title": "Lorem ipsum dolor sit amet",
      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing[...].",
      "image_url": "https://miro.medium.com/max/503/0*ff7rFSLGl14Ysjxr.jpeg"
    },
    
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{"detail": "Not found."}`

  OU

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error :{"detail": "Authentication credentials were not provided."}}`


**Create Post**
----
  Cria um post.

* **URL**

  /post/

* **Method:**

  `POST`
  
*  **URL Params**
  None

* **Data Params**

  ```
  {
    "title": "Lorem ipsum dolor sit amet",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing[...].",
    "image_url": "https://miro.medium.com/max/503/0*ff7rFSLGl14Ysjxr.jpeg"
  }

* **Success Response:**

  * **Code:** 201 CREATED <br />
    **Content:**
    ```
    {
      "id": 1,
      "title": "Lorem ipsum dolor sit amet",
      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing[...].",
      "image_url": "https://miro.medium.com/max/503/0*ff7rFSLGl14Ysjxr.jpeg"
    }
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error :{"detail": "Authentication credentials were not provided."}}`
  
  OU

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : {<field>:["This field cannot be empty."]}, }`


**Update Post**
----
  Atualiza um post.

* **URL**

  /post/

* **Method:**

  `PUT`
  
*  **URL Params**
  None

* **Data Params**

  ```
  {
    "title": "Lorem ipsum dolor sit amet",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing[...].",
    "image_url": "https://miro.medium.com/max/503/0*ff7rFSLGl14Ysjxr.jpeg"
  }

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:**
    ```{
        "title": "Lorem ipsum dolor sit amet",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing[...].",
        "image_url": "https://miro.medium.com/max/503/0*ff7rFSLGl14Ysjxr.jpeg"
      }
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{"detail": "Not found."}`

  OU

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error :{"detail": "Authentication credentials were not provided."}}`

  OU

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : {<field>:["This field cannot be empty."]}, }`


**Delete Post**
----
  Exclui um post.

* **URL**

  /post/:id

* **Method:**

  `DELETE`
  
*  **URL Params**

   **Required:**
 
   `id=[integer]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 204 NO CONTENT<br />
    **Content:** None
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{"detail": "Not found."}`

  OU

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error :{"detail": "Authentication credentials were not provided."}}`
