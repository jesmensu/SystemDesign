class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    class Builder:
        def __init__(self, name):
            self.name = name
            self.age = None
            self.email = None

        def set_age(self, age):
            self.age = age
            return self

        def set_email(self, email):
            self.email = email
            return self

        def build(self):
            return User(self.name, self.age, self.email)

# Usage example:
user = User.Builder("Rohit Verma").set_email("rohit@learnyard.com").build()
print(user.age)
print(type(user))

print(user.name, user.age, user.email)
