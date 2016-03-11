from hello  import db
from hello import Role, User

# db.create_all()
# db.drop_all()
# db.create_all()

admin_role = Role(name = 'Admin')
mod_role = Role(name = 'Moderator')
user_role = Role(name = 'User')
user_john = User(username = 'john', role = admin_role)
user_susan = User(username = 'susan', role = user_role)
user_david = User(username = 'david', role = user_role)

db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])
db.session.commit()