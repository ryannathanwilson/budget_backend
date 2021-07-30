from django.shortcuts import render
from .serializers import UserSerializer, ExpensesSerializer, ExpenseCategoriesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Expenses, ExpenseCategories, Budget
import json
from datetime import datetime


# Create your views here.
class ExpenseView(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)



@api_view(['GET'])
def get_money_data(request):
    # initialize dictionaries
    moneyData = {}              # return this
    thisMonthBudget = {}        
    thisMonthExpenses = {}
    totalRemainingBudget = {}   # sum of all budget minus all expenses
    
    # get list of categories
    categories = ExpenseCategories.objects.all()

    # create dictionary structure
    for c in categories:
        cat = c.category
        thisMonthBudget[cat] = 0
        thisMonthExpenses[cat] = 0
        totalRemainingBudget[cat] = 0 

    # get current date
    today = datetime.today()
    thisMonth = today.month
    thisYear = today.year

    budget = Budget.objects.all() # query all budget data

    for b in budget:
        cat = b.category.category
        month = b.date.month
        year = b.date.year

        # put current month data into thisMonth Budget
        if month == thisMonth and year == thisYear:
            thisMonthBudget[cat] = b.budgeted_money
        
        # sum all budgeted_money
        totalRemainingBudget[cat] += b.budgeted_money

    expenses = Expenses.objects.all() # query all expenses data

    for e in expenses:
        cat = e.category.category
        month = e.date.month
        year = e.date.year

        if month == thisMonth and year == thisYear:
            thisMonthExpenses[cat] += e.expense
    
        # subtract all expenses
        totalRemainingBudget[cat] -= e.expense
    
    # assemble data into moneyData dictionary
    for c in categories:
        cat = c.category
        moneyData[cat] = {
            "thisMonthBudget": str(thisMonthBudget[cat]),
            "thisMonthExpenses": str(thisMonthExpenses[cat]),
            "totalRemainingBudget": str(totalRemainingBudget[cat]),
        }
   
    return Response(json.dumps(moneyData))


# @api_view(['GET'])
# def all_balances(request):
# """
# return all categories, and remaining money for the month.
# """
# 	# todo: query expense categories
# 	queryset =

# 	return Response(serializer.data)
