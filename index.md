<h1>{{ site.title }}</h1>
<ul>
{% for article in site.articles %}
  <li>
    <a href="{{ article.url }}">{{ article.url }}</a>
  </li>
{% endfor %}
</ul>
