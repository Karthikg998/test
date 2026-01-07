class Device:
    brand="noise"
    model="s400"
class Connectivity:
    def connect_bluetooth(self):
        print("connected to bluetooth ")
    def connect_wifi(self):
        print("connected to wifi ")
class Smart_watch(Device,Connectivity):
    def tracking_steps(self):
        print("tracking steps")
    def display_time(self):
        print("display time")
watch = Smart_watch()
print(watch.brand,watch.model)
watch.connect_bluetooth()
watch.connect_wifi()
watch.tracking_steps()
watch.display_time()

