from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['post'])
def calculate():
    total_weightage = 0.0
    cumulative_score = 0.0
    for i in range(1, len(request.form) // 2 + 1):
        weightage = float(request.form['weightage{}'.format(i)])
        cumulative_score += float(request.form['mark{}'.format(i)]) * weightage
        total_weightage += weightage

    # Error checking
    if total_weightage != 100.0:#
        return render_template('400.html', reasons=['Total weightage does not equate to 100.']), 400
    
    cumulative_score /= total_weightage

    return render_template('results.html', form=request.form, score=cumulative_score)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.run(debug=True)