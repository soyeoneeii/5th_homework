# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password
# from rest_framework import serializers


# #TokenObtainPairSerializer를 상속하여 클레임 설정
# class SpartaTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         #생성된 토큰 가져오기
#         token = super().get_token(user)

#         #사용자 지정 클레임 설정하기
#         token['id'] = user.id
#         token['username'] = user.username

#         return token
    


# # class RegisterSerializer(serializers.ModelSerializer):
# #     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
# #     password2 = serializers.CharField(write_only=True, required=True)

# #     class Meta:
# #         model = User
# #         fields = ('username', 'password', 'password2')
# #         extra_kwargs = {
# #             'username': {'required': True},
# #         }

# #     def validate(self, attrs):
# #         if attrs['password'] != attrs['password2']:
# #             raise serializers.ValidationError({"password": "Password fields didn't match."})

# #         return attrs

# #     def create(self, validated_data):
# #         user = User.objects.create(
# #             username=validated_data['username']
# #         )

# #         user.set_password(validated_data['password'])
# #         user.save()

# #         return user




from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'