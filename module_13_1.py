import asyncio

async def sleep(seconds):
    """Пауза на указанное количество секунд."""
    await asyncio.sleep(seconds)

async def start_strongman(name, power):
    """
    Имитация соревнований для одного силача.

    Args:
        name (str): Имя силача.
        power (int): Сила силача (чем больше, тем быстрее поднимает шары).
    """
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        # Задержка обратно пропорциональна силе, т.е. чем сильнее, тем быстрее
        await sleep(5 / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    """Запуск соревнований для нескольких силачей."""
    # Создаем задачи для каждого силача
    tasks = [
        asyncio.create_task(start_strongman('Pasha', 3)),
        asyncio.create_task(start_strongman('Denis', 4)),
        asyncio.create_task(start_strongman('Apollon', 5))
    ]
    # Запускаем все задачи параллельно и ожидаем их завершения
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(start_tournament())