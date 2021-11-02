from .app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Welcome Home")

@app.route('/checkface', methods=['GET', 'POST'])
def index():
    print("Face recognition done here")

@app.route('/denyaccess', methods=['GET', 'POST'])
def index():
    print("Failed face recogition")

@app.route('/register', methods=['GET', 'POST'])
def index():
    print("New User registration")