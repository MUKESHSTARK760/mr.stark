""" import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}
print(mydataset)
myvar = pd.DataFrame(mydataset)
print(myvar) """

# NumPy is a Python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.


""" import numpy
arr = numpy.array([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr)
print(arr[1])
print(arr[2] + arr[3])
print(arr[1:5]) 
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[1:10:2])  """

""" import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([0,3,5])
ypoints = np.array([0,150,45])
plt.plot(xpoints, ypoints)
plt.show()  """

""" 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
np.random.seed(42)
x = np.random.rand(50) * 10
y = 2 * x + 1 + np.random.randn(50) * 2
slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept
plt.scatter(x, y, label='Data')
plt.plot(x, y_pred, color='red', label=f'Regression Line: y = {slope:.2f}x + {intercept:.2f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show() """

""" 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QAction, QMenuBar, QDialog


class SecondWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Window")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()
        label = QLabel("This is the second window", self)
        layout.addWidget(label)
        self.setLayout(layout)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Example")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel("Hello, PyQt!", self)
        self.layout.addWidget(self.label)

        self.button = QPushButton("Click Me", self)
        self.layout.addWidget(self.button)
        

        self.init_menu()

    def init_menu(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        view_menu = menubar.addMenu("View")
        second_window_action = QAction("Open Second Window", self)
        second_window_action.triggered.connect(self.open_second_window)
        view_menu.addAction(second_window_action)

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.exec_()

   
        

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_()) """ 

# bs4
#This will not run on online IDE
""" import requests
from bs4 import BeautifulSoup

URL = "http://www.livewireindia.com"
r = requests.get(URL)

soup = BeautifulSoup(r.content) # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.title) """
