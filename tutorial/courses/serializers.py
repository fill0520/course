from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Course, Contact, Branch

class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = ('latitude', 'longtitude', 'address')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('type', 'value')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    
    branches = BranchSerializer(many=True)
    contacts = ContactSerializer(many=True)
    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'category', 'logo', 'contacts', 'branches')
