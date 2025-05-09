# model/skin_cancer_cnn.py

import torch.nn as nn
import torch.nn.functional as F

class SkinCancerCNN(nn.Module):
    def __init__(self, num_classes=9):
        super(SkinCancerCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)  # Output: (32, 180, 180)
        self.pool = nn.MaxPool2d(2, 2)                           # Down: /2 each time
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1) # Output: (64, 90, 90)
        self.dropout = nn.Dropout(0.25)
        self.fc1 = nn.Linear(64 * 45 * 45, 128)  # Flattened shape
        self.fc2 = nn.Linear(128, num_classes)   # Output: 9 class logits

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))     # -> (32, 90, 90)
        x = self.pool(F.relu(self.conv2(x)))     # -> (64, 45, 45)
        x = x.view(-1, 64 * 45 * 45)             # Flatten
        x = self.dropout(x)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
