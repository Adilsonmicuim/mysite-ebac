# Importações
import factory
from django.contrib.auth.models import User
from blog.models import Post


# Factory para User
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user_{n}')
    email = factory.Sequence(lambda n: f'user_{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'password')


# Factory para Post
class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = 'Test Post'
    slug = 'test-post'
    author = factory.SubFactory(UserFactory)
    content = 'Test content'
    status = 0
