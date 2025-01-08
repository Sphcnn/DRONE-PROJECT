from dronekit import connect, VehicleMode, LocationGlobalRelative, Command
from pymavlink import mavutil
import time

class Simulation:
    def _init_(self, connection_string):
        """
        Simülasyon sınıfı başlatılır ve drone bağlantısı kurulur.
        """
        self.iha = connect(connection_string, wait_ready=True)

    def kalkış(self, irtifa):
        """
        Kalkış işlemleri.
        """
        while self.iha.is_armable is not True:
            print("İHA arm edilebilir durumda değil.")
            time.sleep(1)
        
        print('İHA arm edilebilir')
        self.iha.mode = VehicleMode("GUIDED")#otomatik guide moduna geçicek. Çünkü guide modunda olmazas uçuş başlamıyor.
        time.sleep(1)
        
        print(str(self.iha.mode) + " moduna alındı")

        self.iha.armed = True

        while self.iha.armed is not True:
            print("İHA arm ediliyor...")
            time.sleep(0.5)
        print("İHA arm edildi")

        self.iha.simple_takeoff(irtifa)
        while self.iha.location.global_relative_frame.alt < irtifa * 0.9:
            print("İHA hedefe yükseliyor")
            time.sleep(1)
        print("İHA belirtilen irtifaya ulaştı.")

    def add_mission(self):
        """
        Görev ekleme işlemleri.
        """
        global komut
        komut = self.iha.commands
        komut.clear()
        time.sleep(1)

        # TAKEOFF KOMUTU
        komut.add(Command(
            0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
            mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 0
        ))
        #BURADA BİR SÜRÜ PARAMETRE VAR
        #target_system verdiğimiz değerin önemi yok çünkü dronekit bunu kendi MAVLİNK ID ile ayarlayacak
        #target_component bu prmtre drone değill herhangi bir alt sisteme görev verir cam,mic,gun,etc.
        #seq görev sıralaması için kullanılır buna sıfır versek bile dronekit kendi ayarlıyor
        #frame (x,y,z) kordinatlarının neye göre referans alınacağını belirler. mavutil.mavlinkMAV_FRAME_GLOBAL_RELATIVE_ALT bu komut kalkış noktasından itibaren sıfır almasını sağlıyor
        #**takeoff prmtresi drone gönderdiğimiz komutun ne olduğunu tanımlayan prmtre
        #bundan sonraki  ikisi desteklenmediği için 0 yazmalıyız
        #bu ikisinden sonra 7 tane daha parametre var 6 tanesi kullanılmnadığı için 0 yazacağız sonuncusuna istediğimiz değeri gireceğiz.
        #sonuncusuna da dronun çıkmasını  istediğimiz irtifayı yazıyoruz


        # WAYPOINT KOMUTU
        komut.add(Command(
            0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
            mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 153153, 453254, 20
        ))

        # İKİNCİ WAYPOINT KOMUTU(HEDEF KONUM)
        komut.add(Command(
            0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
            mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 8485424, 44658, 20
        ))
        #Bunun ilk parametresi gittiği yerde kalnasını istediğimiz süreyi(delay) belirleyecek
        #prm2,3,4 0 olacak kullanılmıyor
        #prm5,6,7 droneun gitmesini istediğimiz konumu gireceğimiz yerler.
        #prm5= enlem prm6=boylam prm7= yükseklik
        #Bu komut sayesinde drone bir konuma 20 metrelik irtifadan gidecek sonra diğer konua gidecek oradan da RTL komutu çalıştırdğımız zaman başlangıç noktasına dönecek.
#RTL

        # RTL (Return to Launch) KOMUTU
        komut.add(Command(
            0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
            mavutil.mavlink.MAV_CMD_NAV_RTL, 0, 0, 0, 0, 0, 0, 0, 0
        ))
        #RTL hiçbir parametre almadığı için son 7 parametrenin hepsi 0 olacak
        #Bu parametrelere ve komutlaraardupılot stl nin sitesinden ulaşabiliriz ve istediğimiz komutu verebiliriz
        
        
        komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                          mavutil.mavlink.MAV_CMD_NAV_RTL,0,0,0,0,0,0,0,0
                          ))
        #DOĞRULAMA BU KOMUT DRONE ZATEN İNİŞ YAPMIŞ OLACAĞI İÇİN HİÇBİR İŞE YARAMAYACAK SADECE GÖREVİN BİTİP BİTMEDİĞİNİ SORGULAYACAĞIMIZ İF İÇİN VAR OLACAK

        komut.upload()
        print("Komutlar yükleniyor...")

    def execute_mission(self):
        """
        Görevleri yürütür.
        """
        komut.next = 0   #karışıklığı önlemek için en baştan başlasın diye

        self.iha.mode = VehicleMode("AUTO") #AUTO modunda olmazsa verdiğimiz hazır komutları anlamıyor. Biz GUIDED da kullanıyorduk aslında ama o manuel sistem için kullanılor.


        while True:
            next_waypoint = komut.next
            print(f"Sıradaki komut: {next_waypoint}")
            time.sleep(1)

            if next_waypoint == 4:
                print("Görev başarıyla tamamlandı.")
                break

        print("Döngüden çıkıldı.")