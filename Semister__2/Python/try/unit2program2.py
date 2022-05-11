#/bin/python


class person:
    PersonName = "Saurabh"
    PersonEmail = "abcd@example.com"
    PersonAccountNo = 202103103510362
    __PersonAadharNumber = 123456789123
    __PersonPanNumber = "ABCDE1234X"
    
    def put(self):
        print(self.PersonName)
        print(self.PersonEmail)
        print(self.PersonAccountNo)
        print(self.__PersonAadharNumber)
        print(self.__PersonPanNumber)
        
        
    
person1 = person()
person1.put()