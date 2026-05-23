#Lizbeth San Agustin Vergara

def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def restar(a, b):
    """Devuelve la resta de dos números."""
    return a - b


def multiplicar(a, b):
    """Devuelve la multiplicación."""
    return a * b


def dividir(a, b):
    """Devuelve la división."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

git add .
git commit -m "fix: eliminar línea vacía final W391"
git push
