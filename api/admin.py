from django.contrib import admin
from .models import Profile, Families, Budget, Expenses, ExpenseCategories, Income, IncomeCategories

# Register your models here.

class ProfileAdmin (admin.ModelAdmin):
	list_display = ('user', 'bio', 'family')
	
class FamiliesAdmin (admin.ModelAdmin):
	pass
	# list_display = ('family')
	
class BudgetAdmin (admin.ModelAdmin):
	list_display = ('date', 'category', 'budgeted_money')
	
class ExpensesAdmin (admin.ModelAdmin):
	list_display = ('date', 'expense', 'category', 'vendor')
	
class IncomeAdmin (admin.ModelAdmin):
	list_display = ('date', 'income', 'category')
	
class ExpenseCategoriesAdmin (admin.ModelAdmin):
	pass
	# list_display = ('category')
	
class IncomeCategoriesAdmin (admin.ModelAdmin):
	pass
	# list_display = ('category')


# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Families, FamiliesAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(ExpenseCategories, ExpenseCategoriesAdmin)
admin.site.register(IncomeCategories, IncomeCategoriesAdmin)