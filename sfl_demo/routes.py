from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, login_required, logout_user
from sfl_demo import app, db, bcrypt
from sfl_demo.form import LoginForm, RegistrationForm, UploadPictureForm
from sfl_demo.models import User
from sfl_demo.img_process import save_picture, predict_picture
from sfl_demo.mongodb import insert, query


@app.route("/", methods=['GET', 'POST'])
@login_required
def home():
    form = UploadPictureForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_fn, picture_path = save_picture(form.picture.data)
            prediction = predict_picture(picture_path)
            doc = {
                "picture_fn": picture_fn,
                "prediction": prediction,
                "userId": current_user.id}
            insert(doc)
            flash(
                f'Successfully uploaded a picture!', 'success')
        else:
            flash('No picture selected, please upload a picture!', 'danger')
        return redirect(url_for('home'))
    results = query({"userId":current_user.id})
    return render_template('home.html', title='Home', results=results, form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            print(next_page)
            flash(f'Login successfully', 'success')
            # make sure to use return
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Failed to login, please check username and password', 'danger')
    return render_template('login.html', title='login', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode("utf-8")
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(
            f'home created for { form.last_name.data }! Please login in', 'success')
        # make sure to use return
        return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
