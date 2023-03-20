import sys
import string

cookbook = {
       "Bocadillo" : {
            "Ingredients" : "jamon, pan, queso y tomate",
            "Meal" : "Almuerzo",
            "Prep_time" : 10
            },
        "Tarta" : {
            "Ingredients" : "harina, azucar y huevos",
            "Meal" : "Postre",
            "Prep_time" : 60
            },
        "Ensalada" : {
            "Ingredients" : "aguagate, rucula, tomates y espinacas",
            "Meal" : "Almuerzo",
            "Prep_time" : 15
            }
        }

def ImprimirNombresReceta():
    for key in cookbook:
        print(key)

def ImprimirReceta():
    RecetaAImprimir = input("Introcude receta a consultar: ")
    if RecetaAImprimir in cookbook:
        receta = cookbook[RecetaAImprimir]
        print(receta)
    else:
        print(RecetaAImprimir, "not found in cookbook")

def EliminarReceta():
    RecetaAEliminar = input("Receta a eliminar: ")
    if RecetaAEliminar in cookbook:
        del cookbook[RecetaAEliminar]
    else:
        print(RecetaAEliminar, "not found in cookbook")

def AñadirReceta():
    NombreNuevaReceta = input("Introduce nueva receta: ")
    NuevosIngredients = []
    while True:
        IngredientsAAñadir = input("Introduce ingredientes: "if not NuevosIngredients else "")
        if IngredientsAAñadir == "":
            break
        NuevosIngredients.append(IngredientsAAñadir)
    NuevoMeal = input("Introcude que comida es: ")
    NuevoPrep_time = int(input("Introdice tiempo de preparación: "))
    NuevaReceta = {
        "Ingredients": ", ".join(NuevosIngredients),
        "Meal": NuevoMeal,
        "Prep_time": NuevoPrep_time
    }
    cookbook[NombreNuevaReceta] = NuevaReceta

if __name__ == "__main__":
    print("Welcome to the Python Cookbook!")
    print("List of available options:")
    print("  1: Add a recipe")
    print("  2: Delete a recipe")
    print("  3: Print a recipe")
    print("  4: Print the cookbook")
    print("  5: Quit")
    while True:
        seleccion = input("\nPlease select an option: ")
        if seleccion == "1":
            AñadirReceta()
        elif seleccion == "2":
            EliminarReceta()
        elif seleccion == "3":
            ImprimirReceta()
        elif seleccion == "4":
            ImprimirNombresReceta()
        elif seleccion == "5":
            print("Cookbook closed. Goodbye!")
            sys.exit()
        else:
            print("Sorry, this option does not exist.")