import time
import random

class HijoProdigo:
    """
    Clase que representa el ciclo de vida y decisiones del Hijo Pródigo.
    Aplica principios de POO: Encapsulamiento y Abstracción.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100.0
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento = 0
        self.vivo = True

    def mostrar_estado(self):
        print(f"\n--- ESTADO DE {self.nombre.upper()} ---")
        print(f"💰 Dinero: ${self.dinero:.2f} | 🎭 Dignidad: {self.dignidad}")
        print(f"🍔 Hambre: {self.hambre} | 🛐 Arrepentimiento: {self.arrepentimiento}")
        print("------------------------------")

    def gastar_todo(self):
        print("\n🎉 ¡Decidiste derrocharlo todo en fiestas!")
        self.dinero = 0
        self.dignidad = max(0, self.dignidad - 25)
        self.hambre = min(100, self.hambre + 40)
        self.arrepentimiento += 10
        time.sleep(1)

    def invertir(self):
        if self.dinero >= 20:
            print("\n📈 Invirtiendo en negocios locales...")
            exito = random.choice([True, False])
            if exito:
                ganancia = random.uniform(30, 60)
                self.dinero += ganancia
                print(f"✅ ¡Éxito! Ganaste ${ganancia:.2f}")
            else:
                self.dinero -= 20
                print("❌ El negocio fracasó. Perdiste $20.")
        else:
            print("\n⚠️ No tienes suficiente dinero para invertir.")
        time.sleep(1)

    def trabajar(self):
        print("\n🔨 Buscando trabajo en las porquerizas...")
        pago = random.uniform(10, 25)
        self.dinero += pago
        self.hambre += 15
        self.dignidad = min(100, self.dignidad + 5)
        print(f"💼 Trabajaste duro. Ganaste ${pago:.2f} pero tienes más hambre.")
        time.sleep(1)

    def reflexionar(self):
        if self.hambre > 70 or self.dinero <= 0:
            print("\n🙏 Reflexionando sobre tus actos...")
            self.arrepentimiento += 20
            self.dignidad += 10
        else:
            print("\n🤔 Aún te sientes cómodo, la reflexión no es profunda.")
        time.sleep(1)

def simulador():
    print("========================================")
    print("   SIMULADOR AVANZADO: EL HIJO PRÓDIGO  ")
    print("========================================\n")
    
    nombre_usuario = input("Introduce tu nombre: ")
    personaje = HijoProdigo(nombre_usuario)
    
    ciclos = 0
    while personaje.dinero >= 0 and personaje.vivo:
        personaje.mostrar_estado()
        print(f"📅 Ciclo: {ciclos} | 'Sigues viviendo lejos de casa...'")
        
        print("\n¿Qué deseas hacer?")
        print("1. Gastarlo todo en fiestas")
        print("2. Invertir capital")
        print("3. Trabajar")
        print("4. Reflexionar")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            personaje.gastar_todo()
        elif opcion == "2":
            personaje.invertir()
        elif opcion == "3":
            personaje.trabajar()
        elif opcion == "4":
            personaje.reflexionar()
        else:
            print("Opción no válida.")

        # Lógica de desgaste por ciclo
        personaje.dinero -= 10
        personaje.hambre += 5
        ciclos += 1

        if personaje.dinero <= 0:
            print("\n⚠️ Te has quedado sin dinero.")
            break
        
        if personaje.arrepentimiento >= 100:
            print(f"\n✨ {personaje.nombre} ha decidido volver a casa del Padre. ¡Final Redentor!")
            break

    print("\n--- SIMULACIÓN FINALIZADA ---")

if __name__ == "__main__":
    simulador()