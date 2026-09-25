from Info.Pynox_class import Pynox  #type: ignore
from Boot.bootloader import Bootloader  #type: ignore
from Boot.Boot import BootManager #type: ignore


def main():
    system = Pynox()

    print("================================")
    print(f"{system.name} OS")
    print(f"Version {system.version}")
    print("================================")

    bootloader = Bootloader()
    bootloader.load()

    boot = BootManager()
    boot.start()

    print("================================")
    print("Pynox is ready.")
    print("================================")


if __name__ == "__main__":
    main()
