<ul>
{% for article in site.articles %}
  <li>
    <a href="{{ article.title }}">{{ article.title }}</a>
  </li>
{% endfor %}
</ul>
