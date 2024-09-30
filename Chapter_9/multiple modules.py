import user, privileges

my_admin = privileges.Admin('angel','miholos', '19/08/1984', 'LA')
my_admin.describe_user()
my_admin.privileges.show_privileges()