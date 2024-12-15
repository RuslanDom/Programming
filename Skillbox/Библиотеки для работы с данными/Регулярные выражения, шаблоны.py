import re

text = r'Win nie-the-Po oh sat down at the foot of the tree.'

# Задача: Слова на гласную букву
# Правила паттерна:
#   Начало слова на одну из гласных букв: aeiou
#   Любой регистр: aeiou и AEIOU
#   Нет ограничений на количество букв в слове

# r'.' - обозначает все знаки, кроме символа пропуска строки ['W', 'i', 'n',' ', 'n', 'i', 'e', '-', 't'...
# r'\w' - обозначает любую букву или цифру ['W', 'i', 'n', 'n', 'i', 'e', 't', 'h', 'e'...
# r'+' - обозначает что шаблон будет повторяться 1 и более раз пример: r'\w+' ['Win', 'nie', 'the', 'Po',
# r'[]' - позволяет отобрать указанные символы ['in', 'ie', 'oh', 'at', 'own'...
# r'\b' - обозначает границу
pattern = r'\b\w{4}\b'  # Все слова из 4 символов (букв и цифр)
result = re.findall(r'\b[aeiouAEIOU]\w+', text)
print(result)

deep_ocean = """
                 oCean Ocean ocEan oceaN oCEan OCEAN OCeaN OceaN oCeN
                 ocEAN oCeAn OcEaN OCean oceAN ocean OCEan OCeN ocAen
                 Ocena oCeNa ocAn Ocone OCoce neoca canoe onen Neoca
                 nECoa Enoca ecaNo Necom mecon Necma oacme oaenc Cnema
                 neoma aemca Nemo ocema Oneca Necom meNo ceoa Aneca
                 ocEAN oCeAn OcEaN OCean oceAN ocean OCEan OCaeN ocAen
                 Ocen oCeNa ocne Ocone OCoce neoca canoe Conen Neoca
                 nECoa Enoca eaNo Necom mecon Necma oacme nemoa Cnem
                 nECoa Enoca ecaNo Necom mecon nem0 oacme oaenc Cnema   
             """
nemo_pattern = r'[Nn]em\w{0,2}'
full_search = re.findall(nemo_pattern, deep_ocean)
print(full_search)

nemo_matched = re.search(r'Nemo', deep_ocean)
print(f'Немо в тексте: {nemo_matched.group(0)}')

transparent = re.sub(r'[Oo]\w{4}\s+', '', deep_ocean)  # Все слова на [Оо] будут заменены на ''
# в {4} - кол-во повторений \w
# \s - заменяет пробельный символ
print(transparent)

print('=' * 60)
# Задача про паттерны автомобильных номеров

auto_nums = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

pattern_private_auto = r'\b[АВЕКМНОРСТУХ]\d{3}\w{2}\d{2,3}'
pattern_taxi = r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}'
print(f"Список номеров частных автомобилей: {re.findall(pattern_private_auto, auto_nums)}")
print(f"Список номеров такси: {re.findall(pattern_taxi, auto_nums)}")

print('=' * 60)
s = '<h3>abc</h3><h3>def</h3>'
ex1 = re.findall(r'<h3.*>.*</h3>', s)
ex2 = re.findall(r'<h3.*?>.*?</h3>', s)
ex3 = re.findall(r'<h3.*>(.*)</h3>', s)
ex4 = re.findall(r'<h3.*?>(.*?)</h3>', s)
print(ex1, ex2, ex3, ex4, sep='\n')
