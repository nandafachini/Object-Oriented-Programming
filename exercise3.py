# Implement the Television class.

# ------------------------
# | Television           |
# ------------------------
# | channel              |
# | volume               |
# ------------------------
# turn_up_volume()       |
# turn_down_volume()     |
# change_channel(channel)|
# ------------------------

# Write a program to create an object of the Television class and test your class.


class Television:
    def __init__(self):
        self.channel = None
        self.volume = 0
   
    def turn_up_volume(self):
        self.volume = self.volume +1
        return self.volume

    def turn_down_volume(self):
        self.volume = self.volume - 1
        return self.volume

    def change_channel(self,channel):
        self.channel = channel
        return self.channel

tv = Television()
tv.turn_up_volume()
tv.turn_up_volume()
tv.turn_up_volume()
tv.turn_down_volume()
tv.change_channel(5)
print(f'The tv is on the channel {tv.channel}')
print(f'The tv is on volume {tv.volume}')
