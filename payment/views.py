# from django.shortcuts import render
# https://mpesa-fa.herokuapp.com/ | https://git.heroku.com/mpesa-fa.git

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .mpesa import payment
from .models import EntradasApi
import random
import string


def randomString(stringLength=6):
    """Generate a random string of fixed length """
    letters = string.ascii_uppercase
    word = ''.join(random.choice(letters) for i in range(stringLength))
    numberL = [random.randint(0, 9) for i in range(1)]
    word = word.replace(word[1],"{0}".format(numberL[0]))
    return word

@api_view(['POST'])
def c2b_api(request, format=None):
    if request.method == 'GET':
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        cad = EntradasApi(page="API Payment")  # @classmethod is used here
        cad.save()

        result = payment(
                method="C2B",
                api_key = request.data['api_key'],
                public_key = request.data['public_key'],
                msidsn=request.data['msidsn'],
                amount=request.data['amount'],
                # title=request.data['title'],
                # business=request.data['business'],
                thirdParty=randomString() # thirdParty,
            )
        return Response(result.body, status=result.status_code)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def b2c_api(request, format=None):
    if request.method == 'GET':
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        cad = EntradasApi(page="API Payment")  # @classmethod is used here
        cad.save()

        result = payment(
            method="B2C",
            api_key = request.data['api_key'],
            public_key = request.data['public_key'],
            msidsn=request.data['msidsn'],
            amount=request.data['amount'],
            # business='e-Compra',
            thirdParty=randomString() # thirdParty,
        )
        return Response(result.body, status=result.status_code)
    return Response(status=status.HTTP_400_BAD_REQUEST)
