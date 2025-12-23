# Django School Management CRUD Application

This is a Django-based web application built using **Class-Based Views (CBVs)**.  
It demonstrates complete **CRUD (Create, Read, Update, Delete)** operations for a **School** model and its related **Students** model.

---

## 🚀 Features

- School List View
- School Detail View
- Create School
- Update School
- Delete School
- Home Page using TemplateView
- One-to-Many relationship (School → Students)
- Uses Django Generic Class-Based Views

---

## 🛠️ Tech Stack

- Python
- Django
- HTML (Templates)
- SQLite (default Django DB)

---

## 📂 Project Structure

project/
│
├── app/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ │ └── app/
│ │ ├── Home.html
│ │ └── school_form.html
│
├── manage.py
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/django-school-management-crud.git
cd django-school-management-crud
2️⃣ Create virtual environment
bash
Copy code
python -m venv venv
3️⃣ Activate virtual environment
Windows

bash
Copy code
venv\Scripts\activate
Linux / macOS

bash
Copy code
source venv/bin/activate
4️⃣ Install dependencies
bash
Copy code
pip install django
5️⃣ Run migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
6️⃣ Create superuser
bash
Copy code
python manage.py createsuperuser
7️⃣ Run the server
bash
Copy code
python manage.py runserver
🌐 URLs
URL	Description
/Home/	Home Page
/school_list/	List of Schools
/SchoolCreate/	Create School
/<pk>/	School Detail
/update<pk>/	Update School
/delete<pk>/	Delete School
