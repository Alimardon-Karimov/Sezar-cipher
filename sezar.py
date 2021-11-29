import string

alphabets = string.ascii_lowercase + string.ascii_lowercase

sentence = list(input('enter your text: \n').lower())

what_to_do = input(
    'Kodlash uchun k ni kiriting, Kodni ochish uchun d ni kiriting \n').lower()

shift_number = int(input('Kalit raqamini kiriting (1 dan 25 gacha) \n'))

end_program = False

while not end_program:
    # search through the enter text
    if what_to_do == 'e':
        for i in range(len(sentence)):
            # get the position of each character within the sentence
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) + shift_number
                sentence[i] = alphabets[new_letter]
        # convert the list back to a string
        print(''.join(map(str, sentence)))
        end_program = True
    elif what_to_do == 'd':
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) - shift_number
                sentence[i] = alphabets[new_letter]
            # convert the list back to a string
        print(''.join(map(str, sentence)))
        end_program = True
    else:
        decide = input(
            'xato malumot kiritildi, Qayta kiritish uchun y ni kiriting, tugatish uchun n ni kiriting \n').lower()
        if decide == 'y':
            sentence = list(input('enter your text: \n').lower())
            what_to_do = input(
                'Kodlash uchun k ni kiriting, Kodni ochish uchun d ni kiriting \n').lower()
            shift_number = int(input('Kalit raqamini kiriting (1 dan 25 gacha) \n'))
        else: 
            end_program = True
