from django.shortcuts import render
from .serializers import UserSerializer, ExpensesSerializer, ExpenseCategoriesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Expenses, ExpenseCategories
import json


# Create your views here.


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['GET'])
def get_money_data(request):
    categories = ExpenseCategoriesSerializer(
        ExpenseCategories.objects.all(), many=True)
    # expenses = ExpensesSerializer(Expenses.objects.select_related('category').all(), many=True)
    expenses = Expenses.objects.all()
    totalExpenses = {}
    for e in expenses:
        if e.category.category in totalExpenses:
            totalExpenses[e.category.category] += e.expense
        else:
            totalExpenses[e.category.category] = e.expense
    for key in totalExpenses:
        totalExpenses[key] = str(totalExpenses[key])
    print(totalExpenses)
    return Response(json.dumps(totalExpenses))


# @api_view(['GET'])
# def all_balances(request):
# """
# return all categories, and remaining money for the month.
# """
# 	# todo: query expense categories
# 	queryset =

# 	return Response(serializer.data)
