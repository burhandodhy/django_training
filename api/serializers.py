from rest_framework import serializers
from authenticate.models import CustomUser
from rest_framework.response import Response
from rest_framework.validators import UniqueTogetherValidator



class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
      model = CustomUser
      fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'state', 'country']
      extra_kwargs = {
          'password': {'write_only': True}
      }

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


    def create(self, validated_data):
      username = validated_data.get('username')
      email = validated_data.get('email')
      password = validated_data.get('password')
      first_name = validated_data.get('first_name')
      last_name = validated_data.get('last_name')
      state = validated_data.get('state')
      country = validated_data.get('country')

      user = CustomUser.objects.create_user(
          username=username, password=password, email=email, first_name=first_name, last_name=last_name, state=state, country=country )
      return user

