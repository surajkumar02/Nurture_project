# Nurture_project
Link: https://nurture-assignment.herokuapp.com

Python-Django with DRF and simplejwt


for linux 

      python3 -m pip install --user virtualenv
      python3 -m venv env
      source env/bin/activate

for windows

      py -m pip install --user virtualenv 
      py -m venv env
      ./env/Scripts/activate OR ./env/Scripts/activate.bat (if not working)


Intall Dependencies:

    - pip install django
    - pip install djangorestframework
    - pip install djangorestframework_simplejwt
    
for Authentication - make hidden permission_classes visible (remove '#' or 'Ctrl+/')

urls:

      METHOD = GET
      
      - /user/<user-id>/advisor
          O/P:  An array of advisor objects with each object having
                  Advisor Name
                  Advisor Profile Pic
                  Advisor Id

      
      - /user/<user-id>/advisor/booking/
          O/P: An array of advisor objects with each object having
                  Advisor Name
                  Advisor Profile Pic
                  Advisor Id
                  Booking time
                  Booking id


      METHOD = POST
      
      - /admin/advisor/ 
              data= {
              Advisor name:
              Advisor Photo URL:
              }
              
      - /user/register/ 
              data= {
              Name:
              Email:
              Password:
              }
            
      - /user/login/
              data= {
              Email:
              Password:
              }
      - /user/<user-id>/advisor/<advisor-id>/
              data={
              Booking Time:format=(YYYY,MM,DD,HH,MM,SS)(24HRS Clock)  eg. (2021,12,01,13,00,00)
