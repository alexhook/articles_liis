from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='email', read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'owner', 'is_private']
        read_only_fields = ['id', ]
        extra_kwargs = {
            'is_private': {'write_only': True},
        }