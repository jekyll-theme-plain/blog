<h1>{{ site.title }}</h1>
<ul>
{% for page in site.pages %}
{% if page.categories contains 'articles' %}
  <li>
    <a href="{{ page.url }}">{{ page.url }}</a>
  </li>
{% endif %}
{% endfor %}
</ul>
