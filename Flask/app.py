# 1. import Flask
from flask import Flask,render_template,jsonify,url_for,json

# 2. Create an app, being sure to pass __name__
#app = Flask(__name__)
app = Flask(__name__, static_url_path='/static/')

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    
    # json_data = open(url_for('static', filename="usda_survey_splitted.json"))
    # data = json.load(json_data)
    return render_template('home.html')
    #return render_template('home.html', data=data)

@app.route('/send')
def send():
    return app.send_static_file('usda_survey_splitted.json')
    #return url_for('static', filename='usda_survey_splitted.json')
    #return "<a href=%s>file</a>" % url_for('static', filename='usda_survey_splitted.json')



@app.route('/test')
def homepage():
    return 'test';
  #with open('usda_survey_splitted.json', 'r') as f:
      #return json.loads(f.read())
    #return render_template('movies.html', movies=json.loads(f.read())['movies'])

# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

# @app.route('/data')
# def data():
#     return jsonify(api_scraper())


if __name__ == "__main__":
    app.run(debug=True)
