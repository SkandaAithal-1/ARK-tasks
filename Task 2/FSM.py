class Machine:
    def __init__(self)->None:
        self.states={}
        self.Trans={}
        self.trans=None
        self.currState=None
    def setState(self,toState,code=None):
        self.currState=self.states[toState]
    def transition(self, toState):
        self.trans=self.Trans[toState]
        self.setState(toState)
        self.trans.Execute()
    def Execute(self,code=None):
        if code:
            self.currState.Execute(code)
        else:
            self.currState.Execute()
            
        
class transition():
    def __init__(self, toState):
        self.toState=toState
    def Execute(self):
        print("Transitioning to ", self.toState)
        
class EnterCode:
    def Execute(self):
        print(Items.allItems)
        #print(Items.Itemdict)
        self.code=input("Please Enter the Code :")
        if self.code not in Items.Itemdict:
            print("Entered Item not present. Please choose another item.")
            self.Execute()
        else:
            print("Thank You for choosing the item")
        Items.vend(self.code)
        
class EnterMoney:
    def Execute(self, code):
        self.code=code
        self.money=int(input("Enter the input amount :"))
        self.change=(self.money - Items.Itemdict[self.code][0])
        if self.change==0 :
            print("No change to return")
        elif self.change<0 :
            print("Amount not enough!!!")
            self.Execute(self.code)
        else:
            print("Change = ", self.change)

class Items(Machine):
    allItems=[]
    Itemdict={}
    def __init__(self, No : int, Drink : str, Code : str, Cost : int, Quantity=50)->None:
        self.Sl_No = No
        self.Drink = Drink
        self.Code = Code
        self.Cost = Cost
        self.Quantity = Quantity
        Items.allItems.append(self)
        Items.Itemdict[self.Code] = [self.Cost, self.Quantity]
        super().__init__()

    @staticmethod
    def vend(code)->None:
        count=0
        for i in Items.Itemdict:
            count+=(Items.Itemdict[i][1])
        if (count==0):
            a=input("Please type REFILL")
            if (a=="REFILL"):
                for i in Items.Itemdict:
                    Items.Itemdict[i][1]=50
                return None
        if (Items.Itemdict[code][1]):
            Items.Itemdict[code][1]-=1
        else:
            print("Please Choose another item")
        

    def __repr__(self):
        return f'("{self.Sl_No}","{self.Drink}","{self.Code}","{self.Code}","{self.Cost}")\n'

def main():
    MyFSM=Machine()
    item1=Items(1,"Pepsi","PEPS",30)
    item2=Items(2,"Mountain Dew","MDEW",30)
    item3=Items(3,"Dr. Pepper","DPEP",50)
    item4=Items(4,"Coke","COKE",20)
    item5=Items(5,"Gatorade","GATO",20)
    item6=Items(6,"Diet Coke","DCOK",30)
    item7=Items(7,"Minute Maid","MINM",25)
    item8=Items(8,"Tropicana","TROP",30)
    MyFSM.states["EnterCode"]=EnterCode()
    MyFSM.states["EnterMoney"]=EnterMoney()
    MyFSM.Trans["EnterCode"]=transition("EnterCode")
    MyFSM.Trans["EnterMoney"]=transition("EnterMoney")
    MyFSM.setState("EnterCode")
    MyFSM.Execute()
        
    while (True):
        code=MyFSM.currState.code
        MyFSM.transition("EnterMoney")
        MyFSM.Execute(code)
        MyFSM.transition("EnterCode")
        MyFSM.Execute()

if (__name__ == "__main__"):
    main()
