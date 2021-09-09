import json
import pickle
import torch
import torch.optim
import torch.nn as nn
from torch.utils.data import DataLoader

import preprocess
import model

data_file = open('intents.json').read()
intents = json.loads(data_file)

words, classes, documents = preprocess.create(intents)

#saving words and classes
pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

#dataloaders
patterns, intents, training_dataset = preprocess.get_tensor_dataset(words, classes, documents)
training_loader = DataLoader(training_dataset, batch_size = 5, shuffle = True)


net = model.Sequential(len(patterns[0]), len(intents[0]))

epochs = 200
# define the optimizer - SGD
optimizer = torch.optim.SGD(net.parameters(), lr=0.01, weight_decay=1e-6, momentum=0.9, nesterov=True)
# define the loss function
criterion = nn.CrossEntropyLoss()

for epoch in range(epochs):
    running_loss = 0.0
    for i, (patterns, intents) in enumerate(training_loader):
            optimizer.zero_grad()
            yhat = net.forward(patterns)
            loss = criterion(yhat, torch.max(intents, 1)[1])
            loss.backward()
            optimizer.step()
            
    running_loss += loss.item()
    if epoch % 50 == 49:    
            print('Epoch [%d]  loss: %.3f' %
                  (epoch + 1, running_loss / 50))
            running_loss = 0.0
    
net.eval()
torch.save(net, 'chatbot_model.pt')

print("model created")