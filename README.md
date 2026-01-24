## 🔗 miniLink
* `miniLink` is a Django-based REST API for shortening URLs.
### Overview
The `miniLink` API provides a RESTful interface for URL shortening operations. All endpoints return JSON responses (except redirects) and use standard HTTP response codes.

**Key Features:**
- ✅ Secure HMAC-based token generation
- ✅ Persistent URL storage with PostgreSQL
- ✅ Fast redirects with 302 status codes
- ✅ RESTful API design
- ✅ Comprehensive error handling
---

## ⚙️ Local Setup

1. **Clone & Navigate**
```bash
git clone git@github.com:PritomKarmokar/miniLink.git
cd miniLink
```
2. **Copy `.env.example` to `.env`**
```bash
cp .env.example .env
# Update `.env` with DB credentials & secret key
```
3. **Create & Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
4. **Install Dependencies**
```bash
pip install -r requirements.txt 
```
5. **Database & Server**
```bash
python manage.py migrate
python manage.py runserver
```
6. **(Optional) Create Admin**
```bash
python manage.py createsuperuser
```
## 🐳 Docker Setup
- **Build & Run**
```bash
docker compose up --build
```
- **Run Migrations, Create Superuser & Tests** 
- Open another terminal and run the below commands
```bash
docker ps
docker exec -it <container id> bash
python manage.py migrate
python manage.py createsuperuser
```
## 📚 API Documentation
- The complete API reference is available in the `docs` directory.
- [View API Documentation](./docs/api_documentation.md)