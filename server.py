from flask import Flask,render_template,url_for,request,redirect
import os
import csv 
app = Flask(__name__)
app.debug = True  # Ensure this line is present

print("FLASK_ENV:", os.environ.get("FLASK_ENV"))
app.debug = os.environ.get("FLASK_ENV") == "development"

@app.route('/')
def Home():
    return render_template('index.html')


@app.route('/<string:menu_name>')
def html_menu(menu_name):
    return render_template(menu_name)   

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        password = data['password']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{password},{subject},{message}')


def write_to_csv(data):
    with open('data.csv', mode='a', newline='') as datacsv:
        email = data['email']
        password = data['password']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(datacsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,password,subject,message])



  

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return "form submitted successfully"
    else:
        return "sorry try again" 



# @app.route('/landing.html')
# def Landing():
#     return render_template('landing.html') 

# @app.route('/contact.html')
# def contact_me():
#     return render_template('contact.html') 


app.debug = True


if __name__ == '__main__': 
    app.run()


# import os

# flask_env = os.environ.get("FLASK_ENV")
# if flask_env == "development":
#      app.debug = True

# print("FLASK_ENV:", os.environ.get("FLASK_ENV"))
# print("app.debug:", app.debug)


# import os

# flask_env = os.environ.get("FLASK_ENV")


# @app.route('/')
# def hello_world():
#     return 'welcome to Chuxog home'
# app.debug = True





