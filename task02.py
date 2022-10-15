
# Напишите программу, удаляющую из 
# текста все слова содержащие "абв".

my_text = 'Свиабвнья абвпод Дубом вековым  абвНаелась желуабвдей досыта, до отвабвала  Наевшись, выспалась поабвд ним  Потабвом, глаза проабвдравши, встала  И рылабвом подрыабввать у Дуабвба корни стала'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)