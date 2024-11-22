import jinja2

def print_mails():
    environment = jinja2.Environment()
    template = environment.from_string("Hello, {{ name }}!\n")

    for word in ["Alice", "Bob", "Charlie"]:
        print(template.render(name=word))

print_mails()

def print_texts():
    environment = jinja2.Environment()
    template = environment.from_string("{% for text in texts %}{{ text }}{% endfor %}")

    texts = ["Luke is a Jedi", "Vader is a Sith", "Han shot first"]

    print(template.render(texts=texts))

print_texts()