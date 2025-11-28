# Munch (Mono-Repo)
University Food Review App - Not For Profit and OSS

name: Monash + Lunch  (get it)


## Backend getting started
1. create db munch in postgres

2. go into backend folder
```bash
cd backend
```

3. this project uses uv as the package manager
```
uv sync

# MACOS + Linux:
source .venv/bin/activate

# Windows
.venv/scripts/activate.bat
```

4. Migrate database
```bash
uv run manage.py makemigrations && uv run manage.py migrate
```

5. start backend
```
uv run manage.py runserver
```


## Stack
### - Frontend:
  - React Native or Native? (Swift + Kotlin)
  - Zustand state management (for main website)
 
### - Backend (API Only):
  - Django
  - MINIO (s3 compatible storage)
  - Postgres (relational storage)
  - Advertisement algo generator

## Key Functionality 
#### From User Perspective 
user opens app / website -> look at reviews -> wanting to post or order? user login -> join up onto app
-> user can order through app and get through ceebs???

#### Raising funds through the app
- Use advertisement to raise funding (we will advertise other university clubs or the food places themselves)
- (Ad generator) Use ai/ml to score the advertisement based upon factors such as political bias and what not (we are politically neutral), for ad review and it should
automatically queued for advertising.

## Contributing
- look at Contributing.md
