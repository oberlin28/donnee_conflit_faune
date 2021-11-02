import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import folium
from folium import plugins
from streamlit_folium import folium_static 
from folium.plugins import MarkerCluster
#from folium import FeatureGroup
from folium.plugins import MeasureControl
from folium.plugins import MousePosition
from folium.plugins import Search
from folium.plugins import HeatMap
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



		st.sidebar.header('CONTROLEUR DE DONNEES')

		st.sidebar.markdown("""---""")
		
		st.sidebar.subheader('CHOISIR LA VUE A AFFICHER')		
		menu = ["Données", "Diagramme", "Carte"]
		choix = st.sidebar.selectbox("Données * Diagramme * Carte", menu)



		df = pd.read_excel(io='conflit_faune.xlsx',
							                    sheet_name='DATA',
							                    usecols='A:I',
							                    header=1)

				
		if choix == "Données":

							st.sidebar.subheader('REQUÊTE OU RECHERCHE')
							
							col1, col2, col_droite = st.columns([0.1,1.8, 0.1])
							#col1.image("minef.png", width=80)
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
									    options=df["conflit"].unique())
									    #default="HOMME-ELEPHANTS"
									

							localite = st.sidebar.multiselect(
									    "Choisir localité:",
									    options=df["localite"].unique())
									    #default="ABIDJAN"
									

							annee = st.sidebar.multiselect(
									    "Choisir année:",
									    options=df["annee"].unique())
									    #default=2021
									
							df_selection = df.query("conflit == @conflit & localite == @localite & annee == @annee")
							
							st.markdown("""---""")
							st.subheader("Resultat de la recherche ci-dessous")
							st.dataframe(df_selection)
							st.sidebar.text(f'voir le resultat ci-dessous')
				
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
							conflit_selection = st.sidebar.multiselect('Type de conflit :', conflit_var, default='HOMME-ELEPHANT')

							
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

			menu_deuxieme = ["TOUS LES CONFLITS", "CARTE DE CHALEUR"]
			choix_deuxieme = st.sidebar.selectbox("Choisir type de carte", menu_deuxieme)

			if choix_deuxieme == "TOUS LES CONFLITS":
					#my_bar = st.progress(0)
					#for percent_complete in range(100):
						#time.sleep(0.05)
						#my_bar.progress(percent_complete + 1)

					#df1 = pd.read_csv("clean_data_sample.csv")
					#st.dataframe(df1)
					
					df = pd.read_excel(io='conflit_faune.xlsx',
									                    sheet_name='DATA',
									                    usecols='A:I',
									                    header=1)

					df_elephant = pd.DataFrame(df[df["conflit"] == "HOMME-ELEPHANT"])
					df_buffle = pd.DataFrame(df[df["conflit"] == "HOMME-BUFFLE"])
					df_chauvesouris = pd.DataFrame(df[df["conflit"] == "HOMME-CHAUVE-SOURIS"])
					df_chimpanze = pd.DataFrame(df[df["conflit"] == "HOMME-CHIMPANZE"])
					df_rhinoceros = pd.DataFrame(df[df["conflit"] == "HOMME-RHINOCEROS"])
					df_hippopotame = pd.DataFrame(df[df["conflit"] == "HOMME-HIPPOPOTAME"])
					df_leopard = pd.DataFrame(df[df["conflit"] == "HOMME-LEOPARD"])
					df_crocodile = pd.DataFrame(df[df["conflit"] == "HOMME-CROCODILE"])
					df_singe = pd.DataFrame(df[df["conflit"] == "HOMME-SINGE"])
					df_epervier = pd.DataFrame(df[df["conflit"] == "HOMME-EPERVIER"])

					#ip = df[["latitude", "longitude", "conflit"]]
					
					#op = df.set_index("latitude")#[("latitude", "conflit")]
					#st.dataframe(ip)
					#coord = pd.DataFrame(df)
					#st.dataframe(coord)
					#****fichier = pd.DataFrame(coord, columns=['latitude', 'longitude'])
					#*****st.map(fichier)

					# VARIABLE POUR AFFICHER LA CARTE
					carte = folium.Map(location=[7.3056, -5.3888], zoom_start=7, control_scale=True,
										max_bounds=True, min_lat=4.05, max_lat=10.80, min_lon=-8.86, max_lon=-2.30) #prefer_canvas=True
					

					#OUTILS DESSINS
					draw = plugins.Draw(export=False)

					#POSITION DE LA SOURIS
					MousePosition(separator=' | ', prefix="Coordonnée lat I lon :").add_to(carte)



					#AJOUTE PLEIN ECRAN A LA CARTE
					plugins.Fullscreen(position='topleft').add_to(carte)

					
					draw.add_to(carte)
					#INSERER LES DONNEES LAT LONG DANS LA CARTE
					#for (index, row) in df.iterrows():
					#for (i, row) in df.iterrows():
						#lat = df.at[i, 'latitude']
						#lng = df.at[i, 'longitude']
						#info = df.at[i, 'conflit']

						#popup = '<b>'+'<br>'+ "INFORMATION" + '</br>'+'</b>' + '<b>'+'<br>'+ "Conflit : "+'</b>'+ df.at[i, 'conflit'] +
						#'<b>'+'<br>'+ "Localité : "+'</b>'+ df.at[i, 'localite'] +
						#'<b>'+'<br>'+ "Annee : "+'</b>'+ df.at[i, 'annee']
						#folium.Marker(location=[lat, lng], popup=)

					#CREATION D'UN CLUSTER
					markerCluster_elephant = MarkerCluster(name='Homme-Faune').add_to(carte)
					#markerCluster_buffle = MarkerCluster(name='homme-buffle').add_to(carte)
					#markerCluster_chauvesouris = MarkerCluster(name='homme-chauve-souris').add_to(carte)
					#markerCluster_chimpanze = MarkerCluster(name='homme-chimpanzé').add_to(carte)
					#markerCluster_rhinoceros = MarkerCluster(name='homme-Rhinoceros').add_to(carte)
					#markerCluster_hippopotame = MarkerCluster(name='homme-Hippopotame').add_to(carte)
					#markerCluster_leopard = MarkerCluster(name='homme-Léopard').add_to(carte)
					#markerCluster_crocodile = MarkerCluster(name='homme-Crocodile').add_to(carte)
					#markerCluster_singe = MarkerCluster(name='homme-Singe').add_to(carte)
					#markerCluster_epervier = MarkerCluster(name='homme-Epervier').add_to(carte)

					for (index, row) in df_elephant.iterrows():
						icon_elephant = folium.features.CustomIcon('./elephant2.png', icon_size=(30,30))
						folium.Marker(location=[row.loc["latitude"], row.loc["longitude"]],
							icon = icon_elephant,  
							popup = '<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["conflit"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["localite"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["annee"])+'</br>',
							tooltip="cliquer pour info").add_to(markerCluster_elephant)

					#BUFFLES UNIQUEMENT DANS LA CARTE
					#icon_buffle = folium.features.CustomIcon('Buffle.png', icon_size=(100,100))

					for (index, row) in df_buffle.iterrows():
						icon_buffle = folium.features.CustomIcon('./Buffle3.png', icon_size=(30,30))
						folium.Marker(location=[row.loc["latitude"], row.loc["longitude"]],
							icon = icon_buffle,  
							popup = '<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["conflit"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["localite"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["annee"])+'</br>',
							tooltip="cliquer pour info").add_to(markerCluster_elephant)


					#CHAUVE-SOURIS UNIQUEMENT DANS LA CARTE
					for (index, row) in df_chauvesouris.iterrows():
						icon_chauve = folium.features.CustomIcon('./chauve-souris2.png', icon_size=(30,30))
						folium.Marker(location=[row.loc["latitude"], row.loc["longitude"]],
							icon = icon_chauve,  
							popup = '<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["conflit"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["localite"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["annee"])+'</br>',
							tooltip="cliquer pour info").add_to(markerCluster_elephant)



					#CHIMPANZES UNIQUEMENT DANS LA CARTE
					for (index, row) in df_chimpanze.iterrows():
						icon_chimpanze = folium.features.CustomIcon('./chimpanzé2.png', icon_size=(30,30))
						folium.Marker(location=[row.loc["latitude"], row.loc["longitude"]],
							icon = icon_chimpanze,  
							popup = '<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["conflit"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["localite"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["annee"])+'</br>',
							tooltip="cliquer pour info").add_to(markerCluster_elephant)


					#rhinoceros UNIQUEMENT DANS LA CARTE
					for (index, row) in df_rhinoceros.iterrows():
						icon_rhino = folium.features.CustomIcon('./rhinoceros2.png', icon_size=(30,30))
						folium.Marker(location=[row.loc["latitude"], row.loc["longitude"]],
							icon = icon_rhino,  
							popup = '<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["conflit"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["localite"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["annee"])+'</br>',
							tooltip="cliquer pour info").add_to(markerCluster_elephant)


					#Hippopotame UNIQUEMENT DANS LA CARTE
					for (index, row) in df_hippopotame.iterrows():
						icon_hippo = folium.features.CustomIcon('./hippopotamus2.png', icon_size=(30,30))
						folium.Marker(location=[row.loc["latitude"], row.loc["longitude"]],
							icon = icon_hippo,  
							popup = '<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["conflit"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["localite"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["annee"])+'</br>',
							tooltip="cliquer pour info").add_to(markerCluster_elephant)


					#Leopard UNIQUEMENT DANS LA CARTE
					for (index, row) in df_leopard.iterrows():
						icon_leopard = folium.features.CustomIcon('./leopard2.png', icon_size=(30,30))
						folium.Marker(location=[row.loc["latitude"], row.loc["longitude"]],
							icon = icon_leopard,  
							popup = '<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["conflit"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["localite"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["annee"])+'</br>',
							tooltip="cliquer pour info").add_to(markerCluster_elephant)


					#crocodile UNIQUEMENT DANS LA CARTE
					for (index, row) in df_crocodile.iterrows():
						icon_crocodile = folium.features.CustomIcon('./crocodile2.png', icon_size=(30,30))
						folium.Marker(location=[row.loc["latitude"], row.loc["longitude"]],
							icon = icon_crocodile,  
							popup = '<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["conflit"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["localite"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["annee"])+'</br>',
							tooltip="cliquer pour info").add_to(markerCluster_elephant)


					#singe UNIQUEMENT DANS LA CARTE
					for (index, row) in df_singe.iterrows():
						icon_singe = folium.features.CustomIcon('./singe2.png', icon_size=(30,30))
						folium.Marker(location=[row.loc["latitude"], row.loc["longitude"]],
							icon = icon_singe,  
							popup = '<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["conflit"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["localite"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["annee"])+'</br>',
							tooltip="cliquer pour info").add_to(markerCluster_elephant)



					#epervier UNIQUEMENT DANS LA CARTE
					for (index, row) in df_epervier.iterrows():
						icon_epervier = folium.features.CustomIcon('./epervier2.png', icon_size=(30,30))
						folium.Marker(location=[row.loc["latitude"], row.loc["longitude"]],
							icon = icon_epervier,  
							popup = '<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["conflit"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["localite"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["annee"])+'</br>',
							tooltip="cliquer pour info").add_to(markerCluster_elephant)


					# Add hover functionality.
					highlight_function = lambda x: {'fillColor': '#000000', 
					                                'color':'#000000', 
					                                'fillOpacity': 0.50, 
					                                'weight': 0.1}


        			#groupe_entite = FeatureGroup(name="Aire protégée")

					#AJOUT DE FICHIER DE FORME AU FORMAT GEOJSON
					fc = folium.features.GeoJson('foret_classee.geojson', name='Forêt Classée', highlight_function = highlight_function, 
						tooltip=folium.features.GeoJsonTooltip(fields=['nom','sup'], aliases=['Nom FC :','Superficie (ha) :'], 
						style=("background-color: white; color: #333333; font-family:arial; font-size: 12px; padding: 10px;")), 
						popup=folium.features.GeoJsonPopup(fields=["nom"]+["sup"], aliases=['Nom FC :','Superficie (ha) :']), 
						style_function=lambda x:{'fillColor': '#228B22', 'color': '#228B22', 'fillOpacity':0.1, 'weight':1}).add_to(carte)

					#folium.map.CustomPane("nom").add_to()

					# Recherche de données dans la carte
					fcsearch = Search(
					    layer=fc,
					    geom_type="Polygon",
					    placeholder="Recherche Forêt Classée",
					    collapsed=True,
					    search_label="nom",
					    weight=2
					).add_to(carte)
					
					ap = folium.features.GeoJson('aire_protegee.geojson', name='Aire Protégée', popup=folium.features.GeoJsonPopup(fields=["Nom"]+["Surface"], aliases=['Nom AP :','Superficie (ha) :']), 
						highlight_function = highlight_function, tooltip=folium.features.GeoJsonTooltip(fields=['Nom','Surface'],aliases=['Nom AP : ','Superficie (ha) : '], 
						style=("background-color: white; color: #333333; font-family:arial; font-size: 12px; padding: 10px;")),
						style_function=lambda x:{'fillColor': '#3498DB', 'color': '#3498DB', 'fillOpacity':0.1, 'weight':1}).add_to(carte)

					# Recherche de données dans la carte
					fcsearch = Search(
					    layer=ap,
					    geom_type="Polygon",
					    placeholder="Recherche Aire-protégée",
					    collapsed=True,
					    search_label="Nom",
					    weight=2
					).add_to(carte)

					#groupe_entite.add_to(carte)

					# add tiles to map
					#folium.raster_layers.TileLayer('Open Street Map', name="OSM").add_to(carte)
					folium.raster_layers.TileLayer(tiles="http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", subdomains=["mt0", "mt1", "mt2", "mt3"], 
													attr="google", name="google maps", control=True).add_to(carte)

					#folium.raster_layers.WmsTileLayer(
					#    url="http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi",
					#    name="test",
					#    fmt="image/png",
					#    layers="nexrad-n0r-900913",
					#    attr="Weather data © 2012 IEM Nexrad",
					#    transparent=True,
					#    overlay=True,
					#    control=True,
					#).add_to(carte)

					#folium.raster_layers.TileLayer(tiles="http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi", subdomains=["mt0", "mt1", "mt2", "mt3"], 
													#attr="Weather data © 2012 IEM Nexrad", name="Weather", control=True).add_to(carte)

					folium.raster_layers.TileLayer('Stamen Terrain', name="Topographie").add_to(carte)

					#Ajouter mini-carte
					mini_carte = plugins.MiniMap(toggle_display=True)
					carte.add_child(mini_carte)
					
					#Ajouter Zoom dans la mini-carte
					#plugins.ScrollZoomToggler().add_to(carte)


					# add layer control to show different maps
					folium.LayerControl().add_to(carte) 

					#MESURE SUR LA CARTE
					carte.add_child(MeasureControl(position='topright', primary_area_unit='hectares', secondary_area_unit='sqmeters', primary_length_unit='kilometers', secondary_length_unit='meters',))
					
					# AFFICHER LA CARTE DANS STREAMLIT
					folium_static(carte, width=1070, height=700)

			if choix_deuxieme == "CARTE DE CHALEUR":

					carte = folium.Map(location=[7.3056, -5.3888], zoom_start=7, control_scale=True) 
					
					df = pd.read_excel(io='conflit_faune.xlsx',
									                    sheet_name='DATA',
									                    usecols='A:I',
									                    header=1)
					
					#st.dataframe(data=df, height=700)

					#df['latitude'] = df['latitude'].astype(float)
					#df['longitude'] = df['longitude'].astype(float)

					#df = df[['latitude', 'longitude']]
					#df = df.dropna(axis=0, subset=['latitude','longitude'])

					#CARTE DE CHALEUR
					heat_data = [[row.loc['latitude'], row.loc['longitude']] for index, row in df.iterrows()]

					HeatMap(heat_data, name="Carte de chaleur").add_to(carte)


					#AJOUTE PLEIN ECRAN A LA CARTE
					plugins.Fullscreen(position='topleft').add_to(carte)

					#AJOUTE OUTILS DE DESSINS A LA CARTE
					draw = plugins.Draw(export=False)
					draw.add_to(carte)

					#AJOUT DE FICHIER DE FORME AU FORMAT GEOJSON
					# Add hover functionality.
					highlight_function = lambda x: {'fillColor': '#000000', 
					                                'color':'#000000', 
					                                'fillOpacity': 0.50, 
					                                'weight': 0.1}


        

					#AJOUT DE FICHIER DE FORME AU FORMAT GEOJSON
					folium.features.GeoJson('foret_classee.geojson', name='Forêt Classée', highlight_function = highlight_function, 
						tooltip=folium.features.GeoJsonTooltip(fields=['nom','sup'], aliases=['Nom FC :','Superficie (ha) :'], 
						style=("background-color: white; color: #333333; font-family:arial; font-size: 12px; padding: 10px;")), 
						popup=folium.features.GeoJsonPopup(fields=["nom"]+["sup"], aliases=['Nom FC :','Superficie (ha) :']), 
						style_function=lambda x:{'fillColor': '#228B22', 'color': '#228B22', 'fillOpacity':0.1, 'weight':1}).add_to(carte)
					
					folium.features.GeoJson('aire_protegee.geojson', name='Aire Protégée', popup=folium.features.GeoJsonPopup(fields=["Nom"]+["Surface"], aliases=['Nom AP :','Superficie (ha) :']), 
						highlight_function = highlight_function, tooltip=folium.features.GeoJsonTooltip(fields=['Nom','Surface'],aliases=['Nom AP : ','Superficie (ha) : '], 
						style=("background-color: white; color: #333333; font-family:arial; font-size: 12px; padding: 10px;")),
						style_function=lambda x:{'fillColor': '#3498DB', 'color': '#3498DB', 'fillOpacity':0.1, 'weight':1}).add_to(carte)


					# add tiles to map
					folium.raster_layers.TileLayer('Open Street Map').add_to(carte)
					folium.raster_layers.TileLayer('Stamen Terrain').add_to(carte)
					#folium.raster_layers.TileLayer('Stamen Toner').add_to(carte)
					#folium.raster_layers.TileLayer('Stamen Watercolor').add_to(carte)
					#folium.raster_layers.TileLayer('CartoDB Positron').add_to(carte)
					#folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(carte)

					#Ajouter mini-carte
					mini_carte = plugins.MiniMap(toggle_display=True)
					carte.add_child(mini_carte)
					
					#Ajouter Zoom dans la mini-carte
					#plugins.ScrollZoomToggler().add_to(carte)

					#AJOUTE PLEIN ECRAN A LA CARTE
					#plugins.Fullscreen(position='topleft').add_to(carte)

					# add layer control to show different maps
					folium.LayerControl().add_to(carte)

					# AFFICHER LA CARTE DANS STREAMLIT
					folium_static(carte, width=1070, height=700)

					#plugins.Fullscreen(position='topleft').add_to(carte)
					
    		
			



if __name__ == '__main__':
    main()