from django import template
register = template.Library()
def foo(value,arg):
    return value.replace(arg,'')
register.filter('foo',foo)
