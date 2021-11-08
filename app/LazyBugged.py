from Flask import flask

@app.route('/')
def yomepage():
  return "<p>LazyBugged blog welcomes you!</p>"
