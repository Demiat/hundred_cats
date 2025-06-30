from datetime import datetime
import asyncio

import aiohttp

URL = 'https://api.thecatapi.com/v1/images/search'

# Асинхронная функция для получения нового изображения.


async def get_new_image_url(session):
    # Выполнить асинхронный GET-запрос на указанный URL с общей сессией.
    response = await session.get(URL)
    # Асинхронно получить тело ответа в формате JSON.
    data = await response.json()
    # Извлечь URL случайного изображения из ответа.
    return data[0]['url']

# Главная асинхронная функция.


async def main():
    # Создать единую асинхронную сессию для выполнения HTTP-запросов.
    async with aiohttp.ClientSession() as session:
        # Создать список задач для асинхронного выполнения,
        # передаю общую сессию в каждую задачу.
        tasks = [
            asyncio.create_task(get_new_image_url(session)) for _ in range(100)
        ]
        # Подождать, пока выполнятся все задачи.
        result = await asyncio.gather(*tasks)
        print(result)

# Точка входа в программу.
if __name__ == '__main__':
    # Записать текущее время начала выполнения программы.
    start_time = datetime.now()

    asyncio.run(main())

    # Записать текущее время окончания выполнения программы.
    end_time = datetime.now()
    # Напечатать время выполнения программы.
    print(f'Время выполнения программы: {end_time - start_time}.')
