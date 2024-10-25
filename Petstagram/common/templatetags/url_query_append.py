from django import template

register = template.Library()


@register.simple_tag
def url_query_append_tag(request, field, value):
    dict_ = request.GET.copy()  # -> {'pet_name': 'George', 'page': 2}
    dict_[field] = value
    return dict_.urlencode()  # -> ?pet_name=george
