
from flask import Flask,render_template,request, send_file, send_file,redirect

from engg.engg_cutoff_data import engg_read_db
from engg.engg_get_functions import engg_get_rank,engg_get_category,engg_get_branches,engg_get_places

from medical.med_cutoff_data import med_read_db
from medical.med_get_functions import med_get_rank,med_get_category,med_get_seat_type,med_get_places

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def main():

    if request.method == 'POST':
        name = request.form['firstname']
        stream = request.form['Stream']

        print(name,stream , sep='\n')

        if stream == 'Engineering':
            return redirect('/engineering')

        elif stream == 'Medical':
            return redirect('/medical')


        return redirect('/donate')


    return render_template('index.html')


@app.route('/engineering',methods=['GET','POST'])
def engineering():
    data = []

    if request.method == 'POST':
        # name = request.form['firstname']
        rank = engg_get_rank(request.form['Rank'])
        category = engg_get_category(request.form['Category'])
        branch = engg_get_branches(request.form.getlist('Branch'))
        place = engg_get_places(request.form.getlist('Place'))

        print(rank,category,branch,place, sep='\n')

        data = engg_read_db(rank,category,place,branch)

        for d in data:
            print(d)

        print(len(data))

        return render_template('engg.html',data = data)


    return render_template('engg.html',data = data)


@app.route('/medical',methods=['GET','POST'])
def medical():
    data = []

    if request.method == 'POST':
        name = request.form['firstname']
        rank = med_get_rank(request.form['Rank'])
        category = med_get_category(request.form['Category'])
        seat_type = med_get_seat_type(request.form.getlist('seat_type'))
        place = med_get_places(request.form.getlist('Place'))

        print(name,rank,category,seat_type,place, sep='\n')

        data = med_read_db(rank,category,place,seat_type)

        for d in data:
            print(d)

        print(len(data))

        return render_template('medical.html',data = data)


    return render_template('medical.html')
    

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True , port = 8000)