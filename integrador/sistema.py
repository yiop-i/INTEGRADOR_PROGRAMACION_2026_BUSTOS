import gestion_stock
import menu

def main():
    gestion_stock.inicializar()
    opcion = 67
    while opcion != 0:
        opcion = menu.mostrar_menu()
        if opcion == 1:
            gestion_stock.cargar_stock()
        elif opcion == 2:
            gestion_stock.mostrar_stock()
        elif opcion == 3:
            gestion_stock.contar_categoria()
        elif opcion == 0:
            print("Saliendo del programa... \n(no me manden a diciembre porfa, suficiente con las otras materias)")
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()