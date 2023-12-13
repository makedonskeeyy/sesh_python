users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
un_visit = {}
for i in users:
    if i in un_visit:
        un_visit[i] += 1
    else:
        un_visit[i] = 1
user_i = {
    "Общее количество": len(users),
    "Уникальные посещения": len(un_visit)
}
print(user_i)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений