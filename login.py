from flask import Blueprint, request, jsonify

login = Blueprint ('login', __name__)



@login.route('/login', methods=['POST'])
def llamarServicioSet():
    global user,passw

    user =request.json['user']
    password =request.json['password']
    inicializarVariables(user, password)

def inicializarVariables(user,password)
global codRes, menRes,accion
userLocal="dcaballero"
passLocal="unida123"
codRes = 'SIN_ERROR'
menRes = 'OK'
try:
    print("verificar login")
    if(str(password)==str(passLocal) and str(user)==str(userLocal)):
        print("usuario y contraseña CORRECTO")
        accion:"succes"
        else:
            print("usuario o contraseña INCORRECTA")
            accion="Usuario o contraseña INCORRECTA"

    except Exception as e:
        print("ERROR", str"e")
        codRes='ERROR'
        menRes='Msg'+str(e)

    

  