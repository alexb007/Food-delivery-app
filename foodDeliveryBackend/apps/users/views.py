from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

import requests

from .models import User
from .serializers import CreateUserSerializer, UserSerializer

CLIENT_ID = 'g6eBjRBlqL8jYNqe5G2KQDdoE9v4rnpEFQIcyeMr'
CLIENT_SECRET = 'BDbmthtkPSJsqgiQ92S8hEyPMXyjIb5MKj8pjaqt4ZWuU45yoCgZ0pXFA0IXQMJKvTO6tbIf4QXQ3xLH1vsyPGcSGHWh1y0LvZPZ8uYM7sOhgbx1NJMECJenBHGMWJab'
BASE_URL = 'http://15.188.194.70/o/'


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_customer(request):
    return create_user(request, False)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_restaurant(request):
    return create_user(request, True)


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password
    '''
    user = User.objects.filter(
        username__exact=request.data['username']).first()

    if user is None:
        return Response({'message': 'unauthorized'}, status=401)

    r = requests.post(
        BASE_URL + 'token/',
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )

    res = r.json()

    user = User.objects.filter(
        username__exact=request.data['username']).first()

    res['user_role'] = 'restaurant' if user.is_restaurant else 'customer'

    return Response(res, status=r.status_code)


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Registers user to the server.
    '''
    r = requests.post(
        BASE_URL + 'token/',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    '''
    r = requests.post(
        BASE_URL + 'revoke_token/',
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise)
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)


def create_user(request, is_restaurant):
    # Put the data from the request into the serializer
    serializer = CreateUserSerializer(data=request.data)
    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save(
            email=request.data['email'], is_restaurant=is_restaurant)
        # Then we get a token for the created user.
        # This could be done differentley
        r = requests.post(
            BASE_URL + 'token/',
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )

        res = r.json()

        res['user_role'] = 'restaurant'

        return Response(res)

    return Response(serializer.errors)
