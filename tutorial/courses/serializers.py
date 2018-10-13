from rest_framework import serializers
from courses.models import Course, LANGUAGE_CHOICES, STYLE_CHOICES


class CourseSerializer(serializers.Serializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'category', 'logo')
    

    def create(self, validated_data):
        """
        """
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """

        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.save()
        return instance
