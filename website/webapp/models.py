from django.db import models
from django.contrib.auth.models import User

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

class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	Caracteristics = models.CharField(max_length=255)

	def __str__(self):
		return self.name

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
	caracteristic = models.CharField(max_length=255)
	barCode = models.CharField(max_length=255)

class Category(models.Model):
	name = models.CharField(max_length=255)
	products = models.ManyToManyField(Product)

	def __str__(self):
		return self.name