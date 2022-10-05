

from flask import Flask,render_template,request, send_file, send_file 

from medical.med_cutoff_data import med_read_db
from medical.med_get_functions import med_get_rank,med_get_category,med_get_seat_type,med_get_places

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello_world():

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

@app.route('/donate')
def qr_code():
    return send_file('qr_code.jpg',mimetype='Image')




if __name__ == "__main__":
    app.run(debug=True , port = 8000)