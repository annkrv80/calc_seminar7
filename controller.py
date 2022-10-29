import view
import model


def run(log):
   log.info('Показываю меню')
   opt = view.show_menu()
   log.warn('Меню показано')
   if opt == '1':
      log.info('Выбран калькулятор')
      res = view.show_calc_enter()
      res = model.calc(res,log)
      view.show_calc_res(res)

   if opt == '2':
      log.info('Выбран конвектор')
      kg = view.show_convert_enter()
      res = model.convert(kg,log)
      view.show_convert_res([kg, res])
