# khanto

1. Create your virtual environment, exemple: 'python3 -m venv venv'
2. Load requirements 'pip install -r requirements.txt'
3. Move to the base directory and run 'python3 manage.py makemigrations & migrate'
4. Load all the fixtures running 'python3 manage.py loaddata imovel anuncio reserva'
5. Check for errors testing the application with 'python3 manage.py test'
6. Now it`s time for the action 'python3 manage.py runserver'
7. Is this project we have three APIs 'imovel', 'anuncio', 'reserva'
8. If you wish you can see the relationship between them accessing the diagrom of the entities in this link: https://dbdiagram.io/d/63ba00e47d39e42284e988e0
9. To access any of the APIs, just throw at your browser http://localhost:8000/ + entity like http://localhost:8000/anuncio
10. In order to see the rutes available in any API add at the end of the link '/overview' like http://localhost:8000/anuncio/overview

That`s all! =D 
