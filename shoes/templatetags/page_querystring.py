from django import template



register = template.Library()

@register.filter()

def page_querystring(get, page):
    '''
    Template filter to update/set the page= and render as a querystring
​
    {{ request.GET|page_querystring:page_number }}
    '''
    qd = get.copy()
    qd['page'] = page

    return qd.urlencode()