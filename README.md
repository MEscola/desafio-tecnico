# Sistema de GEstão de Projetos
Este projeto foi desenvolvido em **Django**, focada no gerenciamento de usuários e projetos.
---


## Tecnologias Utilizadas
- Python 3.10.12 
- Django 5.2.10
- SQLite
- HTML5, CSS3 e JavaScript.

### 1. Preparar o Ambiente
Clone o repositório e crie o ambiente virtual:
```bash
# Clonar o repositório
git clone <url-do-seu-repositorio>
cd desafio-tecnico

# Criar e ativar o ambiente virtual
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate 

# Instalar Dependências
pip install django
```
## 2. criar DB e Migrations
O projeto utiliza o sistema de migrações do Django para estruturar o banco de dados. Siga os passos abaixo:
```bash
# Gerar arquivos de migração:
python manage.py makemigrations

# Aplicar as migrações:
python manage.py migrate

```
Obs: Caso o terminal solicite um valor padrão para campos DateField, insira uma data no formato 'YYYY-MM-DD' (ex: `'2000-01-01'').

## 3. Iniciar o servidor:
python manage.py runserver

### 4. Ferramentas de Produtividade
* **VS Code IntelliSense:** Utilizado ativamente para garantir a precisão na escrita do código, autocompletar sintaxes do Django e agilizar a importação de módulos e validações personalizadas, reduzindo erros de digitação e aumentando a velocidade de entrega.

## Acesso às Rotas Principais

Com o servidor rodando em `http://127.0.0.1:8000/`, as rotas principais são:

* **Página Inicial:** `/`
* **Gestão de Usuários:** `/users/` (Lista e acesso ao Perfil)
* **Novo Cadastro:** `/users/novo/` (Formulário com máscaras)
* **Gestão de Projetos:** `/projects/` (Lista de Projetos Cadastrados)

---

## Decisões Técnicas

### 1. Validação e Integridade (Backend)
* **Algoritmo de CPF:** Implementada uma função de validação matemática de dígitos verificadores no `models.py` para impedir CPFs inválidos no banco de dados.
* **Segurança de Datas:** Criado um validador personalizado para o campo `data_nascimento`, impedindo que datas futuras sejam registradas.
* **Normalização:** O formulário de usuário (`forms.py`) converte automaticamente e-mails para letras minúsculas para evitar inconsistências de login ou busca.

### 2. Mensagens de Feedback
* Integrado o `django.contrib.messages` para fornecer alertas visuais de sucesso após operações de cadastro ou exclusão, melhorando a interatividade do sistema.

---

## Autor
Desenvolvido por **Marcia Escolástico** como parte de um desafio técnico. 

