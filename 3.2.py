def send_email(message, recipient, *, sender = "university.help@gmail.com", reсipient=None):
    new_recipient = '@' in recipient and (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net'))
    new_sender = '@' in sender and (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'))
    if new_recipient and new_sender:
        if reсipient == sender:
            print("Нельзя отправить письмо самому себе!")
        else:
            if sender == "university.help@gmail.com":
                print("Письмо успешно отправлено с адреса", sender,"на адрес",recipient,".")
            else:
                print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient, ".")
    else:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru')
sender=('urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')