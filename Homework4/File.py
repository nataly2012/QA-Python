# 1. Записываем “Number: строка из файла” из одного файла в другой. Не забываем закрывать файлы.
# 2. Воспользуйтесь менеджером контекста для файла, в который вы записываете информацию.

f1 = open('text1.txt','w')
text = " Rain, rain, go away.\n Come again another day.\n Little girl wants to play. \n Rain, rain, go away."
f1.write(text)
f1.close()
f1= open('text1.txt')
print(f1.read())

f = open('text1.txt')
with open('text2.txt', 'w') as f2:
    b=1
    for line in f:
        f2.write(str(b) + ': ' + line)
        b+=1
f2.close()
f2=open('text2.txt')
print(f2.read())