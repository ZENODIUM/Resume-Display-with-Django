
# 🧑‍💻 Django Resume Viewer

A simple Django project to display a resume dynamically from a database, with an admin panel for managing data and a Google Docs preview for the resume file. 

---


# Screenshots
## Admin Panel View 🛡️
Admin Panel Screenshot
![WhatsApp Image 2025-02-18 at 20 53 31_43e42725](https://github.com/user-attachments/assets/45e773d2-a4af-41b4-9562-c60242fa6e04)



## Resume Viewer Output 📄
Resume Viewer Screenshot

![WhatsApp Image 2025-02-18 at 20 24 03_532ef245](https://github.com/user-attachments/assets/94cc3ca2-09ba-4c19-bdb0-db725da6137b)

![WhatsApp Image 2025-02-18 at 20 24 28_bb83f1a6](https://github.com/user-attachments/assets/c671da1c-7870-4cff-b4c5-ba6c2369025c)


## 🚀 How to Run This Project

### 1️⃣ Clone the Repository
git clone https://github.com/ZENODIUM/Resume-Display-with-Django
cd repository-folder

### 2️⃣ Set Up the Environment
python -m venv env
source env/bin/activate # On Windows: env\Scripts\activate
pip install -r requirements.txt


### 3️⃣ Apply Migrations
python manage.py migrate


### 4️⃣ Create a Superuser (Admin)
python manage.py createsuperuser

Use these credentials:
- Username: `admin`
- Password: `admin`

### 5️⃣ Run the Server
python manage.py runserver


Navigate to:
- **Admin Panel**: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- **Resume Viewer**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🗂️ Admin Panel Details

The admin panel can be accessed by appending `/admin` to your URL:
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

Log in using:
- Username: `admin`
- Password: `admin`

You can add or edit resume data (e.g., name, email, education, experience) and upload a PDF file for Google Docs preview.

---

## 📋 Models Configuration

The data is stored using Django models defined in `models.py`:
from django.db import models

class Resume(models.Model):
name = models.CharField(max_length=100)
email = models.EmailField()
phone = models.CharField(max_length=15)
linkedin = models.URLField()
github = models.URLField()
kaggle = models.URLField()
education = models.TextField()
experience = models.TextField()
projects = models.TextField()
skills = models.TextField()
competitions = models.TextField()
resume_file = models.FileField(upload_to='resumes/') or Share the google docs link directly in the template html file



The model is registered in `admin.py` for management via the admin panel:



## ✨ About This Project

- Use **Django models** to store resume data (e.g., personal details, education, experience, etc.).
- Configure the **Django admin panel** to manage data using a superuser.
- Render the resume dynamically in HTML with animations and styling.
- Embed a **Google Docs preview** of the resume file (PDF).

---

## Features

- **Admin Panel**: Manage all resume data through the Django admin interface.
- **Dynamic Rendering**: Resume details are fetched from the database and displayed on the webpage.
- **Google Docs Preview**: View the uploaded resume file directly in the browser.
- **Orange-Themed Design**: A clean and consistent UI with animations.

---


