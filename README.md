# Social Auto Publisher

Automatización de publicaciones en **Instagram** y **TikTok** usando **Python + Selenium**.  
Soporta programación automática de posts según la fecha en el nombre de la carpeta.

---

## 📂 Estructura del proyecto
```
/root/proyectos/social_auto/
├── venv/                     # entorno virtual de Python
├── data/
│   ├── instagram/
│   │   ├── DD_MM_YYYY/       # fecha de publicación
│   │   │   ├── foto1.jpg
│   │   │   ├── foto1.txt     # comentario asociado
│   └── tiktok/
│       ├── DD_MM_YYYY/
│       │   ├── video1.mp4
│       │   ├── video1.txt    # comentario asociado
├── cookies/
│   ├── cookies_instagram.json
│   ├── cookies_tiktok.json
├── scripts/
│   ├── instagram.py          # publicar en Instagram
│   ├── tiktok.py             # publicar en TikTok
│   ├── scheduler.py          # planificador APScheduler
│   ├── save_cookies_instagram.py
│   ├── save_cookies_tiktok.py
├── config.py                 # configuración general
├── run_all.sh                # ejecuta el scheduler
├── requirements_pc.txt       # dependencias mínimas para exportar cookies en PC local
├── requirements_server.txt   # dependencias mínimas para el servidor
└── README.md
```

---

## 🔧 Requisitos previos

### En tu PC local (para exportar cookies)
- Tener instalado **Python 3.10+**
- Tener instalado **Google Chrome** (o Chromium)
- Instalar dependencias:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements_pc.txt
  ```

### En el servidor
- Tener instalado **Python 3.10+**
- Instalar **Chromium y Chromedriver**:
  ```bash
  sudo apt-get install -y chromium chromium-driver
  ```
- Instalar dependencias:
  ```bash
  source venv/bin/activate
  pip install -r requirements_server.txt
  ```

---

## 🔑 Autenticación con cookies

1. En tu **PC personal** con navegador gráfico:
   ```bash
   python scripts/save_cookies_instagram.py
   python scripts/save_cookies_tiktok.py
   ```
   - Inicia sesión manualmente (usuario, contraseña, 2FA).
   - Se generarán `cookies_instagram.json` y `cookies_tiktok.json`.

2. Copia los JSON al servidor:
   ```bash
   scp cookies_instagram.json root@SERVIDOR:/root/proyectos/social_auto/cookies/
   scp cookies_tiktok.json root@SERVIDOR:/root/proyectos/social_auto/cookies/
   ```

---

## 📅 Programación de publicaciones

- Dentro de `data/instagram/` y `data/tiktok/`:
  - Crear carpetas con formato `DD_MM_YYYY`.
  - Si la fecha es **hoy o pasada** → publica inmediatamente.
  - Si la fecha es **futura** → se programa a las 12:00 de ese día.

Ejemplo:
```
data/instagram/19_09_2025/foto1.jpg
data/instagram/19_09_2025/foto1.txt
```

---

## 🛠️ Servicio systemd

El proyecto corre automáticamente como servicio:

- Archivo: `/etc/systemd/system/social_auto.service`
- Comandos útiles:
  ```bash
  sudo systemctl status social_auto.service
  sudo systemctl restart social_auto.service
  sudo journalctl -u social_auto.service -f
  ```

Se reinicia solo en caso de fallo y arranca al iniciar el servidor.

---

## 🚀 Flujo de uso

1. Generar cookies en tu PC y subirlas al servidor.  
2. Copiar imágenes/videos con sus `.txt` a `data/instagram/` o `data/tiktok/`.  
3. El servicio se encarga de publicar/programar automáticamente.  
