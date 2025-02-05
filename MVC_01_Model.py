import json


class TimeTableModel:

    def __init__(self):
        self.__dates = []

    def get_dates(self):
        return self.__dates

    def add_date(self, course, date, filename):
        data = {}
        data['course'] = course
        data['date'] = date
        self.__dates.append(data)
        self.update_json(filename)

    def update_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(self.__dates, fp, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    user_name = input('Введите ваше имя: ')
    filename = fr'dates_files\\{user_name}_date_file.json'
    dates_model = TimeTableModel()
    print(dates_model.get_dates())
    dates_model.add_date('HTML', 'May 29', filename)
    dates_model.add_date('CSS', 'Jun 3', filename)
    dates_model.add_date('JavaScript', 'Jun 26', filename)
    dates_model.add_date('Python', 'Sep 9', filename)
    print(dates_model.get_dates())