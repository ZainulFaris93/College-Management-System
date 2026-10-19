# College Management System

[![Live demo](https://img.shields.io/badge/demo-live-2ea44f)](https://college-management.onrender.com/login_page)

A Django web app for running a college's records. Admins manage courses, students and teachers; teachers sign up, log in and keep their own profile up to date.

**Live demo:** https://college-management.onrender.com/login_page

| Role    | Username | Password      |
|---------|----------|---------------|
| Admin   | `admin`  | `Admin@123`   |
| Teacher | `anjali` | `Teacher@123` |

On the login page, click a role to fill in its credentials. The demo runs on Render's free plan, so the first load after it has been idle can take up to a minute. Demo data resets automatically.

## Features

- **Admin:** add courses with fees, add students, view/edit/delete student records, view and remove teachers
- **Teacher:** self sign-up with a profile photo and course, a personal dashboard, and a profile they can edit
- **Login** that sends admins and teachers to their own dashboards
- Photo uploads with Django's file handling

## Tech stack

Python · Django 5 · Django ORM · MySQL (local) / SQLite (demo) · HTML · Bootstrap

## Run locally

```bash
cd college_project
pip install -r requirements.txt
export USE_SQLITE=True DEMO_MODE=True    # Windows PowerShell: $env:USE_SQLITE="True"; $env:DEMO_MODE="True"
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

To use MySQL instead, create a `college` database, run `pip install mysqlclient`, and leave out `USE_SQLITE`.

## Deployment and later changes (added with AI assistance)

> **Transparency note:** I built the application. The deployment setup (`render.yaml`, environment-based settings, WhiteNoise), the demo data command (`seed_demo`), the one-click demo logins, and the access checks below were added with help from an AI assistant (Claude).

- Admin pages now require an admin login, and teacher pages a teacher login. Before, some pages (including delete) could be opened by anyone with the URL.
- Teachers can only edit their own profile.
- In demo mode, the shared demo accounts can't be deleted or edited, so the next visitor can still log in.

---
Built by [Zainul Faris V K](https://zainulfaris93.github.io)
