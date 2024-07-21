with open("bpla_storage_info.csv", "r", encoding="utf-8") as file:
    title = file.readline()
    content = file.readlines()

print(title)


with open("bpla_storage_warehouse.csv", "r", encoding="utf-8") as file1:
    title = file1.readline()
    content = file1.read()
    content = content.split('\n')


for i in range(len(content)):
    content[i] = content[i].split(",")


print(title)
print(*content, sep="\n")

try:
    for drone in content:
        if not (drone[6] in ("исправно", "неисправно")):
            raise ValueError("Такого состояния не существует")
except ValueError as e:
    print(f"Error: {e}. Что творится в твоей БД! Ужас")
print("Программа завершена")