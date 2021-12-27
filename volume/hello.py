from flask import Flask, render_template, render_template_string, request
from jinja2 import Template
app = Flask(__name__)

@app.route('/')
def wtf():
    name = request.args.get('name')
    t = Template(
            '''
            <html>
                <head>
                    <title>ADL SSTI Demo</title>
                </head>
                <body>
                    <p>Hello, %s</p>
                </body>
            </html>
            ''' % (name)
            )
    return t.render()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
