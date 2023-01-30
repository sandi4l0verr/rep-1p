from flask import Blueprint, request, jsonify

login = Blueprint ('login', __name__)



@login.route('/login', methods=['POST'])
def llamarServicioSet():
    global user,password

    user =request.json['user']
    password =request.json['password']
    inicializarVariables(user,password)


    salida = {'codRes': codRes, 'menRes': menRes, 'usuario': user, 'accion':accion}
    return jsonify(salida)


def inicializarVariables(user,password):
    global codRes, menRes,accion
    userLocal="pcabrera"
    passLocal="michi123"
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    try:
        print("Verificar login")
        if(str(password)==str(passLocal) and str(user)==(userLocal)):
            print("Usuario y contraseña OK ")
            accion="succes"
        else:
            print("usuario o contraseña incorrecta")
            accion="usuario o conttraseña incorrecta"

    except Exception as e:
        print ("ERROR",str(e))
        codRes='ERROR'
        menRes='Msg'+str(e)

