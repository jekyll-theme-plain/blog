<ul>{% for page in site.pages %}{% if page.categories contains 'posts' %}
      <li>
        <a href="{{ page.url }}">{{ page.url }} | {{ page.slug }} | {{ page.title }} | {{ page.basename }} | {{ page.name }}</a>
      </li>{% endif %}{% endfor %}
    </ul>
