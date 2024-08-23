from datetime import date # Importa as classes date e datetime do módulo datetime

# Classe Endereço
class Endereco:
    def __init__(self, logradouro="", numero="", endereco_comercial=False):
        # Inicializa os atributos logradouro, numero e endereco_comercial com valores padrão
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_comercial = endereco_comercial
    
# Classe Pessoa
class Pessoa:
    def __init__(self, nome="", rendimento=0.0, endereco=None):
        # Inicializa os atributos nome, rendimento e endereco
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco

    def calcular_imposto(self, rendimento):
        # Método para calcular imposto, retorna o rendimento como padrão (deve ser sobrescrito)
        return rendimento


# Classe Pessoa Física herdando características da Classe Pessoa
class PessoaFisica(Pessoa):
    # Inicializa os atributos herdados e específicos de PessoaFisica
    def __init__(self, nome="", rendimento=0.0, endereco=None, cpf="", data_nascimento=None):

        if endereco is None:
            # Se nenhum endereço for fornecido, cria um objeto Endereco padrão
            endereco = Endereco()
        if data_nascimento is None:
            # Se nenhuma data de nascimento for fornecida, usa a data de hoje
            data_nascimento = date.today()
        super().__init__(nome, rendimento, endereco)
        # Chama o construtor da superclasse Pessoa para inicializar os atributos herdados: nome, rendimento e endereco
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def calcular_imposto(self, rendimento: float) -> float:
        # Método para calcular imposto baseado no rendimento
        if rendimento <= 1500:
            # Sem imposto para rendimentos até 1500
            return 0
        elif 1500 < rendimento <= 3500:
            # 2% de imposto para rendimentos entre 1500 e 3500
            return (rendimento / 100) * 2
        elif 3500 < rendimento <= 6000:
            # 3.5% de imposto para rendimentos entre 3500 e 6000
            return (rendimento / 100) * 3.5
        else:
            # 5% de imposto para rendimentos acima de 6000
            return (rendimento / 100) * 5
        
class PessoaJuridica(Pessoa):
    def __init__(self, nome="", rendimento=0.0, endereco=None, cnpj=""):
        if endereco is None:
            # Se nenhum endereço for fornecido, cria um objeto Endereco padrão
            endereco = Endereco()
        super().__init__(nome, rendimento, endereco)
        # Chama o construtor da superclasse Pessoa para inicializar os atributos herdados: nome, rendimento e endereco
        self.cnpj = cnpj

    def calcular_imposto(self, rendimento: float) -> float:
        # Método para calcular imposto baseado no rendimento para Pessoa Jurídica
        if rendimento <= 20000:
                # 10% de imposto para rendimentos até 20000
            return (rendimento / 100) * 10
        elif 20000 < rendimento <= 50000:
                # 15% de imposto para rendimentos entre 20000 e 50000
            return (rendimento / 100) * 15
        else:
                # 20% de imposto para rendimentos acima de 50000
            return (rendimento / 100) * 20