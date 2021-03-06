from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = ('email', 'role', 'password')
        extra_kwargs = {
            'role': {'write_only': True},
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)

        user.set_password(password)
        user.save()

        return user