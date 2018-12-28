from django import template
from radio4all.models import Types, License

register = template.Library()

@register.inclusion_tag('radio4all/browsenav.html')
def get_categories():
    types = Types.objects.all()
    licenses = License.objects.all()
    return {'categories': types, 'licenses':licenses }
