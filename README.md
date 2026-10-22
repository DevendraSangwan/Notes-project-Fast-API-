# FastAPI Notes

A small notes app built with FastAPI, Jinja2 templates, and MongoDB.

## Requirements

- Python 3.10 or newer
- A MongoDB connection string (for example, from MongoDB Atlas)

## Set up a virtual environment

Run these commands from the project folder.

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install fastapi uvicorn pymongo python-dotenv jinja2 python-multipart
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install fastapi uvicorn pymongo python-dotenv jinja2 python-multipart
```

If PowerShell blocks activation, open Command Prompt and use:

```bat
.venv\Scripts\activate.bat
```

## Configure MongoDB

Copy `.env.example` to `.env` in the project folder, then put your MongoDB connection string in `.env`:

```env
MONGO_URI=mongodb+srv://<username>:<password>@<cluster>/<database>?retryWrites=true&w=majority
```

On Linux / macOS:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Replace the example URI with your real connection string. Keep `.env` private; it is excluded by `.gitignore`. Do not commit database credentials to GitHub. If credentials were already pushed, rotate them in MongoDB Atlas.

## Run the app

With the virtual environment activated and `.env` configured:

```bash
uvicorn index:app --reload
```

Open <http://127.0.0.1:8000> in your browser. The app is started from `index.py` (not `main.py`).

## MongoDB data

The app reads and writes notes in the `notes` database and `notes` collection. Notes have a title, description, and an optional “Keep this in mind” flag.
# Notes-project-Fast-API-
