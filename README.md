# 🏥 FastAPI Patient Management API

A professional **RESTful Patient Management API** built with **FastAPI** and **Pydantic**.

This project demonstrates how to build a backend REST API with patient CRUD operations, request validation, computed fields, BMI calculation, sorting, error handling, and JSON-based data persistence.

The project is designed as a practical learning project for understanding **FastAPI, Pydantic, REST APIs, and backend development with Python**.

---

## 📌 Project Overview

The **FastAPI Patient Management API** provides a simple backend system for managing patient records.

The API allows users to:

- Create patient records
- View all patients
- View individual patient details
- Update patient information
- Delete patient records
- Sort patients based on height, weight, or BMI
- Automatically calculate BMI
- Automatically classify BMI status
- Validate incoming patient data
- Handle invalid requests using HTTP exceptions
- Explore and test APIs through Swagger UI

Patient information is stored using a JSON file for simplicity and learning purposes.

> **Note:** This project uses JSON-based storage for educational purposes. A production application should use a proper database such as PostgreSQL or MySQL.

---

# ✨ Features

### 👤 Patient Management

- Create new patient records
- Retrieve all patients
- Retrieve a patient using their unique ID
- Update patient information
- Delete patient records

### 🧮 Automatic BMI Calculation

BMI is automatically calculated using:

##### text
BMI = Weight (kg) / Height² (m)
