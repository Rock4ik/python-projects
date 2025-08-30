import asyncio

async def say_hello_after_delay(name, delay):
    # Аналог Task.Delay() из C#
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

async def main():
    # Аналог Task.WhenAll() из C#
    await asyncio.gather(
        say_hello_after_delay("Ilnaz", 2),
        say_hello_after_delay("Python", 1),
        say_hello_after_delay("World", 3)
    )

# Запускаем нашу асинхронную программу
asyncio.run(main())