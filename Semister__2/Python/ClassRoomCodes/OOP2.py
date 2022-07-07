class vehicle:
    def get(self,type,color):
        self.color = color
        self.type = type
    def put(self):
        print(self.color)
        print(self.type)
        
Vehicle1 = vehicle()
Vehicle1.get("Car","Red")
Vehicle1.put()
