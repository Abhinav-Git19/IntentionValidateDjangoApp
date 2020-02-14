## Project
A Basic Django app with supports two POST Apis as follows
* validate_finite_values_entity : check if the values extracted lies within the finite list of supported values
* validate_numeric_entity : The method will check if that value satisfies the numeric constraints put on it

### Assumptions
#### validate_finite_values_entity

* If pick first and support-multiple both are present in json, pick_first overrides support-multiple and return parameters as string
* If pick first is enabled, we are showing the value regardless of whether that first value is valid or not
* Aforementioned assumptions apply similarly to *validate_numeric_entity*
* Keys for the request will be same, need to take care of value side of it.

#### validate_numeric_entity
* Using eval for constraint evaluation is a security risk, so we will be using simpleeval(https://pypi.org/project/simpleeval/)
for that which only accepts valid expressions otherwise it will raise exception.
* Also I am assuming constraint is only supposed to be valid boolean expression (only exception is empty expression which means no constraints) which will return either true or false, if its not the
case we must again raise bad request

## Instructions
* git clone the repository or unzip the file provided
* Go to project repository VernacularAssignment and run
```
docker-compose up
```
* Dockerfile, docker-compose.yml files and requirements.txt is already present and will take care of the rest of the dependencies

Note: When building for first time, docker may issue a warning for web service not being present for which it executes build command internally. You don't need to worry about that
* Once Server starts the App can be accessed from
http://localhost:8000/
* The two endpoints hosted are http://localhost:8000/validateFiniteEntity and http://localhost:8000/validateNumEntity and http://localhost:8000/slotValidate

* Image size: 977MB

### Automated Testing
* For your reference I have provided the automated test case for the endpoints
* They can be run from the project root directory VernacularAssignment as:
```
python manage.py test intentvalidator
```
* For further details on tests checkout the JSONfiles inside
```
intentvalidator/JSONfiles
```




