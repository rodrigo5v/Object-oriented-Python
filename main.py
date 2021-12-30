import banco

my_count01 = banco.Bradesco('Rodrigo Souza Vieira','341016-5',1000)
my_count01.transferencia('341700-3',100)

my_count02 = banco.Bradesco('Rodrigo Souza Vieira','247016-5',1000)
my_count02.transferencia('247016-5',100)
my_count02.transferencia('341700-3',1000)
my_count02.transferencia('341700-3',100)

my_count03 = banco.Itau('Rodrigo Souza Vieira','341016-5',1000)
my_count03.transferencia('247016-5',100)
my_count03.transferencia('341700-3',1000)
my_count03.transferencia('341016-5',100)