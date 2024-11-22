import jinja2

def print_mails():
    environment = jinja2.Environment()
    template = environment.from_string("Hello {{ name }}!\n}"
                                       "How are you doing?\n\n")
    
    for word in ["Alice", "Bob", "Charlie"]:
        print(template.render(name=word))

print_mails()

def print_text():
    environment = jinja2.Environment()
    template = environment.from_string("{% for text in texts %}"
                                       "{{ text }}"
                                       "{% endfor %}")

    texts = ["Hello! ", "How are you doing? ", "Goodbye."]

    print(template.render(texts=texts))

print_text()