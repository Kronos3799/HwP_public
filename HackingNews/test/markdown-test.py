from markdown import markdown

def test_markdown():
    # convert markdown from file to html
    with open('markdown.md', 'r') as f:
        markdown_text = f.read()
        html = markdown(markdown_text)
        print(html)

if __name__ == '__main__':
    test_markdown()