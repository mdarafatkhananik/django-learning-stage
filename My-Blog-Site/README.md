<div align="center">

<h1>✍️ My Blog — Bilingual Django Blogging Platform</h1>

<p>
  <strong>A sleek, secure, and modern full-stack blogging application built with Django.</strong><br>
  Designed for seamless reading and writing with inline editing, smart authentication flows, and native Bengali + English URL slug support.
</p>

<p>
  <img src="https://shields.io" alt="Python">
  <img src="https://shields.io" alt="Django">
  <img src="https://shields.io" alt="HTML5">
  <img src="https://shields.io" alt="CSS3">
  <img src="https://shields.io" alt="JavaScript">
</p>

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

> *Add screenshots here after uploading them to a `screenshots/` folder in your repository:*
> - **Home Feed:** `![Home Feed](screenshots/home.png)`
> - **Article Detail & Inline Edit:** `![Inline Edit](screenshots/inline-edit.png)`

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
