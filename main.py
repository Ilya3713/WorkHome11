import requests

API_KEY = 'trnsl.1.1.20190704T044537Z.54fabf014292e3df.1b48e06ff47b9e8f16108fedc7a5a74b5d993d9d'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(way, newway, lan, to_lang = 'ru'):

  text = ''
  try:
    with open(way, 'r', encoding='utf8') as f:
      for texts in f:
        text += texts
  
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(lan, to_lang),
    }
  
    response = requests.get(URL, params = params)
    json_ = response.json()
    newtext = ''.join(json_['text'])
  
      

    my_file = open(newway, 'w')
    my_file.write(newtext)
    my_file.close()
    
    with open(newway, 'r', encoding='utf8') as f:
      for texts in f:
        text += texts
    print('Текст перевода нового файла: \n',  newtext)
  except FileNotFoundError:
    print('Данного файла нет')    
  except KeyError:
    print('Ошибка. Неверный формат языка')

way = ''
newway = ''
lan = ''
to_lang = ''

way = input('Введите путь к файлу(Например: DE.txt)')
newway = input('Введите путь к новому файлу(Например: newDE.txt)')
lan = input('Введите язык с которого перевести(Например: de)')
to_lang = input('Введите на какой язык перевести(Например: ru)')

translate_it(way, newway, lan, to_lang)



