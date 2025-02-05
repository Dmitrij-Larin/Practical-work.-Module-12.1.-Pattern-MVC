from MVC_02_Controller import DatesController


class DatesView:

    def __init__(self, controller: DatesController):
        self.controller = controller

    def display_default_action(self):
        print(self.controller.get_default_action())

    def display_dates_auth(self, user_role='guest'):
        result = self.controller.get_dates_auth(user_role)
        if result == 'Forbidden':
            print(result)
            return
        elif result:
            for item in result:
                print(f'{item['course']} дата: {item['date']}')
        else:
            print('Нет данных')

    def display_only_courses_list(self):
        result = self.controller.get_only_courses_list()
        if result:
            print('Список курсов:')
            for item in result:
                print(item, end=' ')
            print()
        else:
            print('Курсов нет!')

    def display_only_dates_list(self, user_role='guest'):
        result = self.controller.get_only_dates_list(user_role)
        if result == 'Forbidden':
            print(result)
        elif result:
            print('Список')
            for item in result:
                print(item, end=' ')
            print()
        else:
            print('Курсов нет!')

    def display_all_data_list(self, user_role='guest'):
        result = self.controller.get_all_data_list(user_role)
        if result:
            print(result)
        else:
            print('Нет данных!')

    def display_add_date(self, course, date, filename, user_role='guest'):
        result = self.controller.add_date(course, date, filename, user_role)
        if result is False:
            print('Неверный тип данных!')
        elif result == 'Forbidden!':
            print(result)
        else:
            print('Дaта успешно добавлена')
