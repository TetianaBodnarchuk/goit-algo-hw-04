from pathlib import Path

def get_cats_info(path) -> list[dict]:
    try:
        with open(path/'cat.txt', 'r', encoding='utf-8') as file:
            list_cats = []

            for line in file:
                content = line.strip().split(',')

                if len(content) == 3:
                    info = {'id': content[0], 'name': content[1], 'age': content[2]}
                    list_cats.append(info)
                    print(list_cats)
                    print('*'*5)
                else:
                    print(f'Частина необхідних даних відсутня')

    except FileNotFoundError:
        print('Файл не знайдено.')

cats_info = get_cats_info(Path(__file__).parent)
print(cats_info)