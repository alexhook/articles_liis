from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsAuthor, IsSubscriber, IsOwner

class AuthorToolsViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get_permissions(self):
        permission_classes = []

        if self.action == 'create':
            permission_classes = [IsAuthor]
        elif self.action in ['update', 'destroy']:
            permission_classes = [IsAuthor&IsOwner]
        
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PublicArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(is_private=False)
    serializer_class = ArticleSerializer

class PrivateArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(is_private=True)
    serializer_class = ArticleSerializer
    permission_classes = [IsSubscriber|IsAuthor]
