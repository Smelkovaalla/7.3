from pprint import pprint

result_list = []
my_list = ['1.txt', '2.txt', '3.txt']

for i in my_list:
  my_dict = {}
  with open(i) as file:
    my_dict['Имя файла'] = i
    lines = file.readlines()
    my_dict['Количество строк'] = len(lines)
    my_dict['Содержимое файла'] = lines
    result_list.append(my_dict)

result_list.sort(key=lambda x: x['Количество строк'])
pprint(result_list)

with open('4.txt', 'w') as f:
  for line in result_list:
    f.write(f"{line['Имя файла']}\n")
    f.write(f"{str(line['Количество строк'])}\n")
    for i in line['Содержимое файла']:
      f.write(i)
    f.write(f"\n")

  print('Текст записан в файл 4.txt')

