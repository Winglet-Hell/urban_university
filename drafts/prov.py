import tkinter
from tkinter import filedialog, scrolledtext
import os

# Создание главного окна
window = tkinter.Tk()

# Настройка окна
window.title("Проводник")
window.geometry("700x500")
window.configure(bg="black")
window.resizable(width=False, height=False)


# Функция для выбора файла
def file_select():
    filename = filedialog.askopenfilename(
        initialdir="F:/",  # Начальная директория
        title="Выберите файл",
        filetypes=(("Текстовый файл", "*.txt"), ("Все файлы", "*.*")),
    )

    if filename:
        text.config(state="normal")  # Разрешаем редактирование текстового поля
        text.delete(1.0, tkinter.END)  # Очищаем текстовое поле
        text.insert(tkinter.END, f"Выбран файл: {filename}\n\n")
        text.config(state="disabled")  # Блокируем текстовое поле для редактирования

        # Открываем файл, если это текстовый файл
        if filename.endswith(".txt"):
            with open(filename, "r", encoding="utf-8") as file:
                file_content = file.read()
                text.config(state="normal")
                text.insert(tkinter.END, file_content)
                text.config(state="disabled")
        else:
            os.startfile(filename)  # Открываем другие типы файлов


# Функция для выбора директории
def directory_select():
    directory = filedialog.askdirectory(initialdir="F:/", title="Выберите директорию")

    if directory:
        text.config(state="normal")
        text.delete(1.0, tkinter.END)
        text.insert(tkinter.END, f"Выбрана директория: {directory}\n\n")

        # Перебираем файлы в выбранной директории
        for root, dirs, files in os.walk(directory):
            text.insert(tkinter.END, f"Папка: {root}\n")
            for file in files:
                filepath = os.path.join(root, file)
                text.insert(
                    tkinter.END, f"  Файл: {file} ({os.path.getsize(filepath)} байт)\n"
                )
            text.insert(tkinter.END, "\n")

        text.config(state="disabled")


# Создание текстового поля для отображения информации
text = scrolledtext.ScrolledText(
    window, width=85, height=20, wrap=tkinter.WORD, bg="silver"
)
text.grid(column=0, row=0, columnspan=2, padx=10, pady=10)
text.config(state="disabled")  # Сразу делаем текстовое поле только для чтения

# Создание кнопки для выбора файла
button_select_file = tkinter.Button(
    window, width=20, height=3, text="Выбрать файл", command=file_select
)
button_select_file.grid(column=0, row=1, padx=10, pady=10)

# Создание кнопки для выбора директории
button_select_directory = tkinter.Button(
    window, width=20, height=3, text="Выбрать директорию", command=directory_select
)
button_select_directory.grid(column=1, row=1, padx=10, pady=10)

# Запуск окна
window.mainloop()
