from flask import Flask, render_template, request, redirect, url_for
from utils import ageCalculate, bmi

app = Flask(__name__)


# Route for the first page
@app.route('/', methods=['GET', 'POST'])
def personal_info():
    if request.method == 'POST':
        # Retrieve form data
        global name
        name = request.form['name']
        global surname
        surname = request.form['surname']
        global email
        email = request.form['email']
        global mobile
        mobile = request.form['mobile']
        # Save data or process as needed
        # For now, we simply redirect to the next page with form data
        return redirect(url_for('additional_info'))
    return render_template('personal_info.html')

# Route for the second page
@app.route('/additional_info', methods=['GET', 'POST'])
def additional_info():
    if request.method == 'POST':
        # Retrieve form data
        gender = request.form['gender']
        dob = request.form['dob']
        weight = request.form['weight']
        height = request.form['height']
        smoking = request.form['smoking']
        diabetes = request.form['diabetes']

        print("Hello {0} {1}".format(name, surname))
        age = ageCalculate.calculate_age(dob)
        print("your age is {0}".format(age))
        bmi_val, status= bmi.calculate_bmi(weight, height) 
        print("your Body mass index is {0} and Status is {1}".format(int(bmi_val), status))


        # Process or save the data as needed
        return f"Data Received: Name:{name}\n, Surname:{surname}\n, Email:{email}\n, Mobile:{mobile}\n, Gender:{gender}\n, DOB:{dob}\n, Weight:{weight}\n, Height:{height}\n, Smoking: {smoking}\n, Diabetes: {diabetes}"

    return render_template('additional_info.html', name=name, surname=surname, email=email, mobile=mobile)

if __name__ == '__main__':
    app.run(debug=True)
