from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
import datetime
from django.core.validators import RegexValidator

HOUSE_CLASSES = (
    ("1", "эконом"),
    ("2", "комфорт"),
    ("3", "премиум"),
)

HOUSE_STATUSES = (
    ("1", "сдан"),
    ("2", "строится"),
)

AVAILABILITY = (
    ("1", "есть"),
    ("2", "проданы"),
)

YEAR = []
for y in range(1990, (datetime.datetime.now().year + 10)):
    YEAR.append((y, y))

FOUNDATION_YEAR = []
for y in range(1990, datetime.datetime.now().year):
    FOUNDATION_YEAR.append((y, y))

PHONE_REGEX = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)


class Developer(models.Model):
    name = models.CharField('Название строительной компании', max_length=100, blank=False)
    site = models.CharField('Сайт', max_length=100)
    foundation_year = models.IntegerField('Дата основания', choices=FOUNDATION_YEAR, default=datetime.datetime.now().year)
    phone_number = models.CharField('Номер телефона', validators=[PHONE_REGEX], max_length=17)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Developers"


class House(models.Model):
    name = models.CharField('Имя', max_length=100, blank=False)
    year = models.IntegerField('Год ввода в эксплуатацию', choices=YEAR, default=datetime.datetime.now().year)
    number_of_floors = models.PositiveIntegerField('Этажность')
    number_of_apartments = models.PositiveIntegerField('Кол-во квартир')
    house_class = models.CharField('Класс', max_length=100, choices=HOUSE_CLASSES)
    status = models.CharField('Статус дома', max_length=100, choices=HOUSE_STATUSES)
    availability_of_apartments = models.CharField('Наличие квартир', max_length=100, choices=AVAILABILITY)
    address = models.CharField('Адрес', max_length=100)

    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Houses"
