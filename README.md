# Vernacular Intention validator

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This project intendes to validates intention behind the utterance. It's a basic Django app which three POST Apis
  - validate_finite_entity : https://localhost:8000/validateFiniteEntity
  - validate_num_entity: https://localhost:8000/validateNumEntity
  - Slot_Validation: https://localhost:8000/slotValidate

Futher information can found in _problem statetment.txt_

# Assumptions
* If pick_first is present, it will simply overide the behaviour of support_multiple key and first value will be picked regardless the entity value is valid or not
* Constraint is considered to be boolean or bad request response is thrown

# Instructions
* Inside the project directory  run
```
docker-compose up
```
