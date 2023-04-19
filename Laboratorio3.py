import graphviz
import re

def build_tree(expr):
    # Convertimos la expresión aritmética en una lista de tokens
    tokens = re.findall(r'\d+|\+|\-|\*|\/|\(|\)', expr)
    
    # Creamos un gráfico de graphviz
    graph = graphviz.Digraph()
    
    # Llamamos a la función helper para construir el árbol
    build_tree_helper(tokens, graph)
    
    # Devolvemos el gráfico
    return graph

def build_tree_helper(tokens, graph):
    # Si la lista de tokens está vacía, salimos de la función
    if not tokens:
        return
    
    # Obtenemos el primer token de la lista
    token = tokens.pop(0)
    
    # Si el token es un número, lo agregamos al gráfico
    if token.isdigit():
        graph.node(token)
        return token
    
    # Si el token es un operador, creamos un nuevo nodo para él
    graph.node(token)
    
    # Llamamos recursivamente a la función helper para crear el subárbol izquierdo
    left = build_tree_helper(tokens, graph)
    
    # Llamamos recursivamente a la función helper para crear el subárbol derecho
    right = build_tree_helper(tokens, graph)
    
    # Agregamos una arista desde el nodo del operador a los subárboles izquierdo y derecho
    graph.edge(token, left)
    graph.edge(token, right)
    
    # Devolvemos el nodo del operador
    return token

# Función para mostrar el menú
def show_menu():
    print("1. Ingresar expresión aritmética")
    print("2. Salir")

# Ciclo principal del programa
while True:
    # Mostramos el menú
    show_menu()
    
    # Pedimos al usuario que ingrese una opción
    choice = input("Ingrese una opción: ")
    
    # Si el usuario eligió salir, salimos del programa
    if choice == '2':
        break
    
    # Si el usuario eligió ingresar una expresión aritmética, pedimos la expresión y construimos el árbol
    elif choice == '1':
        expr = input("Ingrese la expresión aritmética: ")
        graph = build_tree(expr)
        graph.render('expr.gv', view=True)
    
    # Si el usuario ingresó una opción inválida, mostramos un mensaje de error
    else:
        print("Opción inválida. Inténtelo de nuevo.")