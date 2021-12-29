from flask import Flask, render_template, render_template_string, request, send_file
from jinja2 import Template
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    return render_template('index.html', name = name)

@app.route('/test')
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

@app.get('/lab')
def lab():
    return render_template_string('''
            <form method="POST">
                <input type="text" name="name" placeholder="Your name">
                <button>submit</button>
            </form>
            ''')

@app.post('/lab')
def lab_message():
    name = request.form.get('name')
    return render_template_string("<p> Hello, " + name + "</p>")

@app.get("/source")
def source():
    return send_file(__file__, mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
