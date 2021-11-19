# DJANGO_SURVEY_API
## Task description
design and develop an API for a user survey system.
Functionality for the system administrator:

- authorization in the system (registration is not required)
- adding/changing/ deleting polls. Survey attributes: name, start date, end date, description. After creation, the "start date" field of the survey cannot be changed
- adding/changing/deleting questions in the survey. Question Attributes: question text, question type (answer in text, answer with a choice of one option, answer with a choice of several options)

Functionality for system users:
- getting a list of active polls
- passing the survey: surveys can be conducted anonymously, a numeric ID is transmitted to the API as a user ID, which stores the user's answers to questions; one user can participate in any number of surveys
- receiving surveys completed by the user with details on the answers (what is selected) by the unique user ID

Use the following technologies: Django 2.2.10, Django REST framework.
The result of the task:
- application source code in github (only on github, public repository)
-  instructions for deploying the application (in docker or locally)
-  API documentation

## installation
Clone this repo:
```html
   git clone https://github.com/jaymoz/DJANGO_SURVEY_API.git
```
Open the files in a code editor and create a virtual environment to install dependencies:
```html
   python -m venv Env
   pip install -r requirements.txt 
```
Create database and make migrations:
```html
   python manage.py makemigrations
   python manage.py migrate
```
Create a superuser to gain access to the database:
```html
   python manage.py createsuperuser
```
run the server:
```html
   python manage.py runserver
```

## API documentation
Get user Token:
```html
   http POST  http://127.0.0.1:8000/api-token-auth/ username=“YOUR_USERNAME" password=“YOUR_PASSWORD”
```
Create a survey:
- url: 
``` html
   http://127.0.0.1:8000/api/create-survey
  ```
Update a survey:
- url: 
``` html
   http://127.0.0.1:8000/api/update-survey/[id]/
  ```
Delete a survey:
- url: 
``` html
   http://127.0.0.1:8000/api/delete-survey/[id]/
  ```
View a survey:
- url: 
``` html
   http://127.0.0.1:8000/api/survey-detail/[id]/
  ```
View all surveys:
- url: 
``` html
   http://127.0.0.1:8000/api/survey-list
  ```
View all current surveys:
- url: 
``` html
   http://127.0.0.1:8000/api/active-survey
  ```
Create a question:
- url: 
``` html
   http://127.0.0.1:8000/api/create-question
  ```
Update a question:
- url: 
``` html
   http://127.0.0.1:8000/api/update-question/[id]/
  ```
Delete a question:
- url: 
``` html
   http://127.0.0.1:8000/api/delete-question/[id]/
  ```
View a question:
- url: 
``` html
   http://127.0.0.1:8000/api/question-detail/[id]/
  ```
Create a choice:
- url: 
``` html
   http://127.0.0.1:8000/api/create-choices
  ```
View a choice:
- url: 
``` html
   http://127.0.0.1:8000/api/choice-detail/[id]/
  ```
Update a choice:
- url: 
``` html
   http://127.0.0.1:8000/api/update-choice/[id]/
  ```
Delete a choice:
- url: 
``` html
   http://127.0.0.1:8000/api/delete-choice/[id]/
  ```
Create a response:
- url: 
``` html
   http://127.0.0.1:8000/api/response
  ```
View a response:
- url: 
``` html
   http://127.0.0.1:8000/api/response-detail/[id]/
  ```

Update a response:
- url: 
``` html
   http://127.0.0.1:8000/api/user-response/[id]/
  ```
Delete a response:
- url: 
``` html
   http://127.0.0.1:8000/api/delete-response/[id]/
  ```
Get all responses by user_id:
- url: 
``` html
   http://127.0.0.1:8000/api/user-response/[id]/
  ```
