from flask import Flask, json, render_template
  
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/index.html')


@app.route('/art')
def art():
    return render_template('/art.html')


@app.route('/photo')
def photo():
    return render_template('/photo.html')

  

if __name__ == '__main__':
    # app.run(debug=True, port=5050)
    # app.run(debug=True, host='0.0.0.0')
    app.run()
