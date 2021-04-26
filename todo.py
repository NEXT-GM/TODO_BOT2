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
    userDate = input("Введите дату:\n")
    userTask = input("Что нужно делать?")

  if userDate in todo.keys():
    todo[ userDate ].append( userTask )
  else:
    todo[ userDate ] = [ userTask]
    todo[ userDate ] = userTask
    print(f"[ {userDate} ] - добавлена задача'{userTask}'")
  elif userAnswer == "help":
    print(HELP)
  elif userAnswer == "show":
    for date in todo.keys():
      print(f"[ {date} ] -\t { todo [date] }")
  elif userAnswer == "exit":
    break
  elif userAnswer == "done":
    print("Работает\n")