# Django4 Simple CRUD with REST

1. Create your virtual environment, example: 'python3 -m venv venv'
2. Run makemigrations with 'python3 manage.py makemigrations'
3. Now migrate with 'python3 manage.py migrate'
4. Load all the fixtures running 'python3 manage.py loaddata imovel anuncio reserva'
5. Check for errors testing the application with 'python3 manage.py test'
6. Now it's time for the action 'python3 manage.py runserver'
7. In this project we have three APIs 'imovel', 'anuncio', 'reserva'
8. If you wish you can see the relationship between them accessing the diagrom of the entities in this link: https://dbdiagram.io/d/63ba00e47d39e42284e988e0
9. To access any of the APIs, just throw at your browser http://localhost:8000/ + entity as http://localhost:8000/anuncio
10. In order to see the rutes available in any API jsut open the main route http://localhost:8000/anuncio

That`s all! =D 
