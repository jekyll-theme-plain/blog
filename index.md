<ul>{% for page in site.pages %}{% if page.categories contains 'posts' %}
      <li>
        <a href="{{ page.url }}">{{ page.name | remove_first ".md" }}</a>
      </li>{% endif %}{% endfor %}
    </ul>
