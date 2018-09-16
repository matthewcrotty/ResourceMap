from flask import *
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import urllib.request
from fips import *

app = Flask(__name__, template_folder='templates')


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
    state = getFIPSCode(state)
    if not state:
        return render_template('error.html')
    request_url = "http://api.census.gov/data/2010/sf1?key="+censusKey+"&get=P0010001&for=state:"+state
    with urllib.request.urlopen(request_url) as response:
        text = response.read()
    return text


