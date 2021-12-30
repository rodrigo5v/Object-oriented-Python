class Banco():
    """
    Classe usada para representar um Banco

    ...

    Atributos
    ---------
    titular : str
        String que representa o nome do titular da conta
    num_conta : str
        O número da conta do usuário , sendo uma string pois contém caracteres especiais (-)
    saldo : int
        Inteiro positivo que representa o valor monetário guardado em sua conta
    id_conta : str
        Últimos três digitos do número da conta do titular, para identificar o seu banco
    our_account_bra : boolean
        Valida se os últimos digitos da conta do titual são do Bradesco
    our_account_ita : boolean
        Valida se os últimos digitos da conta do titual são do Itaú

    Metódos
    -------
    transferencia(num_conta_desti, valor)
        Realiza uma transferência bancária
    
    info_conta()
        Retorna as informações do usuário, sendo elas o número da conta e nome do titular

    verifica_id()
        Compara o id_conta com o identificador de cada banco
    """
    id_conta = ''
    our_account_bra = None
    our_account_ita = None

    def __init__(self, titular : str, num_conta : str, saldo : float):
        """
        Paramâtros
        ----------
        titular : str
            O nome do dono da conta bancária
        num_conta : str
            A numeração respectiva a sua conta
        saldo : float
            Quantidade de dinheiro armazenada no banco
        """
        self.titular = titular
        self.num_conta = num_conta
        self.saldo = saldo
        self.id_conta = num_conta[0:3]
        self.verifica_id()

    def transferencia(self, num_conta_desti, valor):
        """Debita o valor passado como parâmetro e o repassa a conta do destinatário.
        
        Verifica se o número da conta do destinátario não é a mesma do titular.

        Se as condições forem atendidas o valor é debitado do saldo do titular e 
        transferido ao destinatário. Caso contrário uma mensagem é printada ao usuário.

        Parâmetros
        ----------
        num_conta_desti : str
            O número do beneficiário que irá receber a transferência

        valor : float
            A quantidade a ser transferida de conta.
        """

        if self.num_conta != num_conta_desti:
            if self.saldo > valor:
                return print(f'O valor de R$ {valor} foi transferido a {num_conta_desti}')
            elif self.saldo < valor:
                return print(f'Impossível fazer a transferência, saldo insuficiente.')

    def info_conta(self):
        """
        Retorna as informações armazenadas na classe ao usuário
        """
        return print(f'{self.titular} é titular da conta: {self.num_conta}')

    def verifica_id(self):
        """
        Compara o atributo id_conta com os identificadores de cada banco e define True
        para our_account_bra (caso Bradesco) ou para our_account_ita (caso Itaú)
        """
        if self.id_conta == '247':
            self.our_account_bra = True
        elif self.id_conta == '341':
            self.our_account_ita = True

class Itau(Banco):
    """
    Classe usada para representar o banco Itaú

    ...

    Atributos
    ---------
    A classe Itaú herda os atributos de Banco

    Metódos
    -------
    transferencia(num_conta_desti, valor)
        Transferência bancária a uma conta específica
    """

    def transferencia(self, num_conta_desti : str, valor : float):
        """Debita o valor passado como parâmetro e o repassa a conta do destinatário.
        
        Verifica se o número da conta do destinátario não é a mesma do titular.

        Calcula se o valor do custo de transferência é menor que o saldo da conta.

        Se as condições forem atendidas o valor é debitado do saldo do titular e 
        transferido ao destinatário. Caso contrário uma mensagem é printada ao usuário.

        Parâmetros
        ----------
        num_conta_desti : str
            O número do beneficiário que irá receber a transferência

        valor : float
            A quantidade a ser transferida de conta.
        """

        if self.our_account_ita == True:
            custo_transf = (valor * 0.01) + valor

            if self.num_conta != num_conta_desti:
                if self.saldo > custo_transf:
                    self.saldo -= custo_transf
                    return print(f'O valor de R$ {custo_transf} foi transferido a {num_conta_desti}')
                elif self.saldo < custo_transf:
                    return print(f'Seu saldo de R$ {self.saldo} é insuficiente para transferência de {valor}')
            else:
                return print('Não é possível transferir da sua conta para a mesma.')
        else:
            return print('Sua conta não pertence a este banco.')
        
        return super().transferencia(num_conta_desti, valor)

class Bradesco(Banco):
    """
    Classe usada para representar o banco Bradesco

    ...

    Atributos
    ---------
    A classe Bradesco herda os atributos de Banco

    Metódos
    -------
    transferencia(num_conta_desti, valor)
        Transferência bancária a uma conta específica
    """

    def transferencia(self, num_conta_desti : str, valor : float):
        """Debita o valor passado como parâmetro e o repassa a conta do destinatário.
        
        Verifica se o número da conta do destinátario não é a mesma do titular.

        Calcula se o valor do custo de transferência é menor que o saldo da conta.

        Se as condições forem atendidas o valor é debitado do saldo do titular e 
        transferido ao destinatário. Caso contrário uma mensagem é printada ao usuário.

        Parâmetros
        ----------
        num_conta_desti : str
            O número do beneficiário que irá receber a transferência

        valor : float
            A quantidade a ser transferida de conta.
        """
        if self.our_account_bra == True:
            custo_transf = (valor * 0.05) + 5 + valor

            if self.num_conta != num_conta_desti:
                if self.saldo > custo_transf:
                    self.saldo -= custo_transf
                    return print(f'O valor de R$ {custo_transf} foi transferido a {num_conta_desti}')
                elif self.saldo < custo_transf:
                    return print(f'Seu saldo de R$ {self.saldo} é insuficiente para transferência de {valor}')
            
            else:
                return print('Não é possível transferir da sua conta para a mesma.')                

        else:
            return print('Sua conta não pertence a este banco.')

        return super().transferencia(num_conta_desti, valor)