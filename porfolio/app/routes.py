from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def return_index():
    return render_template('index.html', title='Home')

@app.route('/projects')
def return_projects():
    return render_template('projects.html', title='Projects')

@app.route('/about')
def return_about():
    return render_template('about.html', title='About')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Message sent!')
        return redirect('/')
    return render_template('contact.html', title='Contact')