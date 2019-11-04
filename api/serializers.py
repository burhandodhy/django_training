from rest_framework import serializers
from authenticate.models import CustomUser
from rest_framework.response import Response
from rest_framework.validators import UniqueTogetherValidator



class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
      model = CustomUser
      fields = ['id', 'username', 'email', 'first_name', 'last_name', 'state', 'country']

    def validate_email(self, value):

      if self.context['request'].method == 'POST' and CustomUser.objects.filter(email=value).exists():
        raise serializers.ValidationError("Email already exists")

      if self.context['request'].method == 'PATCH':
        if value != self.context['request'].user.email and CustomUser.objects.filter(email=value).exists():
          raise serializers.ValidationError("Email already exists")

      return value

    def validate_username(self, value):

      # Not allow to update the username
      if self.context['request'].method == 'PATCH':
        if value != self.context['request'].user.username:
          raise serializers.ValidationError("Cant update username")
      return value
