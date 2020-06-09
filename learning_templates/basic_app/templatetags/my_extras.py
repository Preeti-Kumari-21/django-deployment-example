from django import template

register = template.Library()
@register.filter(name='cut')

def cut(value,arg):
    """
    Thus cuts all the values of "arg" from the string
    """
    return value.replace(arg,'')

register.filter('cut',cut)
