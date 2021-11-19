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

