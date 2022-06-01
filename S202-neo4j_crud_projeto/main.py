from pprintpp import pprint as pp
from db.database import Graph


class PessoaDAO(object):
    def __init__(self):
        self.db = Graph(uri='bolt://44.195.39.243:7687',
                        user='neo4j', password='equations-cube-maneuvers')

    def read_by_nome(self, nome):
        return self.db.execute_query('MATCH (n:Pessoa {nome:$nome}) RETURN n',
                                     {'nome': nome})
    
    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def read_nobres(self):
        return self.db.execute_query('MATCH (n:Nobre) RETURN n')

    def read_guerreiros(self):
        return self.db.execute_query('MATCH (n:Guerreiro) RETURN n')
    
    def read_mortos(self):
        return self.db.execute_query('MATCH (n:Pessoa {vivo:false}) RETURN n')

    def read_relation_aliado(self):
        return self.db.execute_query('MATCH (n:Pessoa)-[r:ALIADO_DE]->(m:Pessoa) RETURN n, m')

    def read_relation_filhos_do_ned(self):
        return self.db.execute_query('''MATCH (n:Pessoa{nome: "Ned Stark"})-[r:PAI_MAE_DE]->
        (m:Pessoa) RETURN m ''')
    
    def read_relation_pais_do_jon(self):
        return self.db.execute_query('MATCH (n:Pessoa)-[r:PAI_MAE_DE]->(m:Pessoa{nome: "Jon Snow"}) RETURN n')
    
    def read_relation_irmaos(self, nome):
        return self.db.execute_query('MATCH (n:Pessoa{nome: $nome})-[r:IRMAO_IRMA_DE]->(m:Pessoa) RETURN m',
                                     {'nome': nome})

    def read_relation_bastardos(self):
        return self.db.execute_query('MATCH (n:Pessoa)-[r:PAI_MAE_DE{legitimo: false}]->(m:Pessoa) RETURN m')

def divider():
    print('\n' + '-' * 80 + '\n')

dao = PessoaDAO()

while 1:    
    option = input('''1. Todas as pessoas da familia
2. Buscar por nome
3. Quem da familia eh nobre ?
4. Quem da familia eh guerreiro ?
5. Quem da familia ja morreu ? 
6. Quem da familia eh aliado de quem ?
7. Ned Stark eh pai de quem ?
8. Quem sao os pais de Jon Snow ? 
9. Quais sao os irmaos de ?
10.Existe algum bastardo ?

''')

    if option == '1':
        aux = dao.read_all_nodes()
        pp(aux)
        divider()

    elif option == '2':
        nome = input('  nome: ')
        aux = dao.read_by_nome(nome)
        pp(aux)
        divider()

    elif option == '3':
        aux = dao.read_nobres()
        pp(aux)
        divider()

    elif option == '4':
        aux = dao.read_guerreiros()
        pp(aux)
        divider()
    elif option == '5':
        aux = dao.read_mortos()
        pp(aux)
        divider()

    elif option == '6':
        aux = dao.read_relation_aliado()
        pp(aux)
        divider()

    elif option == '7':
        aux = dao.read_relation_filhos_do_ned()
        pp(aux)
        divider()
    elif option == '8':
        aux = dao.read_relation_pais_do_jon()
        pp(aux)
        divider()

    elif option == '9':
        nome = input('  nome: ')
        aux = dao.read_relation_irmaos(nome)
        pp(aux)
        divider()

    elif option == '10':
        aux = dao.read_relation_bastardos()
        pp(aux)
        divider()

    else:
        break

dao.db.close()