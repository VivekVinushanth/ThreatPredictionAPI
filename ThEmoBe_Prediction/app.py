from flask import Flask

app = Flask(__name__)


@app.route('/Threat')
def predictThreat():
    return 'Threat Predicted'

@app.route('/Emo')
def predictThreat():
    return 'Emo Detected'

@app.route('/Behav')
def predictThreat():
    return 'Behaviour Detected'

if __name__ == '__main__':
    app.run()
