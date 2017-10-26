# 1. Записываем “Number: строка из файла” из одного файла в другой. Не забываем закрывать файлы.
# 2. Воспользуйтесь менеджером контекста для файла, в который вы записываете информацию.

f1 = open('text1.txt','w')
text = " Rain, rain, go away.\n Come again another day.\n Little girl wants to play. \n Rain, rain, go away."
f1.write(text)
f1.close()
f1= open('text1.txt')
m = f1.read()
print(m)