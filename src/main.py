from rammerhead import RammerheadProxy

def start_proxy():
    config = {
        'PROXY_HOST': 'localhost',
        'PROXY_PORT': 8080,
    }
    rammerhead = RammerheadProxy(config)
    rammerhead.start()

if __name__ == "__main__":
    start_proxy()
