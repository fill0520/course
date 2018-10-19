from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Course, Contact, Branch, Category

class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = ('latitude', 'longtitude', 'address')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('type', 'value')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    
    branches = BranchSerializer(many=True)
    contacts = ContactSerializer(many=True)
    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'category', 'logo', 'contacts', 'branches')

    def create(self, validated_data):
        course_contact = validated_data.pop('contacts')
        course_branch = validated_data.pop('branches')
        course = Course.objects.create(category = Category.objects.get(pk=1),**validated_data)
        for data in course_contact:
            Contact.objects.create(course = course, **data)
        for data in course_branch:
            Branch.objects.create(course = course, **data)
        return course
