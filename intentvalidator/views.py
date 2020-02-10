from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from intentvalidator.CoreValidationLogic.logic import *


# Create your views here.
@api_view(['GET'])
def welcome(request):
    result = "Welcome to Intention Validation Service"
    response = Response(result, status=status.HTTP_200_OK)
    return response


@api_view(['GET', 'POST'])
def validate_finite_values_entity(request):
    if request.method == 'GET':
        return Response({"message": "This is where validate_finite_values_entity api is hosted!"})

    data = request.data
    try:
        t = validate_finite_wrapper(data)
    except:
        error = "Bad Request made due to one or more of the following reasons\nRequired keys are missing from the " \
                "payload "
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    response = Response(t, status=status.HTTP_200_OK)
    return response


@api_view(['GET', 'POST'])
def validate_numeric_entity(request):
    if request.method == 'GET':
        return Response({"message": "This is where validate_numeric_entity api is hosted!"})
    data = request.data
    try:
        t = validate_numeric_wrapper(data)
    except:
        error = "Bad Request made due to one or more of the following reasons\nRequired keys are missing from the " \
                "payload\nData type is incorrect\nConstraint provided is not a valid boolean expression"
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    response = Response(t, status=status.HTTP_200_OK)
    return response
