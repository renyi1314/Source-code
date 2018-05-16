import jinja2

template = jinja2.Template("hello {{ name }} !")

print(template.render(name="world"))
