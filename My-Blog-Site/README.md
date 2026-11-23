<div align="center">

# ✍️ My Blog — Bilingual Django Blogging Platform

**A sleek, secure, and modern full-stack blogging application built with Django.**  
Designed for seamless reading and writing with inline editing, smart authentication flows, and native Bengali + English URL slug support.

<p>
  <kbd>🐍 Python 3.10+</kbd> &nbsp;
  <kbd>🎸 Django 5.x</kbd> &nbsp;
  <kbd>🌐 HTML5</kbd> &nbsp;
  <kbd>🎨 CSS3</kbd> &nbsp;
  <kbd>⚡ Vanilla JavaScript</kbd>
</p>

</div>


</div>


---

## 📖 Overview

**My Blog** is a lightweight, responsive personal blogging platform engineered with clean UI/UX principles and robust Django backend practices. Unlike basic CRUD apps, it focuses on real-world user experience—featuring zero-reload inline post editing, intelligent login redirects (`?next=`), UUID-based database security, and custom Unicode slug generation that preserves Bengali diacritics (*kar-phola*) alongside English text.

---

## ✨ Core Features & Technical Highlights

| Feature | Description |
| :--- | :--- |
| **🔐 Smart Auth & Redirects** | Complete Sign Up, Log In, and Log Out system with dynamic navigation states. Unauthenticated users clicking **"+ Create Post"** are redirected to login and automatically returned to the editor afterward. |
| **⚡ Seamless Inline Editing** | Clicking **✎ Edit** on a post opens an action menu (`Update` / `Delete`) and transforms the article view directly into an editable form on the same page using Vanilla JS. |
| **🌐 Bilingual Unicode Slugs** | Custom regex-powered `save()` override generates clean, collision-free URLs supporting both **Bengali** and **English** titles with a 6-character UUID suffix. |
| **🛡️ Author-Level Security** | Strict ownership checks (`post.user == request.user`) on both template and view layers prevent unauthorized edits or deletions. Safe `POST`-only deletion protects against CSRF attacks. |
| **🆔 UUID Primary Keys** | Replaces predictable auto-incrementing IDs with `UUIDField` to prevent enumeration attacks. |
| **🔔 Dismissible Alerts** | Custom-styled, closeable success and error notification banners integrated globally into `base.html`. |

---

## 🔗 Application Routes

| Endpoint | View | Access | Description |
| :--- | :--- | :--- | :--- |
| `/` | `show_blog` | Public | Home feed displaying summarized posts (`truncatewords`) |
| `/post_blog/` | `post_blog` | Login Required | Create and publish a new blog post |
| `/details_blog/<slug>/` | `details_blog` | Public | Full article view with inline edit/delete controls for the author |
| `/update_blog/<slug>/` | `update_blog` | Author Only | Processes inline post updates via `POST` |
| `/delete_blog/<slug>/` | `delete_blog` | Author Only | Securely deletes the post via `POST` and redirects home |
| `/account/account_register/` | `account_register` | Public | New user registration using `UserCreationForm` |
| `/account/account_login/` | `account_login` | Public | User authentication with `?next=` redirect support |

---

## 📂 Project Architecture

```text
my-blog/
├── blog/                        # Core blogging application
│   ├── migrations/              # Database schema migrations
│   ├── forms.py                 # ModelForm configurations (Blog_Form)
│   ├── models.py                # Blog model with UUID & Unicode regex slugify
│   ├── urls.py                  # Blog CRUD & detail routes
│   └── views.py                 # Business logic & ownership authorization
├── account/                     # Authentication module
│   ├── forms.py                 # Custom UserCreationForm (Sign_Up)
│   ├── urls.py                  # Login, logout, and registration routes
│   └── views.py                 # Auth handlers with safe next-URL redirection
├── templates/
│   ├── base.html                # Master template (dynamic navbar & alert system)
│   ├── show_blog.html           # Main feed template
│   ├── blog/
│   │   ├── post_blog.html       # Post creation interface
│   │   └── details_blog.html         # Article detail & JS-powered inline editor
│   └── account/
│       ├── account_login.html   # Styled login card
│       └── account_register.html# Styled registration card
├── manage.py
└── requirements.txt
```

---

## 🚀 Local Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/mdarafatkhananik/django-learning-stage.git
cd your-repo-name
```

### 2. Set Up Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database & Superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Launch the Server
```bash
python manage.py runserver
```
Visit **`http://127.0.0`** in your browser to explore the application.

---

## 📸 Screenshots

<img width="1366" height="642" alt="Show Blpg" src="https://github.com/user-attachments/assets/c73b5bcb-3b2c-47e5-94dd-e2401c34c1aa" />
<img width="1366" height="639" alt="Blog Post" src="https://github.com/user-attachments/assets/086797b5-1888-4e32-be26-f2227b19d156" />
<img width="1366" height="641" alt="Blog CRUD" src="https://github.com/user-attachments/assets/a899192d-3324-465d-a461-492a40980e02" />

---

## 🔮 Future Enhancements

- [ ] Search and filter posts by title or author
- [ ] Post ordering by latest creation timestamp (`created_at`)
- [ ] Comment section for reader engagement
- [ ] Rich-text / Markdown editor and cover image uploads

---

## 🤝 Contributing & License

Contributions, issues, and feature requests are welcome!  
This project is open-source and licensed under the **MIT License**.
