from django.db import models


class Member(models.Model):
    memberid = models.AutoField(primary_key=True, editable=False)
    membername = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'members'

class Book(models.Model):
    bookid = models.AutoField(primary_key=True, editable=False)
    bookname = models.CharField(max_length=100)
    numberofcopies = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'books'

class Circulation(models.Model):
    bookid = models.AutoField(primary_key=True, editable=False)
    memberid = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'circulation'

class Reservation(models.Model):
    bookid = models.AutoField(primary_key=True, editable=False)
    memberid = models.CharField(max_length=100)
    reservation_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'reservation'