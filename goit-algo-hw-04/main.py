def total_salary(path):
    total_salary = 0.0
    num_of_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    salary = float(parts[1])
                    total_salary += salary
                    num_of_developers += 1

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None

    if num_of_developers == 0:
        return 0.0, 0.0
    else:
        average_salary = total_salary / num_of_developers
        return total_salary, average_salary

total, average = total_salary("/Users/vladislavadanivska/Documents/studyingpython/goit-algo-hw-04/salary_file.txt")
if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")




