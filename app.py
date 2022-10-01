

from flask import Flask,render_template,request 

from cutoff_data import read_db
from get_functions import get_rank,get_category,get_branches,get_places

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello_world():

    data = []

    if request.method == 'POST':
        name = request.form['firstname']
        rank = get_rank(request.form['Rank'])
        category = get_category(request.form['Category'])
        branch = get_branches(request.form.getlist('Branch'))
        place = get_places(request.form.getlist('Place'))

        print(name,rank,category,branch,place, sep='\n')

        data = read_db(rank,category,place,branch)

        for d in data:
            print(d)

        print(len(data))

        return render_template('index.html',data = data)


    return render_template('index.html',data = data)
    #return "<p>Hello, World!</p>"




if __name__ == "__main__":
    app.run(debug=True , port = 8000)