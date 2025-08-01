# Sistema Lista de Tarefas

## Descrição

Este projeto é um sistema web simples para cadastro e gerenciamento de tarefas, desenvolvido com **Python-Flask** no backend e HTML, CSS e JavaScript puros no frontend.

O sistema permite cadastrar, listar, editar, excluir e reordenar tarefas, mantendo os dados armazenados em um banco de dados relacional (PostgreSQL).

---

## Funcionalidades

- **Listagem de tarefas**  
  Exibe todas as tarefas cadastradas, ordenadas pela ordem de apresentação definida.  
  Tarefas com custo maior ou igual a R$1.000,00 são destacadas com fundo amarelo.

- **Inclusão de tarefa**  
  Permite adicionar novas tarefas com nome, custo e data limite.  
  A nova tarefa é adicionada ao final da lista (última na ordem).

- **Edição de tarefa**  
  Permite alterar o nome, custo e data limite de uma tarefa existente.  
  A edição verifica se o novo nome da tarefa já existe na base, evitando duplicidade.

- **Exclusão de tarefa**  
  Permite remover uma tarefa da lista, com confirmação antes da exclusão.

- **Reordenação de tarefas**  
  Permite mudar a posição das tarefas na lista, através de botões "subir" e "descer" ao lado de cada tarefa.

---

## Arquitetura do Projeto

O sistema foi desenvolvido seguindo uma arquitetura em camadas, visando organização e manutenção:

- **Model**  
  Define a estrutura da entidade Tarefa e representa a tabela no banco de dados.

- **Repository**  
  Responsável pela comunicação direta com o banco de dados, realizando consultas e comandos SQL.

- **Service**  
  Contém a lógica de negócio, validações e regras do sistema.

- **Controller**  
  Lida com as requisições HTTP, interage com a camada de serviço e retorna as respostas.

- **Frontend**  
  Construído com HTML, CSS e JavaScript puro para interatividade e manipulação da interface.

---

## Tecnologias Utilizadas

- Python 3.x  
- Flask  
- SQLAlchemy (opcional, se usado) ou outro ORM / biblioteca para DB  
- HTML5  
- CSS3  
- JavaScript 
- Banco de dados relacional (PostgreSQL)


## Convenções de Código

- Os métodos e funções no backend foram escritos seguindo a convenção **snake_case**, que é padrão no Python.  
