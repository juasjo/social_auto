# 📘 Manual de Administración - Social Auto Publisher

Este documento resume los comandos y procedimientos para administrar el proyecto en el servidor.

---

## 🛠️ Servicio systemd

- **Ver estado del servicio:**
  ```bash
  systemctl status social_auto.service
  ```

- **Reiniciar el servicio:**
  ```bash
  systemctl restart social_auto.service
  ```

- **Ver logs en vivo:**
  ```bash
  journalctl -u social_auto.service -f
  ```

---

## 🔄 Actualizar el proyecto desde GitHub

1. Ir al directorio del proyecto:
   ```bash
   cd /root/proyectos/social_auto
   ```

2. Actualizar desde `main`:
   ```bash
   git pull origin main
   ```

3. Reiniciar servicio para aplicar cambios:
   ```bash
   systemctl restart social_auto.service
   ```

---

## 🔑 Manejo de cookies

- Generar cookies en tu PC con entorno gráfico:
  ```bash
  python scripts/save_cookies_instagram.py
  python scripts/save_cookies_tiktok.py
  ```

- Copiar cookies al servidor:
  ```bash
  scp cookies_instagram.json root@SERVIDOR:/root/proyectos/social_auto/cookies/
  scp cookies_tiktok.json root@SERVIDOR:/root/proyectos/social_auto/cookies/
  ```

---

## 📂 Estructura de publicaciones

- Instagram:
  ```
  data/instagram/DD_MM_YYYY/foto1.jpg
  data/instagram/DD_MM_YYYY/foto1.txt
  ```

- TikTok:
  ```
  data/tiktok/DD_MM_YYYY/video1.mp4
  data/tiktok/DD_MM_YYYY/video1.txt
  ```

- Regla de fechas:
  - Hoy o pasado → se publica inmediatamente.
  - Futuro → se agenda a las 12:00 de ese día.

---

## 🧰 Troubleshooting

- **El servicio no arranca** → revisar logs:
  ```bash
  journalctl -u social_auto.service -n 50 --no-pager
  ```

- **No publica en Instagram/TikTok**:
  - Verificar que las cookies existen en `/root/proyectos/social_auto/cookies/`.
  - Si caducaron, regenerar con los scripts de cookies.

- **Error con dependencias**:
  ```bash
  source venv/bin/activate
  pip install selenium watchdog apscheduler
  ```

---
