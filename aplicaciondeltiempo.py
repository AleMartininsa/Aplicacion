import pymysql
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
import sys 
import requests
from moduloaplicacion import Pantalla
from qt_material import apply_stylesheet
from PIL import Image

class PantallaPrincipal(QtWidgets.QWidget):
        

    def __init__(self):
        super().__init__()
        self.crear_widgets()
        self.conectar()
        
        
        
    def crear_widgets(self):
        self.label = QtWidgets.QLabel("")
        self.label.setText("Aplicacion del Tiempo")
        self.font = self.label.font()
        self.font.setPointSize(20)
        self.label.setFont(self.font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        
        self.label_ingreso_ciudad = QtWidgets.QLabel('Ingrese la Ciudad:')
        self.ingreso_ciudad =QtWidgets.QLineEdit()
        self.label_ciudad = QtWidgets.QLabel('Ciudad:')
        self.label_temperatura = QtWidgets.QLabel('Temperatura:')
        self.temperatura = QtWidgets.QLineEdit()
        self.label_temperatura_minima= QtWidgets.QLabel('Temperatura Minima:')
        self.temperatura_minima = QtWidgets.QLineEdit()
        self.label_temperatura_maxima = QtWidgets.QLabel('Temperatura Maxima:')
        self.temperatura_maxima = QtWidgets.QLineEdit()
        self.label_presion = QtWidgets.QLabel('Presion:')
        self.presion = QtWidgets.QLineEdit()
        self.label_Humedad = QtWidgets.QLabel('Humedad:')
        self.humedad = QtWidgets.QLineEdit()
        self.label_visibilidad = QtWidgets.QLabel('Visibilidad:')
        self.visibilidad = QtWidgets.QLineEdit()
        self.label_descripcion = QtWidgets.QLabel('Tiempo Actual:')
        
        self.respuesta_ciudad =QtWidgets.QLabel("")
        self.respuesta_temperatura =QtWidgets.QLabel("")
        self.respuesta_temperatura_minima =QtWidgets.QLabel("")
        self.respuesta_temperatura_maxima =QtWidgets.QLabel("")
        self.respuesta_presion =QtWidgets.QLabel("")
        self.respuesta_humedad =QtWidgets.QLabel("")
        self.respuesta_visibilidad =QtWidgets.QLabel("")
        self.respuesta_descripcion =QtWidgets.QLabel("")
        
        self.buscar = QtWidgets.QPushButton('Obtener')
        self.favoritos = QtWidgets.QPushButton('Favoritos')
        self.borrar = QtWidgets.QPushButton('Borrar')
        
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                                                                         
        self.__cuadricula = QtWidgets.QGridLayout()
        self.__cuadricula.addWidget(self.label,0,0)
        self.__cuadricula.addWidget(self.label_ingreso_ciudad,1,0)
        self.__cuadricula.addWidget(self.ingreso_ciudad,1,1)
        
        self.__cuadricula.addWidget(self.buscar,1,2)
        self.__cuadricula.addWidget(self.favoritos,1,3)
        self.__cuadricula.addWidget(self.borrar,1,4)
        
        self.__cuadricula.addWidget(self.label_ciudad,4,0)
        self.__cuadricula.addWidget(self.label_temperatura,5,0)
        self.__cuadricula.addWidget(self.label_temperatura_minima,6,0)
        self.__cuadricula.addWidget(self.label_temperatura_maxima,7,0)
        self.__cuadricula.addWidget(self.label_presion,8,0)
        self.__cuadricula.addWidget(self.label_Humedad,9,0)
        self.__cuadricula.addWidget(self.label_visibilidad,10,0)
        self.__cuadricula.addWidget(self.label_descripcion,11,0)
        
        self.__cuadricula.addWidget(self.respuesta_ciudad,4,1)
        self.__cuadricula.addWidget(self.respuesta_temperatura,5,1)
        self.__cuadricula.addWidget(self.respuesta_temperatura_minima,6,1)
        self.__cuadricula.addWidget(self.respuesta_temperatura_maxima,7,1)
        self.__cuadricula.addWidget(self.respuesta_presion,8,1)
        self.__cuadricula.addWidget(self.respuesta_humedad,9,1)
        self.__cuadricula.addWidget(self.respuesta_visibilidad,10,1)
        self.__cuadricula.addWidget(self.respuesta_descripcion,11,1)
        
        self.__capa = QtWidgets.QVBoxLayout()
        self.__capa.addLayout(self.__cuadricula)
        self.setLayout(self.__capa)
        
        self.ciudad_solicitada = 'victoria'
        self.API_key = "12d0ab8a83b2d0cf3806baebb9dcbb8c"
        self.URL = "https://api.openweathermap.org/data/2.5/find"
        self.parametros = {"APPID":self.API_key,'q':self.ciudad_solicitada,'lang':'es'}
        self.response = requests.get(self.URL, params = self.parametros)
        self.clima = self.response.json()
        
        self.list=['carcaraña','Roldan']
        self.names =self.clima['list'][0]['name']
        self.a=self.clima['list'][0]['sys']['country']
        self.names1 =self.clima['list'][1]['name']
        self.b=self.clima['list'][1]['sys']['country']
        self.names2 =self.clima['list'][2]['name']
        self.c=self.clima['list'][2]['sys']['country']
        self.names3 =self.clima['list'][3]['name']
        self.d=self.clima['list'][3]['sys']['country']
        self.names4 =self.clima['list'][4]['name']
        self.e=self.clima['list'][4]['sys']['country']
        self.list.append(self.names + ',' + self.a)
        self.list.append(self.names1 + ',' + self.b)
        self.list.append(self.names2 + ',' + self.c)
        self.list.append(self.names3 + ',' + self.d)
        self.list.append(self.names4 + ',' + self.e)
        
        self.ciudad_solicitada = 'funes'
        self.API_key = "12d0ab8a83b2d0cf3806baebb9dcbb8c"
        self.URL = "https://api.openweathermap.org/data/2.5/find"
        self.parametros = {"APPID":self.API_key,'q':self.ciudad_solicitada,'lang':'es'}
        self.response = requests.get(self.URL, params = self.parametros)
        self.clima = self.response.json()
        
        self.names =self.clima['list'][0]['name']
        self.a=self.clima['list'][0]['sys']['country']
        self.names1 =self.clima['list'][1]['name']
        self.b=self.clima['list'][1]['sys']['country']
        self.names2 =self.clima['list'][2]['name']
        self.c=self.clima['list'][2]['sys']['country']
        self.names3 =self.clima['list'][3]['name']
        self.d=self.clima['list'][3]['sys']['country']
        
        self.list.append(self.names + ',' + self.a)
        self.list.append(self.names1 + ',' + self.b)
        self.list.append(self.names2 + ',' + self.c)
        self.list.append(self.names3 + ',' + self.d)
      
        
        self.ciudad_solicitada = 'rosario'
        self.API_key = "12d0ab8a83b2d0cf3806baebb9dcbb8c"
        self.URL = "https://api.openweathermap.org/data/2.5/find"
        self.parametros = {"APPID":self.API_key,'q':self.ciudad_solicitada,'lang':'es'}
       
        self.response = requests.get(self.URL, params = self.parametros)
        self.clima = self.response.json()
        self.names =self.clima['list'][0]['name']
        self.a=self.clima['list'][0]['sys']['country']
        self.names1 =self.clima['list'][1]['name']
        self.b=self.clima['list'][1]['sys']['country']
        self.names2 =self.clima['list'][2]['name']
        self.c=self.clima['list'][2]['sys']['country']
      
        
        self.list.append(self.names + ',' + self.a)
        self.list.append(self.names1 + ',' + self.b)
        self.list.append(self.names2 + ',' + self.c)
        self.completer = QtWidgets.QCompleter(self.list)
        self.ingreso_ciudad.setCompleter(self.completer) 
        
    def conectar(self):
        self.buscar.clicked.connect(self.Localizar_ciudad)
        self.borrar.clicked.connect(self.borrar_datos)
        self.favoritos.clicked.connect(self.abrir_app_Modulo)
    
    def abrir_app_Modulo(self):
        
        self.conexion = pymysql.connect(host='localhost',user='root',password='123456',db='db_tiempo') 
        self.cursor = self.conexion.cursor()
        self.sql ="INSERT INTO tiempo(ciudad,temperatura,temp_min,temp_max,presion,humedad,visibilidad,descripcion) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(self.ciudad_elegida,self.clima_temperatura,self.clima_temp_min,self.clima_temp_max,self.clima_presion,self.clima_humedad,self.clima_visibilidad,self.clima_descripcion)
        self.cursor.execute(self.sql)
        self.conexion.commit()
        self.abrir_pantalla = Pantalla()
        self.abrir_pantalla.show()
    
    def Localizar_ciudad(self):
        
      
        self.ciudad = self.ingreso_ciudad.text()
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
        
        
        
    def borrar_datos(self):
        
        self.respuesta_ciudad.setText('')
        self.respuesta_temperatura.setText('')
        self.respuesta_temperatura_minima.setText('')
        self.respuesta_temperatura_maxima.setText('')
        self.respuesta_presion.setText('')
        self.respuesta_humedad.setText('')
        self.respuesta_visibilidad.setText('')
        self.ingreso_ciudad.setText('')
        self.respuesta_descripcion.setText('')
    



miAplicacion = QtWidgets.QApplication(sys.argv)
pantalla = PantallaPrincipal()
pantalla.show()
apply_stylesheet(miAplicacion,theme='dark_blue.xml')
miAplicacion.exec_()
sys.exit(0)
         
        
        
        
        
        