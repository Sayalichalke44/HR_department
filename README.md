
# Department Management Application  

This application is a simple Django-based CRUD (Create, Read, Update, Delete) application to manage a list of departments.  

---

## Features  

- Display a list of active departments.  
- Add a new department.  
- Update department details.  
- Soft-delete departments by marking them as inactive.  

---

## Technologies Used  

- **Framework:** Django  
- **Language:** Python  
- **Frontend:** HTML, CSS  
- **Database:** SQLite (default for Django)  

---

## Installation  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-repo/department-management.git  
   cd department-management  
   ```

2. **Set up a Virtual Environment**  
   ```bash
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```

3. **Install Dependencies**  
   ```bash
   pip install django  
   ```

4. **Migrate the Database**  
   ```bash
   python manage.py makemigrations  
   python manage.py migrate  
   ```

5. **Run the Server**  
   ```bash
   python manage.py runserver  
   ```

6. **Access the Application**  
   Open your browser and navigate to `http://127.0.0.1:8000/`.  

---

## Directory Structure  

```  
department-management/  
├── Department/  
│   ├── migrations/  
│   ├── __init__.py  
│   ├── admin.py  
│   ├── apps.py  
│   ├── models.py       # Model for Department  
│   ├── tests.py  
│   └── views.py        # Views for handling requests  
├── department_management/  
│   ├── __init__.py  
│   ├── asgi.py  
│   ├── settings.py     # Django project settings  
│   ├── urls.py         # URL routing  
│   └── wsgi.py  
├── templates/  
│   ├── index.html       # Home Page  
│   ├── createdepartment.html   # Create Department Page  
│   └── updatedepartment.html   # Update Department Page  
├── manage.py            # Django management script  
└── README.md            # Documentation file  
```  

---

## Application Workflow  

### 1. **Home Page (`index.html`)**  

- Displays a list of active departments in a table.  
- Provides options to edit or delete a department.  
- Has a button to navigate to the "Create Department" page.  

**Route:** `/`  
**View Function:** `home`  

### 2. **Create Department (`createdepartment.html`)**  

- Form to add a new department.  
- Requires input for department name and description.  

**Route:** `/createdepartment`  
**View Function:** `createDepartment`  

### 3. **Update Department (`updatedepartment.html`)**  

- Form prefilled with the department details for editing.  

**Route:** `/edit/<int:did>`  
**View Function:** `updateDepartment`  

### 4. **Delete Department**  

- Marks a department as inactive (soft delete).  

**Route:** `/delete/<int:did>`  
**View Function:** `Deletedepartment`  

---

## Database Model  

The `Department` model has the following fields:  

| Field Name   | Type         | Description                                   |  
|--------------|--------------|-----------------------------------------------|  
| `dept_id`    | AutoField    | Primary Key. Auto-generated ID.               |  
| `dept_name`  | CharField    | Name of the department (max length: 100).     |  
| `description`| CharField    | Description of the department (max length: 300). |  
| `created_at` | DateField    | Auto-populated when the department is created.|  
| `updated_at` | DateTimeField| Auto-updated when the department is modified. |  
| `status`     | BooleanField | Indicates if the department is active.        |  

---

## Code Explanation  

### Models  

Defined in `models.py`:
```python  
class Department(models.Model):  
    dept_id = models.AutoField(primary_key=True)  
    dept_name = models.CharField(max_length=100)  
    description = models.CharField(max_length=300)  
    created_at = models.DateField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    status = models.BooleanField(default=True)  
```  

### Views  

Defined in `views.py`:  

- **`home`**: Fetches and displays active departments.  
- **`createDepartment`**: Handles the form for adding a new department.  
- **`updateDepartment`**: Handles the form for updating department details.  
- **`Deletedepartment`**: Soft-deletes a department by updating its `status` to `False`.  

### URLs  

Defined in `urls.py`:  
```python  
urlpatterns = [  
    path('', views.home),  
    path('createdepartment', views.createDepartment),  
    path('delete/<int:did>', views.Deletedepartment),  
    path('edit/<int:did>', views.updateDepartment),  
]  
```  

---

## Frontend  

- **`index.html`**: Displays the list of departments and their actions.  
- **`createdepartment.html`**: Form for creating a new department.  
- **`updatedepartment.html`**: Form for updating department details.  

---

## Future Enhancements  

- Add user authentication for secure access.  
- Implement a feature to permanently delete inactive departments.  
- Add pagination to the department list.  
- Enhance the user interface with a modern framework like Bootstrap.  

---

## Author  

Developed by **sayali chalke.**  

For any queries, please contact at **chalkesayali@614gmail.com.**  
