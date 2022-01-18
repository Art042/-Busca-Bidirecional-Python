#Busca Bidirecional - Python

# Definição de Classe Nó a ser adicionada em Grafo
class No_adjacente:
	
	def __init__(objeto, vertice): 
		
		objeto.vertice = vertice
		objeto.next = None

# Implementação de busca Bidirecional
class bsc_bidirecional:
	
	def __init__(objeto, vertices):
		
		# Inicializa vertices e grafo
		objeto.vertices = vertices
		objeto.grafo = [None] * objeto.vertices
		
		# Inicializa busca em duas direções 
		# Começo para fim e fim para começo
		objeto.origem_rota = list()
		objeto.dest_rota = list()
		
		# Inicializando os nós de origem, destino, já visitados como False
		objeto.origem_visitado = [False] * objeto.vertices
		objeto.destino_visitado = [False] * objeto.vertices
		
		# Inicializa nós pais de origem e destino
		objeto.origem_pai = [None] * objeto.vertices
		objeto.dest_pai = [None] * objeto.vertices
		
	# Adição de Aresta não direcionada
	def add_aresta(objeto, origem, dest):
		
		# Adiciona Arestas no Grafo
		
		# Adiciona Destino e Origem
		node = No_adjacente(dest)
		node.next = objeto.grafo[origem]
		objeto.grafo[origem] = node

		# Adiciona Origem e Destino
		node = No_adjacente(origem)
		node.next = objeto.grafo[dest]
		objeto.grafo[dest] = node
		
	# Busca em Largura 
	# - BFS - Começo
	def bfs(objeto, direção = 'forward'):
		
		if direção == 'forward':
			
			# BFS de Começo para Fim
			atual = objeto.origem_rota.pop(0)
			conect_no = objeto.grafo[atual]
			
			while conect_no:
				vertice = conect_no.vertice
				
				if not objeto.origem_visitado[vertice]:
					objeto.origem_rota.append(vertice)
					objeto.origem_visitado[vertice] = True
					objeto.origem_pai[vertice] = atual
					
				conect_no = conect_no.next
		else:
			
			# BFS de Fim para Começo
			atual = objeto.dest_rota.pop(0)
			conect_no = objeto.grafo[atual]
			
			while conect_no:
				vertice = conect_no.vertice
				
				if not objeto.destino_visitado[vertice]:
					objeto.dest_rota.append(vertice)
					objeto.destino_visitado[vertice] = True
					objeto.dest_pai[vertice] = atual
					
				conect_no = conect_no.next
	# - BFS - Fim
				
	# Verifica se há interseção(nó) entre vértices
	def tem_intersc(objeto):
		
		# Retorna o nó correspondente a interseção
		for i in range(objeto.vertices):
			if (objeto.origem_visitado[i] and	objeto.destino_visitado[i]):
				return i
				
		return -1

	# Imprime o caminho do Começo ao destino
	def imprime_rota(objeto, no_intersec, origem, dest):

		rota = list()
		rota.append(no_intersec)
		i = no_intersec
		
		while i != origem:
			rota.append(objeto.origem_pai[i])
			i = objeto.origem_pai[i]
			
		rota = rota[::-1]
		i = no_intersec
		
		while i != dest:
			rota.append(objeto.dest_pai[i])
			i = objeto.dest_pai[i]
			
		print("*****Rota*****")
		rota = list(map(str, rota))
		
		print(' '.join(rota))
	
	# Função da Busca Bidirecional
	def bsc_bidirecional(objeto, origem, dest):
		
		# Adiciona a origem a fila
		# Vértices visitados recem True
		# Seus pais recebem -1
		
		objeto.origem_rota.append(origem)
		objeto.origem_visitado[origem] = True
		objeto.origem_pai[origem] = -1
		
		# Adiciona a Destino a fila
		# Vértices visitados recem True
		# Seus pais recebem -1
		objeto.dest_rota.append(dest)
		objeto.destino_visitado[dest] = True
		objeto.dest_pai[dest] = -1

		while objeto.origem_rota and objeto.dest_rota:
			
			# BFS de Origem a Destino 
			# A partir do Vértice inicial
			
			objeto.bfs(direção = 'forward')
			
			# BFS de Destino a origem 
			# A partir de V~ertice Destino
			objeto.bfs(direção = 'backward')
			
			# Checagem por vértice de interseção
			no_intersec = objeto.tem_intersc()
			
			# Se vértice de interseção existe
			# Então a rota da origem ao destino é verdadeira 
			if no_intersec != -1:
				print(f"Rota entre {origem} e {dest} existe")
				print(f"Interseção : {no_intersec}")
				objeto.imprime_rota(no_intersec, origem, dest)
				exit(0)
		return -1

# Definição de Rota de Busca Bidirecional

''' if __name__ == '__main__': testa se o arquivo de script Python 
está sendo executado como arquivo principal ou não. 
Isto é útil para evitar certos comportamentos caso 
seu script seja importado como módulo de outro script.'''

if __name__ == '__main__':
	
	# Numero de vertices no Grafo
	n = 15
	
	# Vertice inicial (origem)
	origem = 0
	
	# Vertice destino
	dest = 14
	
	# Criação de Grafo
	grafo = bsc_bidirecional(n)
	grafo.add_aresta(0, 4)
	grafo.add_aresta(1, 4)
	grafo.add_aresta(2, 5)
	grafo.add_aresta(3, 5)
	grafo.add_aresta(4, 6)
	grafo.add_aresta(5, 6)
	grafo.add_aresta(6, 7)
	grafo.add_aresta(7, 8)
	grafo.add_aresta(8, 9)
	grafo.add_aresta(8, 10)
	grafo.add_aresta(9, 11)
	grafo.add_aresta(9, 12)
	grafo.add_aresta(10, 13)
	grafo.add_aresta(10, 14)
	
	imprime = grafo.bsc_bidirecional(origem, dest)
	
	if imprime == -1:
		print(f"Rota entre {origem} e {dest} não Existe")



