def ingresar_calificaciones():
  nombre_materias = []
  calificaciones = []
  seguir = True
  calificacion_numerica = 0
  
  while seguir:
    
    nombre_materia = input("Ingresa el nombre de la materia: ")
    calificacion = input("Ingresa la calificación: ")

    if not calificacion.isnumeric():
      return 'ERROR: La calificación debe ser un número'
    
    calificacion_numerica = int(calificacion)

    if calificacion_numerica < 0 or calificacion_numerica > 10:
      return 'ERROR: Calificación fuera del rango permitido [0,10]'
    
    nombre_materias.append(nombre_materia)
    calificaciones.append(calificacion_numerica)

    seguir_text = input("¿Deseas seguir ingresando materias y calificaciones (S/N)?")
    
    match seguir_text:
      case 'S': 
        seguir = True
      case 's':
        seguir = True
      case 'n':
        seguir = False
      case 'N':
        seguir = False
      case _: 
        return 'ERROR: Opción inválida'
  
  return nombre_materias, calificaciones
    
def calcular_promedio(calificaciones:list):

   longitud_lista = len(calificaciones)

   if longitud_lista == 0:
      return 0
   
   return sum(calificaciones)/longitud_lista


def determinar_estado(calificaciones:list, umbral=5):
   lista_aprobados = []
   lista_reprobados = []

   for i, calificacion in enumerate(calificaciones):
      if calificacion > 5:
         lista_aprobados.append(i)
      else:
        lista_reprobados.append(i)

   return lista_aprobados, lista_reprobados

def encontrar_extremos(calificaciones:list):
   if not calificaciones:
      return None, None
   
   calificacion_alta = max(calificaciones)
   calificacion_baja = min(calificaciones)
   
   return calificaciones.index(calificacion_alta), calificaciones.index(calificacion_baja)

def main():
   nombre_materias, calificaciones = ingresar_calificaciones()

   if nombre_materias is None or calificaciones is None:
      print("No se ingresaron materias ni calificaciones.")
      return
   print(f"Materias ingresadas: {', '.join(nombre_materias)}")
   print(f"Calificaciones ingresadas: {', '.join(str(calificacion) for calificacion in calificaciones)}")
   
   promedio = calcular_promedio(calificaciones)

   print(f"El promedio general de las calificaciones es: {promedio:.2f}")

   aprobados, reprobados = determinar_estado(calificaciones)

   print(f"Materias aprobadas: {', '.join(nombre_materias[i] for i in aprobados)}")
   print(f"Materias reprobadas: {', '.join(nombre_materias[i] for i in reprobados)}")

   indice_alta, indice_baja = encontrar_extremos(calificaciones)

   if indice_alta is not None and indice_baja is not None:
      print(f"Materia con la calificación más alta: {nombre_materias[indice_alta]} (Calificación: {calificaciones[indice_alta]})")
      print(f"Materia con la calificación más baja: {nombre_materias[indice_baja]} (Calificación: {calificaciones[indice_baja]})")

if __name__ == "__main__":
   main()