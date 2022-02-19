<ul>{% for page in site.pages %}{% if page.categories contains 'posts' %}
      <li>
        <a href="{{ page.url }}">{{ page.url }} | {{ page.path }} | {{ page.name }}</a>
      </li>{% endif %}{% endfor %}
    </ul>
