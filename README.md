## 4EHEALTH Medical Management System  - 4EHEALTH MMS v1.0

4EHEALTH MMS v.1.0 is a web application to solve adminisitrative and managament challenges in the healthcare sector by automating the processes within all departments, entities, activities and assests.

Note: This is a required technical assessment for ehealth4everyone application.

### Technology Stack
- Django and Bootstrap
 
### Execution Setup
- `git clone https://github.com/moreshud/ehealth.git`
- `cd ehealth` and ensure you have `virtualenv` installed else `pip install virtualenv`
- Setup your virtualenv `source virtualenv venv` and activate with `source venv/bin/activate`
- Install necessary dependencies `pip3 install -r requirement.txt`
- Run and respone to prompts: `python manage.py createsuperuser`, `python manage.py makemigrations`, `python manage.py migrate`
- Finally, `python manage.py runserver`

### Completed Features
- Authentication module - sign-in, sign-out for user entities
- Patient/Doctor mini analytics
- Patient profile completion and updates
- Patient medics reporting and appointment booking
- Doctor appointment approval

### Outstandings
- Patient medics/appointment search feature
- Doctor appointment email notification
- General QA checks and cleanup.
