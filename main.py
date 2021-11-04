from flask import Flask, jsonify, request, render_template, redirect
from flask_cors import CORS
from replit import db
import random, string

app = Flask(__name__)
CORS(app)

@app.route('/')
def app_index():
    return render_template('index2.html')

@app.route('/brand-new')
def app_brsnd():
    return redirect('/')

@app.route('/v2')
def app_v2():
    return redirect('/brand-new')

@app.route('/linklist')
def app_linklist():
    return render_template('linklist.html')

@app.route('/brand-new/login')
def app_newlogin():
    return render_template('newlogin.html')

@app.route('/login')
def app_login():
    return redirect('/brand-new/login')


@app.route('/stats')
def app_statistics():
    return render_template('stats.html') 

@app.route('/shorten')
def app_shorten():
    return render_template('shorten.html') 


@app.route('/jslogin')
def app_javalog():
    return render_template('jslogin.html') 

@app.route('/toxy')
def app_toxy():
    return render_template('toxy.html') 


@app.route('/json')
def app_json():
    return render_template('json.html') 

@app.route('/impressum')
def app_impressum():
    return render_template('impressum.html') 

@app.route('/datenschutz')
def app_datenschutz():
    return render_template('datenschutz.html') 

@app.route('/homepage')
def app_index2():
    return render_template('index2.html') 


@app.route('/<key>')
def app_key(key):
    if (d := db.get(key)):
        d['views'] += 1
        db[key] = d
    return redirect(db.get(key, {}).get('url', '/'))

@app.route('/<key>.json')
def app_key_data(key):
    return jsonify(db.get(key, {}))

@app.route('/api/create', methods=['POST'])
def api_create():
    url = request.form['url']
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    c = 4
    key = ''.join([random.choice(chars) for i in range(c)])
    

    while key in list(db.keys()):
        c += 1
        key = ''.join([random.choice(chars) for i in range(c)])
    db[key] = {
        'url': url,
        'views': 0
    }
    return jsonify({'key': key, 'url': f'https://{request.host}/{key}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)