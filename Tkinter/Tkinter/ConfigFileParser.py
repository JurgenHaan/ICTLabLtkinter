import configparser

class ConfigFileParser:
    def __str__(self):
        config = configparser.ConfigParser()

        config.read("RoomNumber.ini")
        roomNumber = config.get('DEFAULT','Room')
        return roomNumber

