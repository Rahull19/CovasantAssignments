from flask import Flask, request, jsonify, Response
import random

app = Flask(__name__)

def generate_forecast():
    forecast_list = []
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue", "Wed"]
    texts = ["Breezy", "Mostly Sunny", "Mostly Cloudy", "Partly Cloudy", "Cloudy"]
    
    for i in range(10):
        high = random.randint(30, 40)
        low = random.randint(15, 30)
        forecast_list.append({
            "code": str(random.randint(20, 35)),
            "date": f"{21 + i} Apr 2025",
            "day": days[i % 7],
            "high": str(high),
            "low": str(low),
            "text": random.choice(texts)
        })
    return forecast_list

@app.route('/w/<city>', methods=['GET'])
def get_weather(city):
    format_type = request.args.get('format', 'json')
    temp = str(random.randint(15, 40))
    forecast_data = generate_forecast()

    if format_type.lower() == "xml":
        xml_response = f'''<?xml version="1.0" encoding="UTF-8" ?>
<query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="1" yahoo:created="2025-04-21T04:41:58Z" yahoo:lang="en-IN">
  <results>
    <channel>
      <yweather:units xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" distance="mi" pressure="in" speed="mph" temperature="F"/>
      <title>Yahoo! Weather - {city}, Unknown</title>
      <description>Yahoo! Weather for {city}, Unknown</description>
      <language>en-us</language>
      <lastBuildDate>Mon, 21 Apr 2025 06:00 AM</lastBuildDate>
      <ttl>60</ttl>
      <yweather:location xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" city="{city}" country="Unknown" region="Unknown"/>
      <yweather:wind xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" chill="3" direction="23" speed="22"/>
      <yweather:atmosphere xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" humidity="71" pressure="1007.0" rising="0" visibility="16.1"/>
      <yweather:astronomy xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" sunrise="7:6 am" sunset="10:56 pm"/>
      <item>
        <title>Conditions for {city}, Unknown at 06:00 AM</title>
        <yweather:condition xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="31" date="Mon, 21 Apr 2025 06:00 AM" temp="{temp}" text="Clear"/>
      </item>
    </channel>
  </results>
</query>'''
        return Response(xml_response, mimetype='application/xml')

    else:  # Default to JSON
        data = {
            "query": {
                "count": 1,
                "created": "2025-04-21T06:10:11Z",
                "lang": "en-IN",
                "results": {
                    "channel": {
                        "units": {"distance": "mi", "pressure": "in", "speed": "mph", "temperature": "F"},
                        "title": f"Yahoo! Weather - {city}, Unknown",
                        "description": f"Yahoo! Weather for {city}, Unknown",
                        "language": "en-us",
                        "lastBuildDate": "Mon, 21 Apr 2025 06:10 AM",
                        "ttl": "60",
                        "location": {"city": city, "country": "Unknown", "region": "Unknown"},
                        "wind": {"chill": "3", "direction": "23", "speed": "22"},
                        "atmosphere": {"humidity": "71", "pressure": "1007.0", "rising": "0", "visibility": "16.1"},
                        "astronomy": {"sunrise": "7:6 am", "sunset": "10:56 pm"},
                        "item": {
                            "title": f"Conditions for {city}, Unknown at 06:00 AM",
                            "lat": "64.499474",
                            "long": "-165.405792",
                            "pubDate": "Mon, 21 Apr 2025 06:10 AM",
                            "condition": {
                                "code": "31",
                                "date": "Mon, 21 Apr 2025 06:10 AM",
                                "temp": temp,
                                "text": "Clear"
                            },
                            "forecast": forecast_data,
                            "description": "Random weather forecast"
                        }
                    }
                }
            }
        }
        return jsonify(data)

if __name__ == '__main__':
    app.run()
