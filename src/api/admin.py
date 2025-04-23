# src/api/admin.py

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from api.models import db, User


# Optional: Customize how the User model appears in the Admin UI
class UserAdmin(ModelView):
    column_exclude_list = ['password']          # Hide password column from list view
    form_excluded_columns = ['password']        # Hide password field from forms

    can_create = True
    can_edit = True
    can_delete = True

    column_searchable_list = ['email', 'username', 'first_name', 'last_name']
    column_filters = ['role']
    column_list = ['id', 'email', 'username', 'first_name', 'last_name', 'role']  # Show these fields in the table

    form_widget_args = {
        'password': {
            'disabled': True
        }
    }


# Initialize Flask-Admin with app and models
def init_admin(app):
    admin = Admin(app, name='Fitness Trainer Admin', template_mode='bootstrap4')

    # Add all views
    admin.add_view(UserAdmin(User, db.session))

    # Optional: Add more models here
    # admin.add_view(ModelView(WorkoutPlan, db.session))
    # admin.add_view(ModelView(ClientProgress, db.session))
