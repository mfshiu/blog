from flask import Flask, redirect, render_template, url_for
  
app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('photo'))
    # return render_template('/index.html')


@app.route('/archi')
def archi():
    return render_template('/archi.html')
 

@app.route('/art')
def art():
    return render_template('/art.html')


@app.route('/photo')
def photo():
    return render_template('/photo.html')


@app.route('/photos/<string:id>')
def photos(id):
    return render_template(f'photos/photos-{id}.html')

            

if __name__ == '__main__':
    # app.run(debug=True, port=5050)
    # app.run(debug=True, host='0.0.0.0')
    app.run()
      