from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def criar_doc(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Quantidade de dígitos está incorreta!')
        
class DocCpf:
    def __init__(self, documento):
        if self.validar(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido!')

    def validar(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def format(self):
        formato = CPF()
        return formato.mask(self.cpf)
    
    def __str__(self):
        return self.format()
    
class DocCnpj:
    def __init__(self, documento):
        if self.validar(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido!')

    def validar(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
    
    def format(self):
        formato = CNPJ()
        return formato.mask(self.cnpj)
    
    def __str__(self):
        return self.format()

    
    