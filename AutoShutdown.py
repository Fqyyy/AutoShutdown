import os
import time
import platform

def shutdown() -> None:
    system_name = platform.system()
    if system_name == "Windows":
        os.system("shutdown /s /t 1")  # Выключение для Windows
    elif system_name == "Linux" or system_name == "Darwin":  # Linux и macOS
        os.system("sudo shutdown -h now")  # Выключение для Linux/macOS
    else:
        print(f"Unsupported operating system: {system_name}")

def schedule_shutdown(minutes: int) -> None:
    print(f'Компьютер выключится через {minutes} минут(ы)...')
    time.sleep(minutes * 60)
    shutdown()

def main() -> None:
    try:
        set_time = int(input("Введите время до выключения (в минутах): "))
        if set_time <= 0:
            print("Время должно быть больше нуля.")
            return
        schedule_shutdown(set_time)
    except ValueError:
        print("Пожалуйста, введите корректное число минут.")

if __name__ == "__main__":
    main()
