import services
from gui.gui import launch_gui


if __name__ == "__main__":
    
    services.config.load_config()
    launch_gui()
