import torch.nn as nn

class Sequential(nn.Module):

    def __init__(self, n_inputs, n_outputs, drop_prob=0.5):
        
        #Calling constructor of parent class
        super().__init__()
        
        #Input layer
        self.hid1 = nn.Linear(n_inputs, 128) 
        nn.init.kaiming_uniform_(self.hid1.weight, nonlinearity='relu')
        self.act1 = nn.ReLU()
        self.dropout = nn.Dropout(drop_prob)
        
        #Hidden layer
        self.hid2 = nn.Linear(128, 64)
        nn.init.kaiming_uniform_(self.hid2.weight, nonlinearity='relu')
        self.act2 = nn.ReLU()
        self.dropout = nn.Dropout(drop_prob)
        
        #Output layer
        self.hid3 = nn.Linear(64, n_outputs)
        nn.init.xavier_uniform_(self.hid3.weight)
        self.act3 = nn.Softmax(dim=1)

    def forward(self, X):
        
        #input and act for layer 1
        X = self.hid1(X)
        X = self.act1(X)
        
        #dropout
        X = self.dropout(X)
        
        #input and act for layer 2
        X = self.hid2(X)
        X = self.act2(X)
        
        #dropout
        X = self.dropout(X)
         
        #input and act for layer 3
        X = self.hid3(X)
        X = self.act3(X)
        
        return X
    