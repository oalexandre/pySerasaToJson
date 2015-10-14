# -*- coding: utf-8 -*-
from registrosDados import RegistrosB49C
from registrosDados import RegistrosP002
from registrosDados import RegistrosN001
from registrosDados import RegistrosN002_subtipo00
from registrosDados import RegistrosN002_subtipo01
from registrosDados import RegistrosN003
from registrosDados import RegistrosN200_subtipo00
from registrosDados import RegistrosN200_subtipo01
from registrosDados import RegistrosN210_subtipo00
from registrosDados import RegistrosN210_subtipo01
from registrosDados import RegistrosN210_subtipo99
from registrosDados import RegistrosN220
from registrosDados import RegistrosN230_subtipo00
from registrosDados import RegistrosN230_subtipo90
from registrosDados import RegistrosN230_subtipo99
from registrosDados import RegistrosN240_subtipo00
from registrosDados import RegistrosN240_subtipo01
from registrosDados import RegistrosN240_subtipo90
from registrosDados import RegistrosN240_subtipo99
from registrosDados import RegistrosN250_subtipo00
from registrosDados import RegistrosN250_subtipo01
from registrosDados import RegistrosN250_subtipo90
from registrosDados import RegistrosN250_subtipo99
from registrosDados import RegistrosN270_subtipo00
from registrosDados import RegistrosN270_subtipo90
from registrosDados import RegistrosN270_subtipo99
from registrosDados import RegistrosN440_subtipo00
from registrosDados import RegistrosN440_subtipo01
from registrosDados import RegistrosN440_subtipo02
from registrosDados import RegistrosN440_subtipo03
from registrosDados import RegistrosN440_subtipo99
from registrosDados import RegistrosT999
from bloco import Bloco


class pendenciasInternas(Bloco):
    blocos = []

    def __init__(self):
        self.nome = "pendenciasInternas"


class pendenciasFinanceiras(Bloco):
    blocos = []

    def __init__(self):
        self.nome = "pendenciasFinanceiras"


class protestosEstados(Bloco):
    blocos = []

    def __init__(self):
        self.nome = "protestosEstados"


class chequesSemFundos(Bloco):
    blocos = []

    def __init__(self):
        self.nome = "chequesSemFundos"


class blocoB49C(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registros do Protocolo"
        self.nome = nome
        self.campos = RegistrosB49C(bloco)


class blocoP002(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registros adicionais ao Protocolo"
        self.nome = nome
        self.campos = RegistrosP002(bloco)


class blocoN001(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registros adicionais ao Protocolo"
        self.nome = nome
        self.campos = RegistrosN001(bloco)


class blocoN002_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registros adicionais ao Protocolo"
        self.nome = nome
        self.campos = RegistrosN002_subtipo00(bloco)

class blocoN002_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registros adicionais ao Protocolo"
        self.nome = nome
        self.campos = RegistrosN002_subtipo01(bloco)


class blocoN003(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registros adicionais ao Protocolo"
        self.nome = nome
        self.campos = RegistrosN003(bloco)


class blocoN200_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Bloco de informações do Confirmei"
        self.nome = nome
        self.campos = RegistrosN200_subtipo00(bloco)


class blocoN200_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Bloco de informações do Confirmei"
        self.nome = nome
        self.campos = RegistrosN200_subtipo01(bloco)


class blocoN210_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Alerta de Documentos Roubados"
        self.nome = nome
        self.campos = RegistrosN210_subtipo00(bloco)


class blocoN210_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Alerta de Documentos Roubados"
        self.nome = nome
        self.campos = RegistrosN210_subtipo01(bloco)


class blocoN210_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Alerta de Documentos Roubados"
        self.nome = nome
        self.campos = RegistrosN210_subtipo99(bloco)


class blocoN220(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Nada Consta"
        self.nome = nome
        self.campos = RegistrosN220(bloco)


class blocoN230_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Pendencias Internas"
        self.nome = nome
        self.campos = RegistrosN230_subtipo00(bloco)


class blocoN230_subtipo90(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Pendencias Internas"
        self.nome = nome
        self.campos = RegistrosN230_subtipo90(bloco)


class blocoN230_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Pendencias Internas"
        self.nome = nome
        self.campos = RegistrosN230_subtipo99(bloco)


class blocoN240_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Pendências Financeiras"
        self.nome = nome
        self.campos = RegistrosN240_subtipo00(bloco)


class blocoN240_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Pendências Financeiras"
        self.nome = nome
        self.campos = RegistrosN240_subtipo01(bloco)


class blocoN240_subtipo90(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Pendências Financeiras"
        self.nome = nome
        self.campos = RegistrosN240_subtipo90(bloco)


class blocoN240_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Pendências Financeiras"
        self.nome = nome
        self.campos = RegistrosN240_subtipo99(bloco)


class blocoN250_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Protestos do Estado"
        self.nome = nome
        self.campos = RegistrosN250_subtipo00(bloco)


class blocoN250_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Protestos do Estado"
        self.nome = nome
        self.campos = RegistrosN250_subtipo01(bloco)


class blocoN250_subtipo90(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Protestos do Estado"
        self.nome = nome
        self.campos = RegistrosN250_subtipo90(bloco)


class blocoN250_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Protestos do Estado"
        self.nome = nome
        self.campos = RegistrosN250_subtipo99(bloco)


class blocoN270_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Cheques sem fundos - Bacen"
        self.nome = nome
        self.campos = RegistrosN270_subtipo00(bloco)


class blocoN270_subtipo90(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Cheques sem fundos - Bacen"
        self.nome = nome
        self.campos = RegistrosN270_subtipo90(bloco)


class blocoN270_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Cheques sem fundos - Bacen"
        self.nome = nome
        self.campos = RegistrosN270_subtipo99(bloco)


class blocoN440_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registro de Consultas"
        self.nome = nome
        self.campos = RegistrosN440_subtipo00(bloco)


class blocoN440_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registro de Consultas"
        self.nome = nome
        self.campos = RegistrosN440_subtipo01(bloco)


class blocoN440_subtipo02(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registro de Consultas"
        self.nome = nome
        self.campos = RegistrosN440_subtipo02(bloco)


class blocoN440_subtipo03(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registro de Consultas"
        self.nome = nome
        self.campos = RegistrosN440_subtipo03(bloco)


class blocoN440_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registro de Consultaas"
        self.nome = nome
        self.campos = RegistrosN440_subtipo99(bloco)


class blocoT999(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Trailler - Fim dos dados"
        self.nome = nome
        self.campos = RegistrosT999(bloco)
