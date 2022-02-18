<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{{ site.title }}</title>
  </head>
  <body>
    <ul>
    {% for article in site.articles %}
      <li>
        <a href="{{ article.title }}">{{ article.title }}</a>
      </li>
    {% endfor %}
    </ul>
  </body>
</html>
