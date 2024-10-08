from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from .models import Post

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
   created_date = DateFilter(
       field_name='created_date',
       widget=DateInput(attrs={'type': 'date'}),
       lookup_expr='date__gte',
       label='Поиск по дате'
   )

   class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'author': ['exact'],
           'category': ['exact'],
            }



