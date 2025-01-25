class Dog:
  def _init_(self,name,age):
    self.name=name
    self.age=age

  def info(self):
    print("I am {} and I am {} years old".format(self.name,self.age))

  def make_sound(self):
    print("I bark at strangers")

class Cat:
  def _init_(self,name,age):
    self.name=name
    self.age=age

  def info(self):
    print("I am {} and I am {} years old".format(self.name,self.age))

  def make_sound(self):
    print("I make sound meow when i need milk")

d1=Dog("Corto",6)
c1=Cat("Mickey",9)

for animal in(d1,c1):
  animal.info()
  animal.make_sound()
