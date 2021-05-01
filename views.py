from flask import Flask, render_template, request, jsonify
from blueprints.Zachary.bubblesort import bubbleSort
import projects #projects definitions are placed in different file
from blueprints.Abhijay.__init__ import people_Abhijay_bp
from blueprints.Aiden.__init__ import people_Aiden_bp
from blueprints.Ak.__init__ import people_Ak_bp
from blueprints.Megan.__init__ import people_Megan_bp
from blueprints.Zachary.__init__ import people_Zachary_bp


app = Flask(__name__)
app.register_blueprint(people_Abhijay_bp, url_prefix='/abhijay')
app.register_blueprint(people_Aiden_bp, url_prefix='/aiden')
app.register_blueprint(people_Ak_bp, url_prefix='/ak')
app.register_blueprint(people_Megan_bp, url_prefix='/megan')
app.register_blueprint(people_Zachary_bp, url_prefix='/zachary')

@app.route('/')
def base_route():
    return render_template("base.html", projects=projects.setup())

@app.route('/Mini-lab-storage')
def labstorage_route():
    return render_template("labstorage.html", projects=projects.setup())

@app.route('/Mini-lab-storage-Zach')
def zachlabstorage_route():
    return render_template("Bubble_sort_zach.html", projects=projects.setup())

@app.route('/bubbleSort',methods=["GET","POST"])
def bubbleSort():
    data = []
    string = False
    if request.form:
       string = request.form.get("string")
       data = string.split()
       if request.form:
            string = request.form.get("string")
            data = string.split()
            original_data = string.split()
            if(request.form["select"] == "integer"):
            # Need to convert all strings to numbers
                try:
                    for j in range (0,len(data)):
                        data[j] = int(data[j])
                    for j in range (0,len(original_data)):
                        original_data[j] = int(original_data[j])
                    return render_template("Bubble_sort_zach.html",output_list = bubbleSort(data,string).OuputList,original_list = original_data)
                except ValueError:
                    return render_template("Bubble_sort_zach.html",output_list = "Please enter Strings or Integers only",original_list = "Error")
            else:
                 try:
                     string = True
                     return render_template("Bubble_sort_zach.html",output_list = bubbleSort(data,string).OuputList,original_list = original_data)
                 except ValueError:
                       return render_template("Bubble_sort_zach.html",output_list = "Please enter Strings or Integers only",original_list = "Error")
    return render_template("Bubble_sort_zach.html",output_list = bubbleSort(data,string).OutputList,original_list = data)


if __name__ == "__main__":
    #runs the application on the development server
    app.run(port='5000', host='127.0.0.1', debug = True)
