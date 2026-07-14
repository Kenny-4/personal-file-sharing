# Personal File Storage

A personal file-sharing web app that can upload, list, download, and delete files. This is meant to be a solution for LAN access. You can configure it for internet but is not recommended. Built with Flask, SQLite, Python and HTML.

## Features
- Access files through any browser.
- User can upload, list, download, and delete individual files.
- Security: Hashed password-protected access, and https encryption.
- Activity logging

## Setup
### 1. Clone Repository
```bash
git clone <https://github.com/Kenny-4/personal-file-sharing>
#cd <your-project-folder>
```
### 2. Create and activate a python virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your password and secret key

```bash
python set_password.py
```

This generates a hashed password and a session secret key, storing both in a `.env` file.

### 5. Run the server

```bash
python main.py
```

And your done. Visit 'https://127.0.0.1:5000' (for localhost) or your device's LAN ip address (with the 5000 port) if accessed on a seperate device on the same network. For LAN, you need to tinker with your device's and possibly your router's firewall settings.

Warning: This application uses self-signed certificate for https. Your browser will show a security warning, this is expected behavior.
Although there are security measures put into place, again, this is not meant to be used over the internet. 
