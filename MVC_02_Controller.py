class DatesController:

    def __init__(self, model):
        self.model = model

    def get_default_action(self):
        return 'Добро пожаловать на главную страницу'

    def get_dates_auth(self, user_role='guest'):
        if user_role in ['is_superuser', 'is_staff', 'user_owner']:
            if self.model.get_dates():
                return self.model.get_dates()
            return None
        return 'Forbidden'

    def get_only_courses_list(self):
        courses = []
        data = self.model.get_dates()
        if data:
            for element in data:
                courses.append(element['course'])
            return courses
        return None

    def get_only_dates_list(self, user_role='guest'):
        if user_role in ['is_superuser', 'is_staff', 'user_owner']:
            dates = []
            data = self.model.get_dates()
            if data:
                for element in data:
                    dates.append(element['date'])
                return dates
            return None
        return 'Forbidden'

    def get_all_data_list(self, user_role='guest'):
        if user_role in ['is_superuser', 'is_staff', 'user_owner']:
            if self.model.get_dates():
                return self.get_only_courses_list(), self.get_only_dates_list(user_role)
            return None
        return 'Forbidden'

    def add_date(self, course, date, filename, user_role='guest'):
        if user_role not in ['is_superuser', 'is_staff']:
            return 'Forbidden!'
        else:
            self.model.add_date(course, date, filename)
            return True
