import sys
class Pessoa():
	def __init__(self, nome=None, idade=44, *args, **kwargs):
		self.idade = idade
		self.nome = nome
		return super().__init__(*args, **kwargs)

	def cumprimentar(self):
		return f'Olá {id(self)}'

def main():
	p = Pessoa('Marcos')
	print(Pessoa(p))
	print(id(p))
	print(p.cumprimentar())
	print(p.nome)
	p.nome = 'Ederson'
	print(p.nome)
	print(p.idade)

if __name__ == "__main__":
    sys.exit(int(main() or 0))
