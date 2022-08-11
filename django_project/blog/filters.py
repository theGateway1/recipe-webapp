from xml.etree.ElementInclude import include
import django_filters
from django_filters import CharFilter
from .models import Post

class PostFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    ingredient = CharFilter(field_name='ingredients', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title']
        exclude = ['image']