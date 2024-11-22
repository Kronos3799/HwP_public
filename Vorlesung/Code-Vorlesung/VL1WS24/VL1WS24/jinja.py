import jinja2


def print_mails():
    environment = jinja2.Environment()
    template = environment.from_string("Hello, {{ name }}!\n"
                                       "How are you doing\n\n")

    for word in ["Luke", "Anakin", "Vador"]:
        print(template.render(name=word))

print_mails()

def print_text():
    environment = jinja2.Environment()
    template = environment.from_string("{% for text in texts %} {{ text }} {% endfor %}")

    texts = ["Luke is a Jedi", "Darth is a Sith", "Han is a warrior"]

    print(template.render(texts=texts))
    
print_text()