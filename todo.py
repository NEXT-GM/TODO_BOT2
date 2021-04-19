HELP = """
help - выводить список команд
add - добавить задачу
show - показать задачи
done - убрать выполненную задачу
exit - закрыть приложение
"""

todo = {}
print ("Введите команду, введите help для вывода списка команд")

while True:
  userAnswer = input()

  if userAnswer == "add":
    UserDate = input("Введите дату:\n")
    UserTask = input("Что нужно делать?")
    todo[ userDate ] = userTask
    print(f"[ {userDate} ] - добавлена задача'{userTask}'")
  elif userAnswer == "help":
    print(HELP)
  elif userAnswer == "show":
    print("Работает\n")
  elif userAnswer == "exit":
    break
  elif userAnswer == "done":
    print("Работает\n")