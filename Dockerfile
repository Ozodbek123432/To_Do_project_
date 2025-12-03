# ==================== BASE ====================
FROM python:3.11-slim

# Kerakli sistem paketlari
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Ishchi papka
WORKDIR /app

# Requirements birinchi (cache tezroq bo‘lishi uchun)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Barcha loyiha fayllarini ko‘chirish
COPY . .

# generated_projects papkasini yaratish (ZIP lar shu yerga tushadi)
RUN mkdir -p generated_projects

# Django uchun kerakli o‘zgarishlar
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Migrate va superuser yaratish (birinchi marta ishlaganda)
# Agar xohlamasangiz, bu qatorlarni o‘chirib qo‘yishingiz mumkin
# COPY entrypoint.sh .
# RUN chmod +x entrypoint.sh

# Port ochish
EXPOSE 8000

# Bot + Django serverni bir vaqtda ishga tushirish
# (Agar faqat bot kerak bo‘lsa — oxirgi qatorni o‘zgartiring)
CMD ["python", "bot.py"]

# Agar Django serverni ham ishlatmoqchi bo‘lsangiz (masalan: /docs/ ochish uchun):
# CMD gunicorn myproject.wsgi:application --bind 0.0.0.0:8000