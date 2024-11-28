from flask import render_template, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user


from website_management import app

from database_management import db, User, refresh_user_list
import database_management.initialise_db_and_lists
from website_forms import AdminLogin

@app.route("/adminlogin", methods=["GET", "POST"])
def admin_login():
    user_object_list = database_management.initialise_db_and_lists.user_object_list
    admin_login_form = AdminLogin()
    if user_object_list:
        if admin_login_form.validate_on_submit():
            entered_username = admin_login_form.username.data
            entered_password = admin_login_form.password.data
            user = db.session.execute(db.select(User).where(User.username == entered_username)).scalar()
            if user:
                if check_password_hash(user.stored_password, entered_password):
                    print(f"Checking details...")
                    login_user(user)
                    print(f"You have been logged in")
                    return redirect(url_for('admin_dashboard'))
                else:
                    print("Incorrect credentials")
                    return redirect(url_for('home_page'))
            else:
                print("Incorrect credentials")
                return redirect(url_for('home_page'))
    else:
        if admin_login_form.validate_on_submit():
            entered_username = admin_login_form.username.data
            entered_password = admin_login_form.password.data
            new_entry = User(
                username=entered_username,
                stored_password=generate_password_hash(entered_password, method='pbkdf2:sha256', salt_length=8)
            )
            db.session.add(new_entry)
            db.session.commit()
            refresh_user_list()
            user = new_entry
            login_user(user)
            return redirect(url_for('admin_dashboard'))
    return render_template("adminlogin.html", form=admin_login_form, user=user_object_list)