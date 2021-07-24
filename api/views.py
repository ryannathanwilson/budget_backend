from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.


@api_view(['GET'])
def current_user(request):
	"""
	Determine the current user by their token, and return their data
	"""

	serializer = UserSerializer(request.user)
	return Response(serializer.data)


# @api_view(['GET'])
# def all_balances(request):
# """
# return all categories, and remaining money for the month.
# """
# 	# todo: query expense categories
# 	queryset = 

# 	return Response(serializer.data)