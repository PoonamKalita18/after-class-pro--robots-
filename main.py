class robot :
    name = 'Sophia'
    feature = 'ai-oriented'

def introduction(self):
    print('This is a humanoid robot')

def details(self):
    print('Hey! This is ', self.name , 'the humanoid robot')
    print('I am a ', feature , 'robot')

ob = robot()
ob.introduction()
ob.details()