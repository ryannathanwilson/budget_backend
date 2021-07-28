from django.db import models
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    family = models.ForeignKey('Families', on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)

class Families(models.Model):
	family = models.CharField(max_length=63)

	def __str__(self):
		return f"{self.family}"

class Budget(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default='ryannathanwilson')
	date=models.DateField()
	category=models.ForeignKey('ExpenseCategories', on_delete=models.CASCADE)
	budgeted_money=models.DecimalField(max_digits=8, decimal_places=2)
	notes=models.CharField(max_length=255) # todo: not required field
        
	def __str__(self):
		return f"{self.budgeted_money} from category: {self.category} on {self.date}"


class Expenses(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	date = models.DateField()
	expense=models.DecimalField(max_digits=8, decimal_places=2)
	category=models.ForeignKey('ExpenseCategories', on_delete=models.CASCADE)
	vendor=models.CharField(max_length=100)
	notes=models.CharField(max_length=255)

	def __str__(self):
		return f"{self.expense} from category: {self.category} from store: {self.vendor}"

class Income(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	date = models.DateField()
	income=models.DecimalField(max_digits=8, decimal_places=2) 
	category=models.ForeignKey('IncomeCategories', on_delete=models.CASCADE) # todo: what is CASCADE
	notes=models.CharField(max_length=255)

	def __str__(self):
		return f"{self.expense} from category: {self.category} from store: {self.store}"
	
class ExpenseCategories(models.Model):
	category=models.CharField(max_length=20)

	def __str__(self):
		return f"{self.category}"


class IncomeCategories(models.Model):
	category=models.CharField(max_length=20)

	def __str__(self):
		return f"{self.category}"