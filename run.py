from flask import Flask, render_template, request, jsonfy

app = Flask(__name__)

@app.route('/cal')
def c():
    return render_template(ca.html)

@app.route('/calcal')
def cc():
    a = request.args.get('a', 0, type='float')
    b = request.args.get('b', 0, type='float')
    return jsonfy(result=a+b)

if __name__ == '__main__':
    app.run()
