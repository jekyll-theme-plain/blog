<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{{ site.title }}</title>
  </head>
  <body>
    <ul>
    {% for page in site.pages %}
      <li>
        <a href="{{ page }}">{{ page }}</a>
      </li>
    {% endfor %}
    </ul>
  </body>
</html>
