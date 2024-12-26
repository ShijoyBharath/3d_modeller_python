def main():
    print("Running Scene...")

class Viewer(object):
    def __init__(self):
        '''Initialize viewer'''
        self.init_interface()
        self.init_opengl()
        self.init_scene()
        self.init_interaction()
        init_primitives()

    def init_interface(self):
        '''Initialize window and register render function'''
        glutInit()

if __name__ == "__main__":
    main()