from django.conf import settings
from django.core.mail import send_mail
from rest_framework import serializers

from .models import Contact, OrderService


class ContactSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=200)
    phone = serializers.CharField(max_length=20)
    text = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        left_message = Contact.objects.create(**self.validated_data)

        content = left_message.text + "\n\nот:       " \
                                      " " + left_message.first_name + " " + left_message.last_name + "\nemail: " \
                                      " " + left_message.email + "\nтел:     " + left_message.phone

        send_mail(subject='У меня есть крутая идея!',
                  message=content,
                  from_email='aycanmuratbekova@gmail.com',
                  recipient_list=['ariet.muratbekov.dev@gmail.com']
                  )
        left_message.save()
        return left_message


class OrderServiceSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=200)
    phone = serializers.CharField(max_length=20)
    text = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        left_message = OrderService.objects.create(**self.validated_data)

        content = left_message.text + "\n\nот:       " \
                                      " " + left_message.first_name + " " + left_message.last_name + "\nemail: " \
                                      " " + left_message.email + "\nтел:     " + left_message.phone

        send_mail(subject='Хотим оформить заказ.',
                  message=content,
                  from_email='aycanmuratbekova@gmail.com',
                  recipient_list=['aycanmuratbekova@gmail.com']
                  )
        left_message.save()
        return left_message
