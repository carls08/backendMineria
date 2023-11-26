
from flask_cors import cross_origin
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from config import Connecction

class prediccionModel:
    @classmethod
    def model_prediccion_prediction(cls,data):
        with open('shopping_trends_updated.csv','r') as file:
            edad=data["edad"]
            localizacion=data["localizacion"]
            talla=data["talla"]
            color=data["color"]
            temporada=data["temporada"]
            des_aplicado=data["des_aplicado"]
            cd_promo_usado=data["cd_promo_usado"]
            compra_previa=data["compra_previa"]
            metodo_pago=data["metodo_pago"]
            frecuencia_compra=data["frecuencia_compra"]
            
            #Se importa la data
            
            datos=pd.read_csv(file)
            # se  crea la variable para utilizar la libreria de encoder para reemplazar los valores string a int
            
            label_encoder_localizacion=LabelEncoder()
            label_encoder_size=LabelEncoder()
            label_encoder_color=LabelEncoder()
            label_encoder_temporada=LabelEncoder()
            label_encoder_descuento=LabelEncoder()
            label_encoder_promo=LabelEncoder()
            label_encoder_pago=LabelEncoder()
            label_encoder_previa=LabelEncoder()
            label_encoder_frecuencia=LabelEncoder()
            
            datos['Location'] = label_encoder_localizacion.fit_transform(datos['Location'])
            datos['Size'] = label_encoder_size.fit_transform(datos['Size'])
            datos['Color'] = label_encoder_color.fit_transform(datos['Color'])
            datos['Season'] = label_encoder_temporada.fit_transform(datos['Season'])
            datos['Discount Applied'] = label_encoder_descuento.fit_transform(datos['Discount Applied'])
            datos['Promo Code Used'] = label_encoder_promo.fit_transform(datos['Promo Code Used'])
            datos['Previous Purchases'] = label_encoder_previa.fit_transform(datos['Previous Purchases'])
            datos['Payment Method'] = label_encoder_pago.fit_transform(datos['Payment Method'])
            datos['Frequency of Purchases'] = label_encoder_frecuencia.fit_transform(datos['Frequency of Purchases'])
            
            #se convierte a matriz
            X=datos[['Age','Location','Size','Color','Season','Discount Applied','Promo Code Used','Previous Purchases','Payment Method','Frequency of Purchases']]
            Y=datos['Gender']
            X=preprocessing.StandardScaler().fit(X).transform(X.astype(float))
            
            #Se entrenan los datos
            x_entre, x_test, y_entre,y_test =train_test_split(X,Y, test_size=0.2, random_state=4)

            
            #Se empieza con KNN 4
            k=4
            veci=KNeighborsClassifier(n_neighbors=k).fit(x_entre,y_entre)
            #Se predice con los datos de testeo
            y_predict=veci.predict([[edad,localizacion,talla,color,temporada,des_aplicado,cd_promo_usado,compra_previa,metodo_pago,frecuencia_compra]])
            pred_score=metrics.accuracy_score(y_entre,veci.predict(x_entre))
            #Aquí se evalua el modelo con la metrica de  Indice de jaccard
            try:
                conexion= Connecction.getConnection() 
                with conexion.cursor() as cursor:
                    
                    l=str(label_encoder_localizacion.inverse_transform([localizacion])[0])
                    t=str(label_encoder_size.inverse_transform([talla])[0])
                    c=str(label_encoder_color.inverse_transform([color])[0])
                    tp=str(label_encoder_temporada.inverse_transform([temporada])[0])
                    da=str(label_encoder_descuento.inverse_transform([des_aplicado])[0])
                    pu=str(label_encoder_promo.inverse_transform([cd_promo_usado])[0])
                    cp=str(label_encoder_previa.inverse_transform([compra_previa])[0])
                    mp=str(label_encoder_pago.inverse_transform([metodo_pago])[0])
                    f=str(label_encoder_frecuencia.inverse_transform([frecuencia_compra])[0])
                    sql="INSERT INTO predicciones(edad, localizacion, talla, color, temporada, des_aplicado, cd_promo_usado, compra_previa, metodo_pago, frecuencia_compra, prediccion) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql,(edad,l,t,c,tp,da,pu,cp,mp,f,str(y_predict[0])))
                    conexion.commit()
                    return y_predict[0]
            except Exception as ex: 
                print(ex)
                return False
                        
        