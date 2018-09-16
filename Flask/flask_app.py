from flask import *
from flask_googlemaps import Map
import urllib.request
import json
from fips import *

app = Flask(__name__, template_folder='templates')

censusKey = "1dc5156c4a13a23278eb8105175e8d9725fb69f0"

@app.route("/")
def index():
    my_map = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    resources = {"State_Code":"00","County_Code":"001","Resource_Type":"Salt","Quantity":"100 lb.","Location":"Troy Warehouse"}
    return render_template('index.html', mymap=my_map, resources=resources)


@app.route("/popquery")
def query():
    state = request.args.get('state')
    state = getFIPSCodeState('\"'+state+'\"')
    if not state:
        return render_template('error.html')
    request_url = "http://api.census.gov/data/2010/sf1?key="+censusKey+"&get=P0010001&for=state:"+state
    with urllib.request.urlopen(request_url) as response:
        text = response.read()
    return text


@app.route("/geoquery", methods=('GET', 'POST'))
def geoquery():
    if request.method() == 'POST':
        lat = request.args.get('lat')
        lang = request.args.get('lang')
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
        print(county + ", " + state)
    return county+" "+state#redirect('/popquery?state='+state)


