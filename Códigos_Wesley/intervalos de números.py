num_i = int(input("dgite o valor inicial: "))
num_f = int(input("digite o valor  final do intervalo: "))


num_file= []
i = num_i
num_file.append(num_i)
while i != num_f:
    i = i + 1
    num_file.append(i)
print(num_file)
print(len(num_file))