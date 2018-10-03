"""
Main module
"""

from flask import Flask, render_template
import connexion

# create flask app instance
app = Flask(__name__, template_folder='templates')

#create connextion instance
app = connexion.App(__name__, specification_dir='./')

# read swagger .yml file to configure endpoints
app.add_api('swagger.yml')


#create url route for appllication '/'

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)