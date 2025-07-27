
# 💡 Calculadora Avançada com Histórico (Django)

Esta aplicação web é uma calculadora avançada desenvolvida em Python com o framework Django. Ela permite que usuários autenticados realizem cálculos matemáticos simples e visualizem um histórico das últimas operações realizadas.

---

## 🚀 Funcionalidades

- 🧮 Cálculo com os operadores: adição, subtração, multiplicação e divisão.
- 🔒 Sistema de autenticação com login e cadastro.
- 📜 Histórico individual de operações por usuário.
- 🎨 Interface moderna e responsiva com teclado virtual.
- 🔄 Histórico persistente (armazenado em banco de dados).
- 🔐 Apenas usuários logados têm acesso à calculadora.

---

## 🛠️ Tecnologias

- Python 3.10+
- Django 4.x
- HTML5, CSS3
- SQLite3 (default)
- Templates Django
- Autenticação com `User` model padrão

---

## 📁 Estrutura de Pastas

```
├── app_portal/
│   ├── views.py
│   ├── models.py
│   ├── templates/
│   │   ├── app_portal.html
│   │   └── login.html
│   ├── static/
│       └── app_portal/
│           └── style.css
├── manage.py
├── db.sqlite3
└── urls.py
```

---

## 🧪 Como executar localmente

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Aplique as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Inicie o servidor:
```bash
python manage.py runserver
```

Acesse em: `http://127.0.0.1:8000/`

---

## 🧑‍💻 Autor

Desenvolvido por Rafael Santos. 