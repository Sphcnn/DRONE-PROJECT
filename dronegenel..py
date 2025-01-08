import dronesimulator
import dronemechanic

print("Lütfen bir seçim yapın:")
print("1 - Manuel Kontrol")
print("2 - Simülasyon (Varsayılan)")

def manual_mode():
    """Manuel kontrol modu."""
    print("Manuel kontrol moduna geçiliyor...")
    drone = dronemechanic.Drone()  # Drone sınıfını burada kullanıyoruz
    # Burada manuel kontrol fonksiyonlarını çağırabilirsiniz
    drone.take_off(100)  # Manuel modda 100 metreye kalkış
    drone.rotate(90)
    drone.land()
    drone.move_forward()
    drone.move_backward()
    drone.move_right()
    drone.move_left()


def simulation_mode():
    """Simülasyon modu."""
    print("Simülasyon moduna geçiliyor...")
    # Simülasyon kodunu buraya ekleyin
    # Örneğin:
    simulation = dronesimulator.Simulation('connection_string')  # Simülasyon sınıfını doğru şekilde kullanıyoruz
    simulation.kalkış(100)  # Simülasyon için 100 metreye kalkış fonksiyonu
    simulation.add_mission()
    simulation.execute_mission()

choice = input("Seçiminizi girin (1/2): ").strip()

if choice == "1":
    manual_mode()  # Manuel kontrol moduna geç
else:
    simulation_mode()  # Varsayılan simülasyon modu çalışır