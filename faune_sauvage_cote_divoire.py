import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import folium
#from streamlit_folium import folium_static 
from PIL import Image
import openpyxl as xl
import time
from pathlib import Path 
import base64

def main():
		
		st.set_page_config(page_title='App.Conflits-DFRC/MINEF', 
									 layout="wide",
								     initial_sidebar_state="expanded",
								     page_icon='minef.png')


		#@st.cache

		st.sidebar.header('CONTROLEUR DE DONNEES')

		st.sidebar.markdown("""---""")
		st.sidebar.subheader('FILTRE DES DONNEES')
				
		menu = ["Données", "Diagramme", "Carte"]
		choix = st.sidebar.selectbox("CHOISIR LA VUE A AFFICHER", menu)

				
		if choix == "Données":

							st.sidebar.subheader('REQUÊTE OU RECHERCHE')
							
							col1, col2, col_droite = st.columns([0.1,1.8, 0.1])
							col2.header("APP.CONFLITS : Gestion des données Conflits Homme-Faune")
							col2.markdown("""Cette Application est une version bêta en cours de dévéloppement. Elle présente les données
								des differents conflits homme-faune de 2011 à Juillet 2021 dans tout le pays.
								""")
							
							col2.markdown("""
								* ** Source de données: Directions Régionales des Eaux et Forêts.**
								* ** Traitement de données: Service Cartographique Direction de la Faune et des Ressources Cynégétiques (DFRC)**
								""")

							st.markdown("""---""")
							st.subheader("Typologie des conflits")
							
							
							col3, col4, col5, col6, col7 = st.columns(5)
							with col3 :
								st.image("elephant.png", use_column_width=False, width=80, caption = 'Eléphant')
							
							with col4 :
								st.image("Buffle.png", use_column_width=False, width=80, caption = 'Buffle')

							with col5 :	
								st.image("chimpanzé.png", use_column_width=False, width=50, caption = 'Chimpanzé')
							
							with col6 :
								st.image("rhinoceros.png", use_column_width=False, width=80, caption = 'Rhinoceros')
							
							with col7 :
								st.image("hippopotamus.png", use_column_width=False, width=100, caption = 'Hippopotame')

							col8, col9, col10, col11, col12 = st.columns(5)
							col8.image("leopard.png", use_column_width=False, width=80, caption = 'Léopard')
							col9.image("crocodile.png", use_column_width=False, width=130, caption = 'Crocrodile')
							col10.image("singe.png", use_column_width=False, width=70, caption = 'Singe')
							col11.image("chauve-souris.png", use_column_width=False, width=130, caption = 'Chauve-souris')
							col12.image("epervier.png", use_column_width=False, width=80, caption = 'Epervier')


							st.markdown("""---""")
							st.subheader("Données des Conflits Homme-Faune de 2011 à Juillet 2021")

							


							### --- BARRE LATERALE
							## st.sidebar.header('CONTROLEUR DE DONNEES')
							## selection_annee = st.sidebar.selectbox('Année de conflit', list(reversed(range(2011,2022))))

							### --- CHARGER DONNEES EXCEL ET LES METTRE DANS UN DATAFRAME

							df = pd.read_excel(io='conflit_faune.xlsx',
							                    sheet_name='DATA',
							                    usecols='A:I',
							                    header=1)
							st.dataframe(data=df, height=700)
				

							st.download_button(label='Telecharger données', data='df', file_name='donnees_CHF' )

							
							
							#REQUETE SUR LE TABLEUR

							#df_statistique = pd.read_excel(
												#io='conflit_faune.xlsx',
							                    #sheet_name='DATA',
							                    #usecols='K:O',
							                    #header=1)

							conflit = st.sidebar.multiselect("Choisir conflit:",
									    options=df["conflit"].unique(),
									    #default="HOMME-ELEPHANTS"
									)

							localite = st.sidebar.multiselect(
									    "Choisir localité:",
									    options=df["localite"].unique(),
									    #default="ABIDJAN"
									)

							annee = st.sidebar.multiselect(
									    "Choisir année:",
									    options=df["annee"].unique(),
									    #default=2021
									)
							df_selection = df.query("conflit == @conflit & localite == @localite & annee == @annee")
							st.sidebar.dataframe(df_selection)
				
		elif choix == "Diagramme":

							df = pd.read_excel(io='conflit_faune.xlsx',
							                    sheet_name='DATA',
							                    usecols='A:I',
							                    header=1)
							#st.dataframe(data=df, height=600)
							#st.download_button(label='Telecharger données', data='conflit_faune.xlsx', file_name='donnees_CHF.xlsx')

							st.subheader("Rprésentation graphique des données")
							st.markdown("""---""")

							#CREATION DE COLONNE POUR DISPOSITION ELEMENTS  
							left_column, right_column = st.columns(2)
							#st.subheader('Effectif total par type de conflits')
							pie_chart_complet = pd.DataFrame(df['conflit'].value_counts())					
							left_column.markdown('__Effectif total par conflits__')
							left_column.bar_chart(pie_chart_complet, use_container_width=True)

							
							posi1, posi2 = st.columns(2)
							voir = df.groupby("conflit")["Blesses"].sum()
							posi1.markdown('__Effectif des blèssés par conflit__')
							posi1.bar_chart(voir)

							voir2 = df.groupby("conflit")["Morts"].sum()
							posi2.markdown('__Effectif des morts par conflit__')
							posi2.bar_chart(voir2)

							#voir3 = df["conflit", "annee"]("HOMME-ELEPHANTS")
							#st.dataframe(voir3)




							#st.subheader('Nombre de conflit par année')
							annee_diagramme = pd.DataFrame(df['annee'].value_counts())
							right_column.markdown('__Nombre de conflit par année__')
							right_column.bar_chart(annee_diagramme, use_container_width=True)


				
							
							#AJOUTE BARRE LATERALE
							

							#AJOUT DES DONNEES DU FILTRE
							annee_var = df['annee'].unique().tolist()
							annee_selection = st.sidebar.multiselect('Annee de conflit :', annee_var, default=2020)

							conflit_var = df['conflit'].unique().tolist()
							conflit_selection = st.sidebar.multiselect('Type de conflit :', conflit_var, default='HOMME-ELEPHANTS')

							
							## FILTRE DE DONNEES PAR CONFLIT

							mask = (df['annee'].isin(annee_selection)) & (df['conflit'].isin(conflit_selection))
							number_of_result = df[mask].shape[0]
							st.sidebar.markdown(f'*Resultat disponible:{number_of_result}*')

							## GROUPER BLOC DE DONNEES APRES SELECTION
							df_grouper = df[mask].groupby(by=['conflit']).count()[['annee']]
							df_grouper = df_grouper.rename(columns = {'annee':'Effectif'})
							df_grouper = df_grouper.reset_index()

							
							## AFFICHE LE DIAGRAMME DU FILTRE 
							st.markdown("__Diagramme en Bande des données filtrées__")
							graphique = px.bar(df_grouper,
												x='conflit',
												y='Effectif',
												text='Effectif')
							st.plotly_chart(graphique)


		elif choix == "Carte":
			
			df = pd.read_excel(io='conflit_faune.xlsx',
							                    sheet_name='DATA',
							                    usecols='A:I',
							                    header=1)

			
			#ip = df[["latitude", "longitude", "conflit"]]
			
			#op = df.set_index("latitude")#[("latitude", "conflit")]
			#st.dataframe(ip)
			coord = pd.DataFrame(df)
			#st.dataframe(coord)
			fichier = pd.DataFrame(coord, columns=['latitude', 'longitude'])
			st.map(fichier)



if __name__ == '__main__':
    main()