# Enheritence versus composition


# Implicit Inheritance

# class Parent(object):
#
#     def implicit(self):
#         print("PARENT implicit()")
#
# class Child(Parent):
#
#     pass
#
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()

# Override Explicity

# class Parent(object):
#
#     def override(self):
#         print("PARENT override()")
#
# class Child(Parent):
#
#     def override(self):
#         print("CHILD override()")
#
# dad = Parent()
# son = Child()
#
# dad.override()
# son.override()

# Alter Befor and After

# class Parent(object):
#
#     def altered(self):
#         print("Parent altered()")
#
# class Child(Parent):
#
#     def altered(self):
#         # override the function altered from the parent
#         # before alter to the parent's altered function
#         print("CHILD, BEFORE PARENT altered()")
#         # using super syntax to get the parent's altered function
#         # and calling it
#         # the two parameter Child and self is the same if you
#         # type super()
#         super(Child, self).altered()
#         # overried it again
#         print("CHILD, AFTER PARENT altered()")
#
# dad = Parent()
# son = Child()
#
# dad.altered()
# son.altered()

# All three combined
#
# class Parent(object):
#
#     def override(self):
#         print("PARENT override()")
#
#     def implicit(self):
#         print("PARENT implicit()")
#
#     def altered(self):
#         print("PARENT altered()")
#
# class Child(Parent):
#
#     def override(self):
#         print("CHILD override()")
#
#     def altered(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()")
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()
#
# dad.override()
# son.override()
#
# dad.altered()
# son.altered()

# Using super() with __init__

class Parent(object):

    def __init__(self, asping, asbun):
        self.asping = asping
        self.asbun = asbun

    def tell(self):
        print(f"asping is {self.asping}")

class Child(Parent):

    def __init__(self, name):
        super(Child, self).__init__(name,name)

son = Child("hasan")

print(son.asping)

print(son.asbun)

son.tell()


# composition

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


a
