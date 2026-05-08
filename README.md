# Django Blog Website

A modern and responsive blog web application built with **Django** that allows users to create, manage, and share blog posts. This project demonstrates full-stack web development concepts including authentication, database management, CRUD operations, and responsive frontend design.

---

## 🚀 Features

- User Authentication (Register, Login, Logout)
- Create, Read, Update, Delete (CRUD) Blog Posts
- User-specific Dashboard
- Responsive Design for Mobile and Desktop
- Search Functionality
- Admin Panel for Content Management
- Database Integration with SQLite
- Secure Form Handling and Validation

---

## 🛠️ Tech Stack

**Frontend**
- HTML5
- CSS3
- JavaScript

**Backend**
- Python
- Django

**Database**
- SQLite

---

## 📂 Project Structure

```bash
blog-website/
│── blog/
│   │── migrations/
│   │── templates/
│   │── static/
│   │── models.py
│   │── views.py
│   │── urls.py
│
│── users/
│   │── templates/
│   │── forms.py
│   │── views.py
│
│── blogproject/
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│
│── db.sqlite3
│── manage.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/django-blog-website.git
```

### 2. Navigate to Project Directory
```bash
cd django-blog-website
```

### 3. Create Virtual Environment
```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Run Database Migrations
```bash
python manage.py migrate
```

### 7. Start Development Server
```bash
python manage.py runserver
```

Open browser and visit:

```bash
http://127.0.0.1:8000/
```

## 🔮 Future Enhancements

- Comment System
- Like and Bookmark Posts
- Rich Text Editor
- User Profile Page
- Blog Categories & Tags
- Deployment on AWS/Render/Heroku

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create your feature branch
```bash
git checkout -b feature-name
```
3. Commit your changes
```bash
git commit -m "Added new feature"
```
4. Push to branch
```bash
git push origin feature-name
```
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Rudraj Kumar Nath**

- GitHub: https://github.com/Rudrajcoder03
- LinkedIn: https://www.linkedin.com/in/rudraj-kumar-nath-b76b6627a

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
