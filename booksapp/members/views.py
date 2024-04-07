from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
# Create your views here.
from rest_framework import viewsets

from .models import Member, Book, Circulation, Reservation

from .serializers import MemberSerializer, BookSerializer

class CheckoutView(APIView):
  def get(self, request):
    book_id = request.GET.get('book_id')
    member_id = request.GET.get('member_id')
    book = Book.objects.get(bookid=book_id)
    if book.numberofcopies > 0:
      book.numberofcopies -= 1
      book.save()
      circulation = Circulation.objects.create(bookid=book_id, memberid=member_id)
      return Response({"response": "Book has been checked out successfully"})
    else:
      rs = Reservation.objects.create(bookid=book_id, memberid=member_id, reservation_date=datetime.date.today())
      return Response({"response": "There are no books available. A reservation request has been initiated."})
    
class ReturnView(APIView):
  def get(self, request):
    book_id = request.GET.get('book_id')
    member_id = request.GET.get('member_id')
    book = Book.objects.get(bookid=book_id)
    circulation = Circulation.objects.get(bookid=book_id, memberid=member_id).delete()
    book.numberofcopies += 1
    return Response({"response": "Book has been returned successfully."})


class FulfillView(APIView):
  def get(self, request):
    book_id = request.GET.get('book_id')
    book = Book.objects.get(bookid=book_id)
    book.numberofcopies += 1
    first_reservation = Reservation.objects.get(bookid=book_id).order_by('reservation_date')[0]

    first_reservation.delete()
    return Response({"response": "Resercation request has been fulfilled successfully."})

