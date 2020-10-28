import re

inp = "Иван Иванович! Нужен ответ на письмо от ivanoff@ivan-chai.ru. Не забудьте поставить в копию serge'o-lupin@mail.ru- это важно.ivanoff@ivan-chai.ru serge'o-lupin@mail.ru NO: foo.@ya.ru, foo@.ya.ru PARTLY: boo@ya_ru, -boo@ya.ru-, foo№boo@ya.ru"
my_input = 'asda@das.ru  foo@boo@goo@moo@roo@zoo as2da@12das.ru a.s2da@12das.ru a_s-2da@12das.ru a_s-2da@12das.ru'
input_test = 'NO: foo.@ya.ru, foo@.ya.ru PARTLY: boo@ya_ru, -boo@ya.ru-, foo№boo@ya.ru'
match = re.findall(r'[\w][\w.-]+[\w]@[\w][\w.-]+[.][\w0-9]{2,3}', input_test)
print(match)
