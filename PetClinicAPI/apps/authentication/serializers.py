from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=False, write_only=True)
    role = serializers.ChoiceField(
        choices=User.RoleChoices.choices, default=User.RoleChoices.OPERATOR
    )

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.save()

        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.role = validated_data.get("role", instance.role)

        if "password" in validated_data:
            instance.set_password(validated_data["password"])

        instance.save()

        return instance

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "role", "password")
        validators = [
            UniqueTogetherValidator(queryset=User.objects.all(), fields=["email"])
        ]
        ref_name = None


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user_role"] = user.role
        return token
