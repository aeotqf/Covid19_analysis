
"""
Analisis lineal de casos de Covid primeros 20 dias Pais: X

Observe la diferencia de modelar un crecimiento exponencial con una funcion lineal

Created on Mon Jun 22 18:09:51 2020

@author: Ellis

documentacion:https://pyqtgraph.readthedocs.io/en/latest/
"""


#importamos lo necesario de Pyqt5
from PyQt5 import QtWidgets, QtCore

#es necesario instalar el paquete asi: conda install pyqtgraph
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  
import os

class MainWindow(QtWidgets.QMainWindow):
    
    
        #args y kwargs se usa para pertmitr pasar varios argumentos a la funcion
        #args especificamente se usa para permitir argumentos posicion
        #kwargs funciona igual que args pero para argumentos de de keywords o argumentos nombrados
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        #use los valores de su df, al menos los primeros 20 dias    
        fecha = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        positivos = [2,2,3,3,6,8,9,12,24,26,27,30,36,52,68,95,110,139,141,172]

        #Color de fondo a blanco
        self.graphWidget.setBackground('w')
        #Agregamos el titulo
        self.graphWidget.setTitle("Grafica lineal de casos positivos de Covid19 Pais X", color="b", size="30pt")
        #Agregamos las etiquetas de los ejes
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Positivos", **styles)
        self.graphWidget.setLabel("bottom", "Fecha", **styles)
        #Se agrega una leyenda
        self.graphWidget.addLegend()
        #Se agrega el fondo de matriz de la ventana
        self.graphWidget.showGrid(x=True, y=True)
        #Se establece el rango de los ejes
        self.graphWidget.setXRange(0, 20, padding=0)
        self.graphWidget.setYRange(0, 200, padding=0)
        #se define el lapiz con su color
        pen = pg.mkPen(color=(255, 0, 0))
        self.graphWidget.plot(fecha, positivos, name="Sensor 1",  pen=pen, symbol='+', symbolSize=30, symbolBrush=('b'))

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()