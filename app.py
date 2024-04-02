from flask import Flask, json, render_template, request

  
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/photo.html', current_path=request.path)
    # return render_template('/index.html', current_path=request.path)
  

@app.route('/archi')
def archi():
    return render_template('/archi.html', current_path=request.path)
 
 
@app.route('/art')
def art():
    return render_template('/art.html', current_path=request.path)


@app.route('/photo')
def photo():
    return render_template('/photo.html', current_path=request.path)

 
@app.route('/photos/<string:id>')
def photos(id):
    return render_template(f'photos/photos-{id}.html')


@app.template_filter('is_active')
def is_active(path, current_path):
    return 'active' if path == current_path else ''

   

if __name__ == '__main__':
    # app.run(debug=True, port=5050)
    # app.run(debug=True, host='0.0.0.0')
    app.run()
 