from nodes.operations import Plus
from nodes.basic import Value

def main():
    p1 = Plus()
    p2 = Plus()
    p3 = Plus(p1,p2)
    print(p3)

if __name__ == "__main__":
    main()