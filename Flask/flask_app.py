from flask import *
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import urllib.request
from fips import *

app = Flask(__name__, template_folder='templates')

app.config['GOOGLEMAPS_KEY'] = "AIzaSyBbbvgJb9Yc-qHEZYmcot9C3ZdTaWWsLjc"
GoogleMaps(app)

censusKey = "1dc5156c4a13a23278eb8105175e8d9725fb69f0"


@app.route("/")
def index():
    my_map = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )

    return render_template('index.html', mymap=my_map)


@app.route("/popquery")
def query():
    state = request.args.get('state')
    state = getFIPSCodeState(state)
    if not state:
        return render_template('error.html')
    request_url = "http://api.census.gov/data/2010/sf1?key="+censusKey+"&get=P0010001&for=state:"+state
    with urllib.request.urlopen(request_url) as response:
        text = response.read()
    return text


