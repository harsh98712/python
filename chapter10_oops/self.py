class employee:
    language = "javascript"
    salary = "250000"
    
    
    def getInfo(self):
      print(f"the language is {self.language}.the salary is {self.salary} ")
    
    @staticmethod
    def greet(self):
     print("good morning")
         

harsh = employee()
# harsh.language = "python"


# print(harsh.language,harsh.salary)

harsh.getInfo()
harsh.greet()




