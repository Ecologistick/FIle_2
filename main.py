files = ['1.txt', '2.txt', '3.txt']
result = []
for filename in files:
  with open(filename, encoding='utf-8') as file:
    result.append((filename, file.read().splitlines()))
result.sort(key=lambda r: len(r[1]))
with open("result.txt", 'w', encoding='utf-8') as file:
  for filename, lines in result:
    file.write("{}\n{}\n{}\n".format(filename, len(lines), '\n'.join(lines)))