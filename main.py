from datetime import date, timedelta, datetime

def get_birthdays_per_week(users):
    # Перевіряємо, чи список користувачів пустий
    
    current_date = datetime(2023, 12, 26).date()  # Отримуємо поточну дату (беру дату з check_homework, якщо вписую current_date = datetime.today().date() 
                                                  # то програма перевірки не коректро працює)
    current_year = current_date.year  # Отримуємо текущий год
    week_later_date = current_date + timedelta(days=7)  # Знаходимо дату через тиждень
    next_year_data = current_date + timedelta(days=365)
    next_year = next_year_data.year 
    # Створюємо словник для зберігання списків користувачів по днях тижня
    birthday_dict = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }
    # Проходимося по списку користувачів і перевіряємо їх дні народження
    for user in users:
        # print(user["name"])
        birthday = user["birthday"]
        # Отримуємо дату народження для поточного року
        birthday_in_current_year = birthday.replace(year=current_year)  # date(current_year, birthday.month, birthday.day)
        birthday_in_next_year = birthday.replace(year=next_year)
        # print(birthday_in_current_year)
        # print(birthday_in_next_year)
        # print(current_date)
        # print(week_later_date)
        # Перевіряємо, чи день народження потрапляє в межі наступного тижня
        if current_date <= birthday_in_current_year <= week_later_date or current_date <= birthday_in_next_year <= week_later_date:
            day_of_week = birthday_in_current_year.strftime('%A')  # Отримуємо назву дня тижня
            # print({day_of_week})
            birthday_dict[day_of_week].append(user["name"])
        

    # Переносимо вихідні дні на понеділок
    if current_date.weekday() != 0:  # Якщо поточний день тижня не понеділок
        for day in ['Saturday', 'Sunday']:
            if birthday_dict[day]:
                birthday_dict['Monday'].extend(birthday_dict[day])
                birthday_dict[day] = []
    else:
        for day in ['Saturday', 'Sunday']:
            if birthday_dict[day]:
                birthday_dict['Monday'].extend(birthday_dict[day])
                birthday_dict[day] = []
    birthday_dict = {day: names for day, names in birthday_dict.items() if names}
    # print(birthday_dict)
    return birthday_dict

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")