from MVC_01_Model import TimeTableModel
from MVC_02_Controller import DatesController
from MVC_03_View import DatesView

if __name__ == '__main__':
    model = TimeTableModel()
    controller = DatesController(model)
    view = DatesView(controller)
    user = 'user_owner'
    staff = "is_staff"
    superuser = "is_superuser"

    view.display_add_date('HTML', 'May 29', 'dates_file.json', 'is_staff')
    view.display_add_date('CSS', 'Jun 3', 'dates_file.json', 'is_superuser')
    view.display_add_date('JavaScript', 'Jun 26', 'dates_file.json', 'is_staff')
    view.display_add_date('Python', 'Sep 9', 'dates_file.json', 'is_superuser')
    print()
    view.display_default_action()
    view.display_dates_auth()
    view.display_dates_auth(user)
    view.display_dates_auth(staff)
    view.display_dates_auth(superuser)
    view.display_only_courses_list()
    view.display_only_dates_list()
    view.display_only_dates_list(user)
    view.display_only_dates_list(staff)
    view.display_only_dates_list(superuser)
    view.display_all_data_list()
    view.display_all_data_list(user)
    view.display_all_data_list(staff)
