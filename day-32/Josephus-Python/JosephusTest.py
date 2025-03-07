
from Solution import Josephus, DoublyCircularLL

def main():
    game = Josephus()
    
    # Provided test cases
    print("Test Case: size=5, rotation=2 | Survivor:", game.josephusDCLL(5, 2))
    print("Test Case: size=7, rotation=2 | Survivor:", game.josephusDCLL(7, 2))
    print("Test Case: size=8, rotation=2 | Survivor:", game.josephusDCLL(8, 2))
    print("Test Case: size=13, rotation=2 | Survivor:", game.josephusDCLL(13, 2))
    
    # Additional test cases
    print("Test Case: size=1, rotation=1 | Survivor:", game.josephusDCLL(1, 1))
    print("Test Case: size=10, rotation=3 | Survivor:", game.josephusDCLL(10, 3))
    print("Test Case: size=10, rotation=1 | Survivor:", game.josephusDCLL(10, 1))
    print("Test Case: size=15, rotation=4 | Survivor:", game.josephusDCLL(15, 4))
    # Fun test cases
    print("Test Case: size=10, rotation=11 | Survivor: ", game.josephusDCLL(10, 11));
    print("Test Case: size=20, rotation=21 | Survivor: ", game.josephusDCLL(20, 21));
    print("Test Case: size=30, rotation=31 | Survivor: ", game.josephusDCLL(30, 31));
    print("Test Case: size=15, rotation=25 | Survivor: ", game.josephusDCLL(15, 25));
    print("Test Case: size=15, rotation=15 | Survivor: ", game.josephusDCLL(15, 15));

main()
