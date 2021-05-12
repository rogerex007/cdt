def CDT(usuario: str, capital: int, tiempo: int):
    #Variables locales
    cantidad = capital
    porcentaje_interes = 0.03
    porcentaje_perder = 0.02
    tiempo = tiempo

    #Formulas
    valor_interes = cantidad * porcentaje_interes * tiempo / 12
    valor_a_perder = cantidad * porcentaje_perder


    
 

    if(tiempo <= 2):
        #Valor si @tiempo <= 2
        valor_total = cantidad - valor_a_perder
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {cantidad} para un tiempo de {tiempo} meses es: {valor_total}"
        
    elif(tiempo >= 3):
        #Valor si @tiempo >= 3
        valor_total = valor_interes + cantidad 
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {cantidad} para un tiempo de {tiempo} meses es: {valor_total}"

def main():
    print(CDT("AB1012", 1000000, 3))
    print(CDT("QW3456", 5000000, 2))
    print(CDT("TY9087", 800000, 12))



if __name__ == "__main__":
    main()