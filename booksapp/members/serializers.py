from rest_framework import serializers

from .models import Member, Book

class MemberSerializer(serializers.ModelSerializer):
    class Meta:

        model = Member

        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:

        model = Member

        fields = '__all__'