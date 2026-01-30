class Dog:
<<<<<<< HEAD
    def __init__(self, name, age):
=======
    def __init__(self, namne, age):
>>>>>>> 1ec9508a48c8b0393e775d36f4e72a263446fbb8
      self.name = name
      self.age = age
    
    def info(self):
        print(f"{self.name}is{self.age} yeras old") 
        
def main():
    my_dog = Dog("Buddy", 3)
    your_dog = Dog ("paulie", 2)
   
    print(my_dog)


if __name__ == "__main__":
    main()
