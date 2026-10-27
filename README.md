# Plastic Reimagined

> An interactive environmental creativity platform empowering people to see discarded plastic bottles as opportunities for creative expression, community art, and circular economy learning.

---

## 🌿 Project Overview

**Plastic Reimagined** is built with a production-ready Django foundation, utilizing server-rendered HTML5 templates, Vanilla CSS3, and Vanilla JavaScript—without unnecessary heavyweight frameworks.

### Platform Architecture & Destinations

The platform is structured into clean, decoupled Django applications:

| Application | Namespace | Scope / Responsibility |
|:---|:---|:---|
| **`core`** | `core:` | Entrypoint, base templates, design system tokens, layout, and health monitoring. |
| **`studio`** | `studio:` | **Destination 1 — Create**: 2D Creative Studio, bottle transformation canvas, starter designs, and creative challenges. |
| **`catalogue`** | `catalogue:` | **Destination 2 — Discover**: Educational environmental catalogue detailing plastic resin codes, marine life impacts, and sustainable alternatives. |
| **`blog`** | `blog:` | **Destination 3 — Read**: Visual environmental blog, photo essays, and artisan upcycling stories. |
| **`gallery`** | `gallery:` | **Destination 4 — Showcase**: Public visitor creations gallery and moderation workflows. |
| **`config`** | — | Project settings, URL dispatch, WSGI/ASGI gateways, and environment bindings. |

---

## 🛠️ Technology Stack

- **Backend Framework**: Python 3.13+ & Django 5.1
- **Templating**: Django Templates (DTL)
- **Frontend**: Semantic HTML5, Vanilla CSS3 (Custom Design Tokens), Vanilla JavaScript (ES6+)
- **Database**:
  - **Local Development**: SQLite (default, zero configuration)
  - **Production Ready**: PostgreSQL support via `DATABASE_URL` (configured via `dj-database-url`)
- **Administration & Moderation**: Built-in Django Admin (visitors need no accounts)

---

## 🚀 Windows Setup Guide

Follow these steps to set up and run the project locally on Windows.

### 1. Prerequisites

- Python 3.11+ installed and added to your `PATH`.
- Git (optional, for version control).

Check your Python installation:
```powershell
python --version
```

### 2. Create and Activate Virtual Environment

Navigate to the project root directory:

**In PowerShell:**
```powershell
# Create the virtual environment
python -m venv .venv

# If script execution is blocked in PowerShell, run:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Activate the environment
.\.venv\Scripts\Activate.ps1
```

**In Command Prompt (cmd.exe):**
```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

*(When activated, your prompt will show `(.venv)`)*

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the provided placeholder configuration:

```powershell
# PowerShell
Copy-Item .env.example .env

# Or Command Prompt
copy .env.example .env
```

The default values in `.env` are pre-configured for local SQLite development.

### 5. Apply Database Migrations

Initialize the SQLite database schema:

```powershell
python manage.py migrate
```

### 6. Create Django Administrator (Staff Account)

Create a superuser account for moderating creations and managing blog content:

```powershell
python manage.py createsuperuser
```

### 7. Run the Development Server

Start the local server:

```powershell
python manage.py runserver
```

Open your browser and navigate to:
- **Public Platform**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Django Administration**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🧪 Verification & Testing

Run the automated test suite across all modular applications:

```powershell
python manage.py test
```

Perform Django configuration and system checks:

```powershell
python manage.py check
```

---

## 🐘 PostgreSQL Transition (Production Deployment)

The project uses `dj-database-url` to enable database swapping without modifying application code:

1. **Install PostgreSQL driver**:
   ```powershell
   pip install psycopg[binary]
   ```
2. **Update `.env`**:
   ```env
   DATABASE_URL=postgres://USERNAME:PASSWORD@HOST:5432/DB_NAME
   ```
3. Run migrations on PostgreSQL:
   ```powershell
   python manage.py migrate
   ```

---

## 🔒 Production Security Checklist

Before deploying to a public server:
- [ ] Set `DEBUG=False` in `.env`.
- [ ] Generate a cryptographically secure `SECRET_KEY`.
- [ ] Set exact domains in `ALLOWED_HOSTS` (e.g., `ALLOWED_HOSTS=plasticreimagined.org,www.plasticreimagined.org`).
- [ ] Set `SECURE_SSL_REDIRECT=True`, `SESSION_COOKIE_SECURE=True`, and `CSRF_COOKIE_SECURE=True`.
- [ ] Configure `STATIC_ROOT` and static file serving (e.g., WhiteNoise or an external CDN/Nginx).
- [ ] Configure `MEDIA_ROOT` storage (e.g., S3 or protected persistent volume).

---

## 📁 Directory Structure

```text
plastic-reimagined/
├── .env.example            # Environment configuration template
├── .gitignore              # Python, Django, IDE, and media exclusions
├── manage.py               # Django CLI utility
├── requirements.txt        # Verified project dependencies
├── README.md               # Architecture and setup documentation
├── config/                 # Project configuration root
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Environment-driven settings & DB switching
│   ├── urls.py             # Root URL routing
│   └── wsgi.py
├── core/                   # Platform hub & shared foundations
├── studio/                 # Destination 1: 2D Creative Studio
├── catalogue/              # Destination 2: Environmental Catalogue
├── blog/                   # Destination 3: Environmental Blog
├── gallery/                # Destination 4: Public Creations Gallery
├── static/                 # Static assets
│   ├── css/
│   │   ├── tokens.css      # Design tokens (Colors, Typography, Glass)
│   │   ├── base.css        # Reset, layout & responsiveness
│   │   └── components.css  # Buttons, glass cards, micro-animations
│   └── js/
│       └── main.js         # Vanilla JS utilities & mobile navigation
└── templates/              # Django HTML templates
    ├── base.html           # Master semantic layout
    ├── core/index.html     # Platform overview & status
    ├── studio/index.html   # Studio destination entrypoint
    ├── catalogue/index.html# Catalogue destination entrypoint
    ├── blog/index.html     # Blog destination entrypoint
    └── gallery/index.html  # Gallery destination entrypoint
```
