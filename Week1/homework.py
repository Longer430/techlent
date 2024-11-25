from flask import Flask, make_response
from yattag import Doc

app = Flask(__name__)

def generate_html(title, heading, content, link_text, link_url):
    doc, tag, text = Doc().tagtext()

    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            with tag('title'):
                text(title)
            with tag('style'):
                text('body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }')
        with tag('body'):
            with tag('h1'):
                text(heading)
            with tag('p'):
                text(content)
            with tag('a', href=link_url):
                text(link_text)

    return doc.getvalue()

@app.route('/')
def home():
    return make_response(generate_html(
        title="My Simple Flask App",
        heading="Welcome to My Flask App",
        content="This is a simple webpage served by Flask and generated with Yattag.",
        link_text="Say Hello",
        link_url="/hello"
    ))

@app.route('/hello')
def hello():
    return make_response(generate_html(
        title="Hello Page",
        heading="Hello, Flask!",
        content="This is another simple page generated with Yattag.",
        link_text="Go Back Home",
        link_url="/"
    ))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)