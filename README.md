# 🚔 Crime Investigation Backend

A RESTful API built using **FastAPI** and **SQLite** for managing criminal investigation cases. This project allows users to create, update, retrieve, and delete criminal cases along with related suspects, witnesses, and evidence.

---

## 🚀 Features

* Create a new criminal case
* Retrieve case details
* Update case information
* Delete a case
* Add suspects to a case
* View suspects of a case
* Add witness statements
* View witness statements
* Add evidence
* View evidence
* SQL JOIN to retrieve related case information
* SQLite database with Foreign Key relationships
* Error handling using HTTPException

---

## 🛠️ Technologies Used

* Python 3
* FastAPI
* SQLite3
* Pydantic
* Uvicorn

---

## 📁 Project Structure

```text
crime-investigation-backend/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   └── crime.db
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/gowthamsakelu/crime-investigation-backend.git
```

Move into the project:

```bash
cd crime-investigation-backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn backend.main:app --reload
```

---

## 📌 API Endpoints

### Cases

| Method | Endpoint      | Description   |
| ------ | ------------- | ------------- |
| POST   | `/case`       | Create a case |
| GET    | `/cases/{id}` | Get a case    |
| PUT    | `/cases/{id}` | Update a case |
| DELETE | `/cases/{id}` | Delete a case |

### Suspects

| Method | Endpoint              | Description  |
| ------ | --------------------- | ------------ |
| POST   | `/suspect`            | Add suspect  |
| GET    | `/suspects/{case_id}` | Get suspects |

### Witnesses

| Method | Endpoint               | Description            |
| ------ | ---------------------- | ---------------------- |
| POST   | `/witnesses`           | Add witness            |
| GET    | `/witnesses/{case_id}` | Get witness statements |

### Evidence

| Method | Endpoint              | Description  |
| ------ | --------------------- | ------------ |
| POST   | `/evidence`           | Add evidence |
| GET    | `/evidence/{case_id}` | Get evidence |

---

## 📊 Database Design

The project uses four tables:

* Cases
* Suspects
* Witnesses
* Evidence

Relationships are maintained using **Foreign Keys** with **ON DELETE CASCADE**.

---

## 🧪 API Documentation

After starting the server, FastAPI automatically generates interactive API documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## 🔮 Future Improvements

* JWT Authentication
* User Login System
* Image Upload for Evidence
* Search & Filtering
* Pagination
* Deployment (Render / Railway / AWS)
* Docker Support

---

## 👨‍💻 Author

**Gowtham Sakelu**

BSc Data Science Student | Python Developer | FastAPI Learner

GitHub: https://github.com/gowthamsakelu
