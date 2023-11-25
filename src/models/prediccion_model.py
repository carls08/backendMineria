
from flask_cors import cross_origin
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

class prediccionModel:
    @classmethod
    def model_prediccion_prediction(cls,data):
        with open('shopping_trends_updated.csv','r') as file: 
        #Se importa la data
            print(data)
            datos=pd.read_csv(file)
            # se  crea la variable para utilizar la libreria de encoder para reemplazar los valores string a int
            label_encoder=LabelEncoder()
            datos['Gender'] = label_encoder.fit_transform(datos['Gender'])
            datos['Item Purchased'] = label_encoder.fit_transform(datos['Item Purchased'])
            datos['Category'] = label_encoder.fit_transform(datos['Category'])
            datos['Location'] = label_encoder.fit_transform(datos['Location'])
            datos['Size'] = label_encoder.fit_transform(datos['Size'])
            datos['Color'] = label_encoder.fit_transform(datos['Color'])
            datos['Season'] = label_encoder.fit_transform(datos['Season'])
            datos['Subscription Status'] = label_encoder.fit_transform(datos['Subscription Status'])
            datos['Shipping Type'] = label_encoder.fit_transform(datos['Shipping Type'])
            datos['Discount Applied'] = label_encoder.fit_transform(datos['Discount Applied'])
            datos['Promo Code Used'] = label_encoder.fit_transform(datos['Promo Code Used'])
            datos['Payment Method'] = label_encoder.fit_transform(datos['Payment Method'])
            datos['Frequency of Purchases'] = label_encoder.fit_transform(datos['Frequency of Purchases'])
            
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
            y_predict=veci.predict([[data['edad'],data['localizacion'],data['talla'],data['color'],data['temporada'],data['des_aplicado'],data['cd_promo_usado'],data['compra_previa'],data['metodo_pago'],data['frecuencia_compra']]])
            pred_score=metrics.accuracy_score(y_entre,veci.predict(x_entre))
            #Aquí se evalua el modelo con la metrica de  Indice de jaccard
           
            
        return y_predict[0]