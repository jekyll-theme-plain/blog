<ul>{% for page in site.pages %}{% if page.categories contains 'posts' %}
      <li>
        <a href="{{ page.url }}">{{ page.url }} | {{ page.title }} | {{ page.name }}</a>
      </li>{% endif %}{% endfor %}
    </ul>
