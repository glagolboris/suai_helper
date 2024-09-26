import json


def set_data(file: str, self_bot):
    self_bot.cursor.execute("""SELECT * FROM timetable""")
    timetable = self_bot.cursor.fetchall()
    self_bot.cursor.execute("""SELECT full_name FROM professors""")
    professors = self_bot.cursor.fetchall()

    with open(file, 'w') as file:
        for couples in timetable:
            file.write(f'\nУ группы {couples[0]} такое расписание пар:\n')
            file.write(f'\nЧислитель:\n')
            for couple in json.loads(couples[1])['numerator'].keys():
                file.write(f"{couple}:\n")
                for day in json.loads(couples[1])['numerator'][couple].keys():
                    try:
                        file.write(f"\t{json.loads(couples[1])['numerator'][couple][day][0]}-{json.loads(couples[1])['numerator'][couple][day][1]}\n")
                    except IndexError:
                        pass
                        # file.write(f"\t{json.loads(couples[1])['numerator'][couple][day][0]}-'------'\n")
            file.write(f'\nЗнаменатель:\n')
            for couple in json.loads(couples[1])['denominator'].keys():
                file.write(f"{couple}:\n")
                for day in json.loads(couples[1])['denominator'][couple].keys():
                    try:
                        file.write(f"\t{json.loads(couples[1])['denominator'][couple][day][0]}-{json.loads(couples[1])['denominator'][couple][day][1]}\n")
                    except IndexError:
                        pass
                        file.write(f"\t{json.loads(couples[1])['denominator'][couple][day][0]}-'------'\n")

        file.write(f'\nСписок ФИО преподавателей:\n')
        for professor in professors[0]:
            file.write(professor+'\n')
