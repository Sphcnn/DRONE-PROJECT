class Drone:
    def _init_(self):
        # Pervanelerin hızları (1, 2, 3, 4 numaralı pervaneler)
        self.motors = [0, 0, 0, 0]  # Hızlar başlangıçta 0
        self.altitude = 0           # İrtifa
        self.yaw = 0                # Yön (derece)

    def _update_motors(self):
        """Pervane hızlarını yazdır."""
        print(f"Pervane hızları: {self.motors}")

    def take_off(self, height):
        """Kalkış: Tüm motor hızlarını eşit şekilde artır."""
        self.motors = [500, 500, 500, 500]
        self.altitude = height
        print(f"Drone kalktı. İrtifa: {self.altitude} metre")
        self._update_motors()

    def land(self):
        """İniş: Tüm motor hızlarını sıfıra indir."""
        self.motors = [0, 0, 0, 0]
        self.altitude = 0
        print("Drone yere indi.")
        self._update_motors()

    def rotate(self, angle):
        """Dönüş (Yaw): Karşılıklı motor hızlarını farklılaştır."""
        if angle > 0:  # Saat yönünde dön
            self.motors = [520, 480, 520, 480]
        elif angle < 0:  # Saat yönünün tersine dön
            self.motors = [480, 520, 480, 520]
        self.yaw = (self.yaw + angle) % 360
        print(f"Drone yönü değiştirildi. Yeni yön: {self.yaw} derece")
        self._update_motors()

    def move_forward(self, distance):
        """İleri hareket: Ön motor hızlarını azalt, arka motorları artır."""
        self.motors = [450, 450, 550, 550]
        print(f"Drone ileri hareket etti. Mesafe: {distance} metre")
        self._update_motors()

    def move_backward(self, distance):
        """Geri hareket: Arka motor hızlarını azalt, ön motorları artır."""
        self.motors = [550, 550, 450, 450]
        print(f"Drone geri hareket etti. Mesafe: {distance} metre")
        self._update_motors()

    def move_right(self, distance):
        """Sağa hareket: Sağ motor hızlarını azalt, sol motorları artır."""
        self.motors = [450, 550, 450, 550]
        print(f"Drone sağa hareket etti. Mesafe: {distance} metre")
        self._update_motors()

    def move_left(self, distance):
        """Sola hareket: Sol motor hızlarını azalt, sağ motorları artır."""
        self.motors = [550, 450, 550, 450]
        print(f"Drone sola hareket etti. Mesafe: {distance} metre")
        self._update_motors()

# Kullanım
drone = Drone()

drone.take_off(10)      # Kalkış
drone.move_forward(5)   # İleri git
drone.move_right(3)     # Sağa git
drone.rotate(90)        # 90 derece döndür
drone.move_backward(2)  # Geri git
drone.land()            # İniş