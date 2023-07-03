# Movie Store

A aplicação serve para gerenciar usuários, filmes e compras, incluindo autenticação e permissões de rotas para diferentes tipos de usuário.

Tecnologias utilizadas:

 - Python
 - Django

  ## **Devs**

 > - [Amanda R. Costa](https://www.linkedin.com/in/amanda-fullstack/)

 ---

 ## **Start the project:**
 ### Type the command in the terminal:

```json
  Criar Ambiente Venv : python -m venv venv
  
  Ativar Ambiente Venv : source venv/Scripts/activate -> para Windows // source venv/bin/activate -> para Linux
  
  Instalar Pacotes : pip install -r requirements.txt

  Preencher informações sensíveis no arquivo ENV
  
  Gerar Migrações : python manage.py migrate
  
  Iniciar Servidor : python manage.py runserver
 ```

## Rotas para usar pelo insomnia:
---
**Usuário:**

POST /api/users/ 
Request:
```json
{
 "email": "teste@teste.com",
	"password": "teste123@",
	"fist name": "teste",
	"last name": "teste again",
	"birthday": "13-13-12",
	"is employee": true,
 "is superuser": true,
}
```

PATCH /api/users/ 
- Para Editar dados dos usuários

GET /api/users/ 
- Para listar todos os usuários caso você seja funcionário.

---
**Filmes:**

POST em /api/users/login/
- Retorna um token

POST em /api/movies/
Request:
```json
{
	"title": "Panico 5",
	"user": "teste",
	"duration": "2.45min",
	"rating": "PG-13",
	"synopsis": "Whatever whatever whatever"
}
```

GET em /api/movies/
- Retorna os filmes cadastrados

DELETE em /api/movies/:id/ com token de employee
- Para deletar filmes se for funcionário

GET em /api/movies/:id/ livre para acesso

---
**Pegar Filmes:**

POST em /api/movies/:id/orders/ com token de non employee
- Deve ser possivel comprar filmes com token de non employee

GET em /api/users/:id/ com token de employee
- Employee pode acessar informação de qualquer perfil

PATCH em /api/users/:id/ com token de employee
- Employee pode atualizar informação de qualquer perfil.

---
