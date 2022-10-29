def calc(text,log):
    try:
        return eval(text)
    except SyntaxError:
        log.error(f'Синтаксическая ошибка {text}')
        return 'Ошибка ввода'
 
def convert(kg,log):
    try:
        return int(kg)*1000
    except ValueError:
        log.error(f'При конвертации {kg} в грамму возникла ошибка приведения к INT')
        return 'Ошибка ввода'