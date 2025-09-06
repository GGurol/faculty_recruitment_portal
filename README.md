### Faculty Recruitment Portal ###



## Installation

1-Clone the repository:
```bash
git clone https://github.com/GGurol/faculty_recruitment_portal.git
```

```bash
cd faculty_recruitment_portal
```

2-Build the docker and it's contens:
```bash
docker compose up --build -d
```

3-Database Operations:
```
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```


4-Visit http://localhost:8000

5-Admin Panel : http://localhost:8000/admin



