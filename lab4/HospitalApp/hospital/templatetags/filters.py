from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name='client'):
    return user.groups.filter(name=group_name).exists()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
