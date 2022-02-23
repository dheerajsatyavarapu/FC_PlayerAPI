# FC_PlayerAPI

This application is a **REST API** regarding Football Players which has two endpints i.e.,
1. [localhost:8080/playerstats](localhost:8080/playerstats): 
Fetches all the players with overall score greater than 90
2. [localhost:8080/countrystats](localhost:8080/countrystats): 
Fetches average overall score of players grouped by country

### Backend Info:
#### Technology Used: Django REST Framework
#### Application Flow :
1. Request from end point
2. urls.py-> views.py (Class Based inherited from APIView)
3. Query Set retrieval from django models using Django ORM
4. Serialize retrieved Queryset to JSON format
5. Sending response to endpoint. 

### How to Use:
1. Set up a virtual environiment
2. Clone this repository and change directory(cd) to root folder of repo.
3. run requirements.txt file using `pip install -r requiremnts.txt` 
4. Make Migrations: `python manage.py makemigrations` `python manage.py migrate`.
5. Create Superuser: `python manage.py createsuperuser`.
6. Run Server `python manage.py runserver`.
7. Now you are ready to check above mentioned two endpoints. 


