## 4EHEALTH Medical Management System  - 4EHEALTH MMS v1.0

4EHEALTH MMS v.1.0 is a web application to solve adminisitrative and managament challenges in the healthcare sector by automating the processes within all departments, entities, activities and assests.

Note: This is a required technical assessment for ehealth4everyone application.

### Technology Stack
- Django and Bootstrap
 
### Execution Setup
1. `git clone https://github.com/moreshud/ehealth.git`
2. `cd ehealth` and ensure you have `virtualenv` installed else `pip install virtualenv`
3. Setup your virtualenv `source virtualenv venv` and activate with `source venv/bin/activate`
4. Install necessary dependencies `pip3 install -r requirement.txt`
5. Run and respone to prompts: `python manage.py createsuperuser`, `python manage.py makemigrations`, `python manage.py migrate`
6. Finally, `python manage.py runserver`

### Completed Features
- Authentication module - sign-in, sign-out for user entities
- Patient mini analytics
- Patient profile completion and updates
- Patient medics reporting and appointment booking

### Outstandings
- Patient medics/appointment search feature
- Doctor mini analytics
- Doctor appointment email notification and approval
- General QA checks and cleanup.
