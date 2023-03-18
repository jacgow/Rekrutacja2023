from django.db import models


# Create your models here.

class Candidate(models.Model):
    # Candidate data/ dane kandydata
    id_candidate = models.AutoField(Field.primary_key)
    name1 = models.CharField(max_length=100, verbose_name='Imię1')
    name2 = models.CharField(max_length=100, verbose_name='Imię2')
    last_name = models.CharField(max_length=100, verbose_name='Nazwisko')
    data_of_brith = models.DateTimeField(verbose_name='Data urodzenia')
    place_of_birth = models.CharField(max_length=100, verbose_name='Miejsce urodzenia')
    PESEL = models.IntegerField(max_length=11, verbose_name='PESEL')
    # Candidate's address details
    country_C = models.CharField(max_length=100, verbose_name='Kraj')
    state_c = models.CharField(max_length=100, verbose_name='Wojewodztwo')
    city_c = models.CharField(max_length=100, verbose_name='Miasto')
    street_c = models.CharField(max_length=100, verbose_name='Ulica')
    nr_hous_c = models.CharField(max_length=100, verbose_name='Nr domu')
    nr_apartment_c = models.IntegerField(max_length=11, verbose_name='Nr mieszkania')
    zip_cod_c = models.IntegerField(max_length=6, verbose_name='Kod pocztowy')
    post_c = models.CharField(max_length=100, verbose_name='Poczta')
    same_address = models.BooleanField()
    # Data of the candidate's guardians/ dane opiekunów
    name_guardians1 = models.CharField(max_length=100, verbose_name='Imię opieuna1')
    last_name_guardians1 = models.CharField(max_length=100, verbose_name='Nazwisko opieuna1')
    telephone_guardians1 = models.IntegerField(max_length=12, verbose_name='Telefon opieuna1')
    email_guardians1 = models.EmailField(verbose_name='email opieuna1')
    name_guardians2 = models.CharField(max_length=100, verbose_name='Imię opieuna2')
    last_name_guardians2 = models.CharField(max_length=100, verbose_name='Nazwisko opieuna2')
    telephone_guardians2 = models.IntegerField(max_length=12, verbose_name='Telefon opieuna2')
    email_guardians2 = models.EmailField(verbose_name='email opieuna2')
    # address details of the Guardians
    country_g = models.CharField(max_length=100, verbose_name='Kraj')
    wojewodztwo_g = models.CharField(max_length=100, verbose_name='Wojewodztwo')
    city_g = models.CharField(max_length=100, verbose_name='Miasto')
    street_g = models.CharField(max_length=100, verbose_name='Ulica')
    nr_hous_g = models.CharField(max_length=100, verbose_name='Nr domu')
    nr_apartment_g = models.IntegerField(max_length=11, verbose_name='Nr mieszkania')
    zip_cod_g = models.IntegerField(max_length=6, verbose_name='Kod pocztowy')
    post_g = models.CharField(max_length=100, verbose_name='Poczta')