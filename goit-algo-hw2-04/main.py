def get_cats_info(path):
    cats_info = []

    try:
      with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": parts[2]
                    }
                    cats_info.append(cat)

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")
    return cats_info

cats_info = get_cats_info("/Users/vladislavadanivska/Documents/goit-algo-hw2-04 /cats_info")
for cat in cats_info:
        print(f"ID: {cat['id']}, Name: {cat['name']}, Age: {cat['age']}")
        print() 
