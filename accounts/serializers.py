# from rest
# from rest_framework import serializers
# from django.contrib.auth.models import User
# class UserSignupSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = "__all__"

#     # def create(self, validated_data):
#     #     user = User.objects.create_user(
#     #         username=validated_data['username'],
#     #         password=validated_data['password'],
#     #         email=validated_data.get('email'),
#     #         full_name=validated_data.get('full_name')
#     #     )
#     #     return user
# class UserSigninSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
# class UserUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'full_name']


from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):  #converting complex data such as querysets and models into native python datatypes
    #password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = "__all__"