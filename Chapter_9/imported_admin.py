import admin

my_admin = admin.Admin('angel','miholos', '19/08/1984', 'LA')
my_admin.describe_user()
my_admin.privileges.show_privileges()