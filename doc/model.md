# Model User
O princial modelo de dados da API trata-se de uma classe.
###### Caminho até o modelo
> app/models/user.py

Essa classe herda de BaseModel da lib pydantic
> class User(BaseModel):

Para construir essa classe é necessário passar um dict
> user = User(**user_dict):
