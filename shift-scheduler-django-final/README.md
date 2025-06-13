# Shift Scheduler Django

Aplikasi web berbasis Django untuk menjadwalkan shift otomatis tim support 24 jam selama 1 bulan penuh.

## ✅ Fitur
- Input 4 nama tim support secara manual
- Jadwal otomatis dengan shift pagi (08:00–20:00) dan malam (20:00–08:00)
- 2 orang bekerja selama 4 hari, 2 orang libur, bergantian
- Output tabel shift + tabel libur
- Warna berbeda untuk masing-masing orang

## 🚀 Cara Menjalankan di GitHub Codespaces

1. **Clone atau buka repo ini di GitHub**
2. Klik tombol `<> Code > Codespaces > Create codespace on main`

### Jalankan perintah berikut di terminal:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

3. Klik **Ports** dan akses aplikasi di port 8000

## 📁 Struktur Proyek

- `shift_app/`: aplikasi Django
- `templates/`: HTML template untuk input dan hasil
- `shift_scheduler/`: konfigurasi project Django
- `requirements.txt`: daftar dependensi

## 📝 Catatan

- Dibuat untuk keperluan simulasi penjadwalan tim support
- Waktu server default mengikuti zona `Asia/Jakarta`
