# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_capacity, storage_capacity):
        # Constructor to initialize attributes
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity  # in mAh
        self.storage_capacity = storage_capacity  # in GB
        self.battery_level = 100  # Battery level starts at 100%

    def turn_on(self):
        print(f"{self.brand} {self.model} is now ON.")

    def make_call(self, phone_number):
        print(f"Making a call to {phone_number}...")

    def check_battery(self):
        print(f"Battery Level: {self.battery_level}%")

    def charge(self, charge_amount):
        self.battery_level = min(self.battery_level + charge_amount, 100)  # Ensure battery doesn't exceed 100%
        print(f"Charging... Battery Level: {self.battery_level}%")

# Derived class: SmartphoneWithCamera (inherits from Smartphone)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_capacity, storage_capacity, camera_resolution):
        super().__init__(brand, model, battery_capacity, storage_capacity)
        self.camera_resolution = camera_resolution  # in MP

    def take_picture(self):
        print(f"Taking a picture with {self.camera_resolution}MP camera...")

    def record_video(self):
        print(f"Recording video with {self.camera_resolution}MP camera...")

# Create an object of Smartphone
phone = Smartphone("Samsung", "Galaxy S21", 4000, 128)
phone.turn_on()
phone.make_call("123-456-7890")
phone.check_battery()
phone.charge(20)

# Create an object of SmartphoneWithCamera
camera_phone = SmartphoneWithCamera("Apple", "iPhone 13 Pro", 4000, 256, 12)
camera_phone.turn_on()
camera_phone.take_picture()
camera_phone.record_video()
camera_phone.check_battery()
