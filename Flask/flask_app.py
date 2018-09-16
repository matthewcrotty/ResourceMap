from flask import *
import urllib.request
import json
from fips import *
from flaskext.mysql import MySQL
from flask import jsonify

app = Flask(__name__, template_folder='templates')
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'Resources'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

censusKey = "1dc5156c4a13a23278eb8105175e8d9725fb69f0"

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/popquery")
def query():
    state = request.args.get('state')
    county = request.args.get('county')
    county = getFIPSCodeCounty(state, county)
    state = getFIPSCodeState('\"'+state+'\"')
    print("State",state,"County",county)
    if not state:
        return ["Sorry Cannot find any resources available here!"]
    request_url = "http://api.census.gov/data/2010/sf1?key="+censusKey+"&get=P0010001,NAME&for=county:"+county+"&in=state:"+state
    with urllib.request.urlopen(request_url) as response:
        text = response.read()
    ## Query MySQL Database for all resources at location represented by 
    ## state and country code
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from resources where state_code='" + "36" + "' and county_code='" + "001" + "'")
    data = cursor.fetchall()
    print(type(data))
    if data is None:
        return ["Sorry. Cannot find any resources available here!"]
    else:
        return jsonify(data)


@app.route("/geoquery", methods=('GET', 'POST'))
def geoquery():
    if request.method == 'POST':
        lat = request.form['lat']
        lang = request.form['lng']
        request_url = "https://maps.googleapis.com/maps/api/geocode/json?&latlng="+lat+","+lang+"&key=AIzaSyBbbvgJb9Yc-qHEZYmcot9C3ZdTaWWsLjc"
        r = urllib.request.urlopen(request_url)
        data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
        results = data['results']
        state = ""
        county = ""
        for x in results:
            for y in x['address_components']:
                if y['types'][0] == 'administrative_area_level_2':
                    county = y['long_name']
                elif y['types'][0] == 'administrative_area_level_1':
                    state = y['long_name']
    return redirect('/popquery?state='+state+"&county="+county)


