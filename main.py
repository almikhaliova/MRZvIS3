from hopfield_network import *

if __name__ == '__main__':
    manager = TemplatesManager()
    patterns = manager.pattern
    print("--------------MENU-------------")
    print("1) Image 1\n2) Image 2\n")
    menu = input("Enter number: ")

    if menu == '1':
        print("\n----------Noisy image-----------")
        giraffe = manager.giraffe
        Network.print(giraffe)
        print("\n----------Realization-----------")
        mine = Network(patterns)
        mine.learning(giraffe)

    elif menu == '2':
        print("\n----------Noisy image-----------")
        fox = manager.fox
        Network.print(fox)
        print("\n----------Realization-----------")
        mine = Network(patterns)
        mine.learningf(fox)