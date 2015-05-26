from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/cal')
def c():
    return render_template('ca1.html')

@app.route('/calcal')
def cc():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    c = request.args.get('operator')
    if c == '+':
        return jsonify(result=a+b)
    elif c == '-':
        return jsonify(result=a-b)
    elif c == '*':
        return jsonify(result=a*b)
    elif c == '/':
        return jsonify(result=a/b)
    elif c == '%':
        return jsonify(result=a%b)

if __name__ == '__main__':
    app.run()
