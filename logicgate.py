#!/usr/bin/python


#logic gate to represent python class in heritance

#logic gate is my super class. The gates are going to be categorized by the number on inputs they contain
#then dilineiated further by sublcasses of each kind of input.
class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None
    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        print self.output
#this is our double input gate
class BinaryGate(LogicGate):
    
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A for gate " + self.getLabel() + "---->")
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return input("Enter Pin B for gate " + self.getLabel() + "---->")
        else:
            return self.pinB.getFrom().getOutput()
    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print "Cannot Connect: NO EMPTY PINS"

#a sublcass of the binarygate is the and class. this will implement the peroformGateLogic()
class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        else:
            return 1
        

#this class is for the unary gate
class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPinA(self):
        return input("Enter Pin A for Gate" + self.getLabel() + "---->")

    def setNextPin(self,source):
        print source
        if self.pin == None:
            self.pin = source
        else:
            print "Cannot Connect: No EMPTY Pins"
class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)
    def performGateLogic(self):
        a = self.getPinA()
        if a == 1:
            return 0
        else:
            return 1


class Connector:
    def __init__(self,fgate,tgate):
        self.fromgate = fgate
        self.togate = tgate
        

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate
    def getTo(self):
        return self.togate

    





gate = AndGate('Jons And Gate')
#gate.getOutput()

orgate = OrGate('Jons Or Gate')
#orgate.getOutput()

notgate = NotGate('Not Gate')
#notgate.getOutput()


c1 = Connector(notgate,orgate)
c2 = Connector(notgate,orgate)
c3 = Connector(orgate,notgate)

notgate.getOutput()
