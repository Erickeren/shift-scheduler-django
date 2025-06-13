# Shift Scheduler Django

Aplikasi Django untuk penjadwalan otomatis shift pagi dan malam tim support.

## Fitur
- Input manual 4 nama
- Shift pagi & malam (12 jam masing-masing)
- Siklus 4 hari kerja 2 orang, 4 hari libur 2 orang
- Tabel hasil dan tabel libur dengan warna per nama

## Jalankan di GitHub Codespaces

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Akses app dari tab PORTS > 8000.
