from pathlib import Path

def total_salary(path):
    try:
        with open(path/'salary.txt', 'r', encoding='utf-8') as file:
            developers = 0
            total_salary = 0
            for line in file:
                name, salary = line.split(',')
                total_salary += float(salary)
                developers += 1     
        return total_salary, total_salary / developers
    except FileNotFoundError:
        print('Файл не знайдено.')
    except ZeroDivisionError:
        print('Файл порожній.')
    except Exception:
        print('Помилка читання файлу.')

total, average = total_salary(Path(__file__).parent)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
