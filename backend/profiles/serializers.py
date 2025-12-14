import os
from django.conf import settings
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        read_only_fields = ("owner",)

    def create(self, validated_data):
        photo = validated_data.pop("photo", None)
        person = Person.objects.create(**validated_data)

        if photo:
            ext = os.path.splitext(photo.name)[1]
            new_name = f"faces/image_{person.id}{ext}"
            new_path = os.path.join(settings.MEDIA_ROOT, new_name)

            os.makedirs(os.path.dirname(new_path), exist_ok=True)

            with open(new_path, "wb+") as destination:
                for chunk in photo.chunks():
                    destination.write(chunk)
            
            person.photo.name = new_name
            person.save(update_fields=["photo"])
        
        return person