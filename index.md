<h1>{{ site.title }}</h1>
<ul>
{% for page in site.pages %}
  <li>
    <a href="{{ page.url }}">{{ page.url }} {{ page.categories }}</a>
  </li>
{% endfor %}
</ul>
