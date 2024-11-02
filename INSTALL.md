## Installation Guide

### Step 1: Git Clone the Repository
```bash
git clone https://github.com/The-Powerpuff-Girls3/CSC-510-Movie-Mood.git
```

### Step 2: Install the required packages
```bash
pip install -r requirements.txt
```

### Step 3: Get a TMDB API Key

To get an API key from TMDB:

1. [Signup for an account](https://www.themoviedb.org/signup)
2. Under the Account icon, click **Settings**.
3. On the **API** page, click on the link under the **Request an API Key** section.
4. Register an API key.
5. Agree to the terms of use and fill in the required information.

### Step 4: Create a `.env` file
In the project directory, create a `.env` file and add your TMDB API key:
```bash
# .env
TMDB_API_KEY=YOUR_TMDB_API_KEY
```

### Step 5: Run the following commands
Navigate to the app directory and initialize the database:
```bash
cd app
python init_db.py
python run.py
```

### Step 6: Open the Application
Open your browser and go to:
```
http://127.0.0.1:8000/
```

### Enjoy!
Start matching your mood with the perfect movies!
