from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField


# Create your models here.
class User(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	birthDate = models.DateField()

class Address(models.Model):
	firstName = models.CharField(max_length=255)
	lastName = models.CharField(max_length=255)
	company = models.CharField(max_length=255)
	phoneNumber = models.CharField(max_length=255)
	address1 = models.CharField(max_length=255)
	address2 = models.CharField(max_length=255)
	address3 = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	stateOrRegion = models.CharField(max_length=255)
	postalCode = models.CharField(max_length=255)
	country = models.CharField(max_length=255)
	facturationDefault = models.BooleanField()
	deliveryDefault = models.BooleanField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.lastName

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	image = models.CharField(max_length=255, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.name

	def nameToUrl(self):
		return self.name.replace(' ','-')

class Order(models.Model):
	number = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=255)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	deliveryAddress = models.ForeignKey(Address, on_delete=models.CASCADE,related_name='user_deliveryAddress')
	billingAddress = models.ForeignKey(Address, on_delete=models.CASCADE,related_name='user_billingAddress')
	products = models.ManyToManyField(Product, through='Order_Product')

	def __str__(self):
		return self.number

class Order_Product(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=19, decimal_places=2)
	size = models.CharField(max_length=255)
	quantity = models.IntegerField()
	property = models.CharField(max_length=255)
	barCode = models.CharField(max_length=255)

class Flavour(models.Model):
	name = models.CharField(max_length=255,null=True)
	picture = models.CharField(max_length=255,null=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Size(models.Model):
	name = models.CharField(max_length=255,null=True)
	unit = models.CharField(max_length=255,null=True)
	price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='EUR',
        max_digits=11,
    )
	product = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
		return self.name