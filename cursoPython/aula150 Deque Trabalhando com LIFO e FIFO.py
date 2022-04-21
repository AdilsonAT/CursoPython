
# Pilha - LIFO
livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')
print(livros)
livro_removido = livros.pop()
print(livros, livro_removido)
livro_removido = livros.pop()
print(livros, livro_removido)
livro_removido = livros.pop()
print(livros, livro_removido)
livro_removido = livros.pop()
print(livros, livro_removido)
livro_removido = livros.pop()
print(livros, livro_removido)

# Fila - FIFO
from collections import deque
from time import sleep

fila = deque()
print(fila)
fila.append('Livro 1')
fila.append('Livro 2')
fila.append('Livro 3')
fila.append('Livro 4')
fila.append('Livro 5')
print(fila)
saiu = fila.popleft()
print(fila, saiu)
saiu = fila.popleft()
print(fila, saiu)
saiu = fila.popleft()
print(fila, saiu)
saiu = fila.popleft()
print(fila, saiu)
saiu = fila.popleft()
print(fila, saiu)

fila = deque(maxlen=5)
fila.extend([1, 2, 3, 4])
print(fila)
fila.append(5)
print(fila)
fila.append(6)
print(fila)
fila.append(7)
print(fila)

fila = deque(maxlen=10)
for i in range(1000):
    fila.append(i)
    sleep(1)
    print(fila)


