<h1>{{ site.title }}</h1>
<ul>
{% for article in site.html_pages %}
  <li>
    <a href="{{ article.url }}">{{ article.title }} {{ article.url }} {{ article.name }}</a>
  </li>
{% endfor %}
</ul>
