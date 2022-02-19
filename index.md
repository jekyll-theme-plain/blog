<ul>{% for page in site.pages %}{% if page.categories contains 'posts' %}
      <li>
        <a href="{{ page.url }}">{{ page.url | remove_first: "/" }}</a>
      </li>{% endif %}{% endfor %}
    </ul>
