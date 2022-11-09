import pymysql
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
import sys 
import requests


class Pantalla ( QtWidgets.QWidget):
        

    def __init__(self):
        super().__init__()
        self.crear_widgets()
        self.conectar()
        self.actualizar_clima()
    
        
    def crear_widgets(self):
        self.label = QtWidgets.QLabel("")
        self.label.setText("Favoritos")
        self.font = self.label.font()
        self.font.setPointSize(20)
        self.label.setFont(self.font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.tabla = QtWidgets.QTableWidget(8,8)
        self.label_titulo_datos = QtWidgets.QLabel('')
        self.respuesta_ciudad =QtWidgets.QLabel("")
        self.respuesta_temperatura =QtWidgets.QLabel("")
        self.respuesta_temperatura_minima =QtWidgets.QLabel("")
        self.respuesta_temperatura_maxima =QtWidgets.QLabel("")
        self.respuesta_presion =QtWidgets.QLabel("")
        self.respuesta_humedad =QtWidgets.QLabel("")
        self.respuesta_visibilidad =QtWidgets.QLabel("")
        self.respuesta_descripcion =QtWidgets.QLabel("")
        self.guardar = QtWidgets.QPushButton('ver favoritos ')
        self.buscar = QtWidgets.QPushButton('actualizar datos')
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        
        self.__cuadricula = QtWidgets.QGridLayout()
        self.__cuadricula.addWidget(self.label,0,0)
        self.__cuadricula.addWidget(self.label_titulo_datos,1,0)
        
        self.__cuadricula.addWidget(self.tabla,4,1)
        self.__capa = QtWidgets.QVBoxLayout()
        self.__capa.addLayout(self.__cuadricula)
        self.setLayout(self.__capa)
        
    def conectar(self):
        
        self.guardar.clicked.connect(self.Guardar_datos)
        self.buscar.clicked.connect(self.actualizar_clima)
        
    def Guardar_datos(self):
        
        self.conn = pymysql.connect(host='localhost',user='root',password='123456',db='db_tiempo') 
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM tiempo")
        self.info = self.c.fetchall()
        
        f = len(self.info)  # No. de filas
        c = len(self.info[0])  # No. de columnas
        self.tabla.setRowCount(f)
        self.tabla.setColumnCount(c)

        for i in range(f):
            for j in range(c):
                self.tabla.setItem(i, j,QtWidgets.QTableWidgetItem(self.info[i][j]))
                        
        self.tabla.move(1, 1)

        
    def actualizar_clima(self):
        
        self.listanueva =[]
        self.conn = pymysql.connect(host='localhost',user='root',password='123456',db='db_tiempo') 
        self.c = self.conn.cursor()
        self.c.execute("SELECT ciudad FROM tiempo")
        self.info = self.c.fetchall()
      
        for self.ciudad in self.info:
            
           
            
            
            self.ciudad = self.ciudad
            self.API_key = "12d0ab8a83b2d0cf3806baebb9dcbb8c"
            self.URL = "https://api.openweathermap.org/data/2.5/weather"
            self.parametros = {"APPID":self.API_key,"q":self.ciudad,"units":"metric",'lang':'es'}
       
            self.response = requests.get(self.URL, params = self.parametros)
            self.clima = self.response.json()
            self.ciudad_elegida = self.clima['name']
            self.respuesta_ciudad.setText(self.ciudad_elegida)
            self.clima_temperatura = str(int(self.clima['main']['temp'])) + 'c°'
            self.respuesta_temperatura.setText(self.clima_temperatura)
            self.clima_temp_min = str(int(self.clima['main']['temp_min'])) + 'c°'
            self.respuesta_temperatura_minima.setText(self.clima_temp_min)
            self.clima_temp_max = str(int(self.clima['main']['temp_max'])) + 'c°'
            self.respuesta_temperatura_maxima.setText(self.clima_temp_max)
            self.clima_presion = str(int(self.clima['main']['pressure'])) + 'hPA'
            self.respuesta_presion.setText(self.clima_presion)
            self.clima_humedad = str(int(self.clima['main']['humidity'])) + '%'
            self.respuesta_humedad.setText(self.clima_humedad)
            self.clima_visibilidad = str(int(self.clima['visibility'])) + 'Km'
            self.respuesta_visibilidad.setText(self.clima_visibilidad)
            self.clima_descripcion = self.clima['weather'][0]['description']
            self.respuesta_descripcion.setText(self.clima_descripcion)
            self.tupla =self.ciudad_elegida,self.clima_temperatura,self.clima_temp_min,self.clima_temp_max,self.clima_presion,self.clima_humedad,self.clima_visibilidad,self.clima_descripcion
            self.listanueva.append(self.tupla)
       
        f = len(self.listanueva)  # No. de filas
        c = len(self.listanueva[0])  # No. de columnas
        self.tabla.setRowCount(f)
        self.tabla.setColumnCount(c)

        for i in range(f):
            
            for j in range(c):
                self.tabla.setItem(i, j,QtWidgets.QTableWidgetItem(self.listanueva[i][j]))
                    
                self.tabla.move(1, 1)   
                    
                    
            
        
    
