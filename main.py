from pyscript import document, when

numero_actual = "0"
numero_anterior = None
operacion_seleccionada = None
esperando_numero = False

pantalla = document.querySelector("#resultado")
texto_operacion = document.querySelector("#operacion")


def actualizar_pantalla():
    pantalla.innerText = numero_actual


def obtener_simbolo(operacion):
    if operacion == "*":
        return "×"
    elif operacion == "/":
        return "÷"
    else:
        return operacion


def escribir_numero(numero):
    global numero_actual, esperando_numero
    if numero_actual == "0" or esperando_numero:
        numero_actual = numero
        esperando_numero = False
    elif len(numero_actual) < 12:
        numero_actual += numero
    actualizar_pantalla()


def seleccionar_operacion(operacion):
    global numero_anterior, operacion_seleccionada, esperando_numero
    numero_anterior = numero_actual
    operacion_seleccionada = operacion
    esperando_numero = True
    texto_operacion.innerText = numero_anterior + " " + obtener_simbolo(operacion)


def hacer_calculo():
    global numero_actual, numero_anterior, operacion_seleccionada, esperando_numero
    if numero_anterior is None or operacion_seleccionada is None:
        return

    numero1 = float(numero_anterior)
    numero2 = float(numero_actual)

    if operacion_seleccionada == "/" and numero2 == 0:
        numero_actual = "Error"
        actualizar_pantalla()
        return

    if operacion_seleccionada == "+":
        resultado = numero1 + numero2
    elif operacion_seleccionada == "-":
        resultado = numero1 - numero2
    elif operacion_seleccionada == "*":
        resultado = numero1 * numero2
    else:
        resultado = numero1 / numero2

    if resultado.is_integer():
        resultado = int(resultado)
    else:
        resultado = round(resultado, 8)

    texto_operacion.innerText = numero_anterior + " " + obtener_simbolo(operacion_seleccionada) + " " + numero_actual + " ="

    numero_actual = str(resultado)
    numero_anterior = None
    operacion_seleccionada = None
    esperando_numero = True
    actualizar_pantalla()


def limpiar_calculadora():
    global numero_actual, numero_anterior, operacion_seleccionada, esperando_numero
    numero_actual = "0"
    numero_anterior = None
    operacion_seleccionada = None
    esperando_numero = False
    texto_operacion.innerText = ""
    actualizar_pantalla()


def agregar_decimal():
    global numero_actual, esperando_numero
    if esperando_numero:
        numero_actual = "0."
        esperando_numero = False
    elif "." not in numero_actual:
        numero_actual += "."
    actualizar_pantalla()


@when("click", "#btn-0")
def clic_0(event):
    escribir_numero("0")


@when("click", "#btn-1")
def clic_1(event):
    escribir_numero("1")


@when("click", "#btn-2")
def clic_2(event):
    escribir_numero("2")


@when("click", "#btn-3")
def clic_3(event):
    escribir_numero("3")


@when("click", "#btn-4")
def clic_4(event):
    escribir_numero("4")


@when("click", "#btn-5")
def clic_5(event):
    escribir_numero("5")


@when("click", "#btn-6")
def clic_6(event):
    escribir_numero("6")


@when("click", "#btn-7")
def clic_7(event):
    escribir_numero("7")


@when("click", "#btn-8")
def clic_8(event):
    escribir_numero("8")


@when("click", "#btn-9")
def clic_9(event):
    escribir_numero("9")


@when("click", "#btn-sumar")
def clic_sumar(event):
    seleccionar_operacion("+")


@when("click", "#btn-restar")
def clic_restar(event):
    seleccionar_operacion("-")


@when("click", "#btn-multiplicar")
def clic_multiplicar(event):
    seleccionar_operacion("*")


@when("click", "#btn-dividir")
def clic_dividir(event):
    seleccionar_operacion("/")


@when("click", "#btn-igual")
def clic_igual(event):
    hacer_calculo()


@when("click", "#btn-ac")
def clic_ac(event):
    limpiar_calculadora()


@when("click", "#btn-punto")
def clic_punto(event):
    agregar_decimal()


actualizar_pantalla()
