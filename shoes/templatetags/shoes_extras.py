from django import template



register = template.Library()

@register.filter(name='getUserState')
def getUserState(shoe, user):
    
    return shoe.checkItemState(user)