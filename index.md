<h1>{{ site.title }}</h1>
<ul>
{% for article in site.pages %}
  <li>
    <a href="{{ article.title }}">{{ article.title }}</a>
  </li>
{% endfor %}
</ul>
