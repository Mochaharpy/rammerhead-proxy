from config import Configuration
from rammerhead import RammerheadProxy

def main():
    config = Configuration()
    rammerhead = RammerheadProxy(config.get_rammerhead_config())
    rammerhead.start()

if __name__ == "__main__":
    main()
