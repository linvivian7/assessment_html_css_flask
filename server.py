from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.secret_key = 'testing123'


@app.route('/')
def index():
    """Return homepage."""

    return render_template("index.html")


@app.route('/application')
def application_form():
    """Return application form."""

    avail_job = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html", jobs=avail_job)


@app.route('/application-success', methods=['POST'])
def process_application():
    """Acknowledge applicant that application is received.

    Includes full name, title, and salary requirement.
    """

    first_name = request.form.get("firstname").rstrip()
    last_name = request.form.get("lastname").rstrip()

    role = request.form.get("role")
    salary = "{:,.2f}".format(float(request.form.get("salaryreq")))

    return render_template("application-response.html",
                           first_name=first_name,
                           last_name=last_name,
                           role=role,
                           salary=salary)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
