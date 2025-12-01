# Book API (Django REST + JWT + Swagger)

Zamonaviy kitoblar API si — JWT autentifikatsiya, Swagger dokumentatsiya, toza kod.

## Texnologiyalar
- Django 5.2+
- Django REST Framework
- SimpleJWT (JWT autentifikatsiya)
- drf-spectacular (Swagger + Redoc)

## Ishga tushirish (6 qadam)

```bash
# 1. Loyihani yuklab oling
hozircha clone yoq
cd book-api

# 2. Virtual muhit yarating
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# 3. Kerakli paketlarni o'rnating
pip install -r requirements.txt

# 4. Migratsiyalarni bajaring
python manage.py makemigrations
python manage.py migrate

# 5. Superuser yarating
python manage.py createsuperuser

# 6. Serverni ishga tushiring
python manage.py runserver