{% for page in site.pages %}{% if page.categories contains 'posts' %}
    <a href="{{ page.url }}">{{ page.url | remove_first: "/" }}</a>{% endif %}{% endfor %}
