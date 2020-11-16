from django.conf import settings
from django.db import transaction
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Student, Company, Admin


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username',)


class BaseUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    default_error_messages = {
        "cannot_create_user": settings.CONSTANTS.messages.USER_CANNOT_CREATE
    }

    class Meta:
        model = User
        type = None
        fields = ('id', 'email', 'username', 'password',)
        abstract = True

    def validate(self, attrs):
        user = self.Meta.model(**attrs, type=self.Meta.type)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )

        return attrs

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = self.Meta.model.objects.create_user(**validated_data)
            # if settings.SEND_ACTIVATION_EMAIL:
            #     user.is_active = False
            #     user.save(update_fields=["is_active"])
        return user


# STUDENT
# ------------------------------------------------------------------------------
class StudentCreateSerializer(BaseUserCreateSerializer):

    class Meta:
        model = Student
        type = User.TYPES.STUDENT


# COMPANY
# ------------------------------------------------------------------------------
class CompanyCreateSerializer(BaseUserCreateSerializer):

    class Meta:
        model = Company
        type = User.TYPES.COMPANY


# Admin
# ------------------------------------------------------------------------------
class AdminCreateSerializer(BaseUserCreateSerializer):

    class Meta:
        model = Admin
        type = User.TYPES.ADMIN
