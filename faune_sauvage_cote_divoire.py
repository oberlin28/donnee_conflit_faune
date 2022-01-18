import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import folium
from folium import plugins
from streamlit_folium import folium_static 
from folium.plugins import MarkerCluster
#from folium import FeatureGroup
from folium.plugins import MeasureControl
from folium.plugins import MousePosition
from folium.plugins import Search
from folium.plugins import HeatMap
import plotly.graph_objects as go
#from gsheetsdb import connect
from PIL import Image
import openpyxl as xl
import time
from pathlib import Path 
import base64
import pickle
import datetime 
#from sklearn.linear_model import LogisticRegression
#from sklearn.model_selection import train_test_split


st.set_page_config(page_title='App.Conflits-DFRC/MINEF', 
							 layout="wide",
						     initial_sidebar_state="expanded",
						     page_icon='minef.png')


def main():

		#img_1, img_2, img_3 = st.columns([0.1, 0.5, 0.1])
		st.sidebar.header('CONTROLEUR DE DONNEES')

		st.sidebar.markdown("""---""")
		
		st.sidebar.subheader('CHOISIR LA VUE A AFFICHER')		
		menu = ["Données 💾", "Tableau de bord 📈", "Cartographie 🌈"]
		choix = st.sidebar.selectbox("Données * Tableau de bord * Cartographie", menu)

		#option = st.selectbox('Please Select', ['POWERBI', 'ok'])
		#if option=='POWERBI':
			#st.markdown('https://app.powerbi.com/links/vkkaAgsrD6?ctid=eecc4b36-240a-4a05-b3bc-72718c4c513f&pbi_source=linkShare', unsafe_allow_html=True)

		
									
		#df_conflit = pd.read_excel(io='conflit_faune.xlsx',
							                    #sheet_name='DATA',
							                    #usecols='A:I',
							                    #header=1)

		#Create a connection object.
		#conn = connect()
		#def run_query(query):
		 #   rows = conn.execute(query, headers=1)
		 #   return rows
		#sheet_url = st.secrets["public_gsheets_url"]
		#rows = run_query(f'SELECT * FROM "{sheet_url}"')
		#data = rows.fetchall()
		#res = pd.DataFrame.from_dict(data) # Converting to dataframe
		#res = res.astype({"annee":int, "Morts":int, "Blesses":int, "Victimes":int})  # Now you can manipulate easily the DATFRAME
		#st.write(res)
		#rows['annee'] = rows['annee'].astype(int)
		#st.dataframe(rows, height=100)

		#for row in rows:
			#localites=[(row.localite, row.conflit)]
			#conflits=row.conflit
			#annees=int(row.annee)
			#mm=[(localites, conflits, annees)]
			#pp=pd.DataFrame(localites)
			#st.dataframe(localites, height=500)
			
			#op=(f"{row.localite} {row.conflit} {int(row.annee)}")
			#st.write(op)
   
		#mylist=['localite', 'conflit']
		#dg=pd.DataFrame(mylist)
		#print(dg)
			#st.dataframe(op)
		df_conflit = pd.read_excel(io='BD_conflitHommeFaune.xlsx',
                    sheet_name='DONNEES',
                    usecols='A:Q',
                    header=0,
                    converters={'Année':int,'Autres victimes culture et matériel':int, 'Mort':int, 'Blessé':int, "nombre d'animaux":int})
							                    #dtype={'Année': np.int32, 'Autres victimes culture et matériel': np.int32})
		
		#df_mort = pd.read_excel(io='BD_conflitHommeFaune.xlsx',
                    #sheet_name='STATISTIQUE_STREAMLIT',
                    #usecols='A:B',
                    #header=0,
                    #converters={'NombreMort':int})	


		df_blesses_mort_victime = pd.read_excel(io='BD_conflitHommeFaune.xlsx',
                    sheet_name='STATISTIQUE_STREAMLIT',
                    usecols='J:L',
                    header=0,
                    converters={'NombreBlessé':int})
		#st.write(df_blesses)

		date_jour = str(datetime.date.today())
		
		info_text_1_1=date_jour

		#ELEMENTS DU GRAPHIQUE DES CONFLITS
		elephant_graph = df_conflit[df_conflit['Typologie'] == 'HOMME-ELEPHANT']
		buffle_graph = df_conflit[df_conflit['Typologie'] == 'HOMME-BUFFLE']
		chimpanze_graph = df_conflit[df_conflit['Typologie'] == 'HOMME-CHIMPANZE']
		hippo_graph = df_conflit[df_conflit['Typologie'] == 'HOMME-HIPPOPOTAME']
		crocodile_graph = df_conflit[df_conflit['Typologie'] == 'HOMME-CROCODILE']
		rino_graph = df_conflit[df_conflit['Typologie'] == 'HOMME-RHINOCEROS']
		leopard_graph = df_conflit[df_conflit['Typologie'] == 'HOMME-LEOPARD']
		singe_graph = df_conflit[df_conflit['Typologie'] == 'HOMME-SINGES']
		epervier_graph = df_conflit[df_conflit['Typologie'] == 'HOMME-EPERVIER']
		chauve_graph = df_conflit[df_conflit['Typologie'] == 'HOMME-CHAUVE SOURIS']
		

		valeur_foyer_select = elephant_graph.groupby(by=['Année'], as_index=False)['Typologie'].count()
		#st.write(valeur_foyer_select.rename(columns={'Typologie': 'Nombre'}))

		valeur_foyer_select1 = buffle_graph.groupby(by=['Année'], as_index=False)['Typologie'].count()
		#st.write(valeur_foyer_select1.rename(columns={'Typologie': 'Nombre'}))
		valeur_foyer_select2 = chimpanze_graph.groupby(by=['Année'], as_index=False)['Typologie'].count()
		valeur_foyer_select3 = hippo_graph.groupby(by=['Année'], as_index=False)['Typologie'].count()
		valeur_foyer_select4 = crocodile_graph.groupby(by=['Année'], as_index=False)['Typologie'].count()
		valeur_foyer_select5 = rino_graph.groupby(by=['Année'], as_index=False)['Typologie'].count()
		valeur_foyer_select6 = leopard_graph.groupby(by=['Année'], as_index=False)['Typologie'].count()
		valeur_foyer_select7 = singe_graph.groupby(by=['Année'], as_index=False)['Typologie'].count()
		valeur_foyer_select8 = epervier_graph.groupby(by=['Année'], as_index=False)['Typologie'].count()
		valeur_foyer_select9 = chauve_graph.groupby(by=['Année'], as_index=False)['Typologie'].count()

		if choix == "Données 💾":
							st.sidebar.markdown("""---""")
							st.sidebar.markdown(f"<h6 style='text-align: center; color: yellow;'>{'Copyright : Decembre 2021 Service Cartographique DFRC'}</h6>", unsafe_allow_html=True)
							st.sidebar.image("minef.png", width=150, caption='')
							#st.sidebar.image("dfrc.png", width=100, caption='DFRC')
							#with open('style.css') as f:
								#st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html=True)

							#st.sidebar.subheader('FILTRE OU RECHERCHE')
							info_text1="""APP.CONFLITS : Gestion des données Conflits Homme-Faune"""
							st.markdown(f"<body style='background-color:NavajoWhite;'><h2 style='text-align: center; color: black;'>{info_text1}</h2></body>", unsafe_allow_html=True)
							
							
							#st.sidebar.image("minef.png", width=80)
							
							st.markdown('')
							#col2.header("APP.CONFLITS : Gestion des données Conflits Homme-Faune")
							info_text2="""L'APP.Conflits sert à : 1. Visualiser les données dans les DataFrames 2. Analyser les données à partir des tableaux statistiques & graphiques
											3. Cartographier les données"""
											
							st.markdown(f"<h5 style='text-align: center; color: white;'>{info_text2}</h5></body>", unsafe_allow_html=True)
							
							#st.write(info_text_1_1)
							
							col1, col2, col_droite = st.columns([0.1,1.8, 0.1])
							#col2.markdown(
								#* ** Source de données : Directions Régionales des Eaux et Forêts.**
								#* ** Traitement de données : Service Cartographique Direction de la Faune et des Ressources Cynégétiques (DFRC)**
								#)

							st.markdown("""---""")
							info_text3="""Typologie des conflits et Pourcentage estimé"""
							st.markdown(f"<h2 style='text-align: center; color: white;'>{info_text3}</h2></body>", unsafe_allow_html=True)
							#st.subheader("Typologie des conflits")

							valeur = pd.DataFrame(df_conflit['Typologie'].value_counts())

							

							valeur['percent'] = (valeur['Typologie'] / valeur['Typologie'].sum()) * 100
							valeur['percent']=valeur['percent'].apply(lambda x:round(x,4))
							#st.write(valeur.rename(columns={'Typologie': 'Nombre de conflit', 'percent':'Pourcentage'}))
							
							txt = "{:.2F} %"

							col3, col4, col5, col6, col7 = st.columns(5)
							with col3 :
								st.image("elephant.png", use_column_width=False, width=80) #caption = 'Eléphant')
								oi1=valeur['percent'].values[0]
								st.markdown(f"<h6 style='text-align: center; color: Red;'>{txt.format(oi1)}</h6>", unsafe_allow_html=True)
								#st.write(txt.format(oi1))
								#st.write()
								#st.write(oi)
							
							with col4 :
								st.image("Buffle.png", use_column_width=False, width=80) #caption = 'Buffle')
								oi2=valeur['percent'].values[1]
								st.markdown(f"<h6 style='text-align: center; color: yellow;'>{txt.format(oi2)}</h6>", unsafe_allow_html=True)
								#st.write(txt.format(oi2))

							with col5 :	
								st.image("chimpanzé.png", use_column_width=False, width=55) #caption = 'Chimpanzé')
								pp=valeur['percent'].values[3]
								st.markdown(f"<h6 style='text-align: center; color: PaleGreen;'>{txt.format(pp)}</h6>", unsafe_allow_html=True)
								#st.write(txt.format(pp))
							
							with col6 :
								st.image("rhinoceros.png", use_column_width=False, width=90) #caption = 'Rhinoceros')
								pp2=valeur['percent'].values[4]
								st.markdown(f"<h6 style='text-align: center; color: PaleGreen;'>{txt.format(pp2)}</h6>", unsafe_allow_html=True)
								#st.write(txt.format(pp2))
							
							with col7 :
								st.image("hippopotamus.png", use_column_width=False, width=135) #caption = 'Hippopotame')
								pp3=valeur['percent'].values[2]
								st.markdown(f"<h6 style='text-align: center; color: yellow;'>{txt.format(pp3)}</h6>", unsafe_allow_html=True)
								#st.write(txt.format(pp3))

							col8, col9, col10, col11, col12 = st.columns(5)
							with col8 :
								st.image("leopard.png", use_column_width=False, width=80)# caption = 'Léopard')
								pp4=valeur['percent'].values[7]
								st.markdown(f"<h6 style='text-align: center; color: PaleGreen;'>{txt.format(pp4)}</h6>", unsafe_allow_html=True)
								#st.write(txt.format(pp4))
							
							with col9 :
								st.image("crocodile.png", use_column_width=False, width=150)# caption = 'Crocrodile')
								pp5=valeur['percent'].values[5]
								st.markdown(f"<h6 style='text-align: center; color: PaleGreen;'>{txt.format(pp5)}</h6>", unsafe_allow_html=True)
								#st.write(txt.format(pp5))
							
							with col10 :
								st.image("singe.png", use_column_width=False, width=50)# caption = 'Singe')
								pp6=valeur['percent'].values[6]
								st.markdown(f"<h6 style='text-align: center; color: PaleGreen;'>{txt.format(pp6)}</h6>", unsafe_allow_html=True)
								#st.write(txt.format(pp6))
							
							with col11 :
								st.image("chauve-souris.png", use_column_width=False, width=150)# caption = 'Chauve-souris')
								pp7=valeur['percent'].values[8]
								st.markdown(f"<h6 style='text-align: center; color: PaleGreen;'>{txt.format(pp7)}</h6>", unsafe_allow_html=True)
								#st.write(txt.format(pp7))
							
							with col12 :
								st.image("epervier.png", use_column_width=False, width=70)# caption = 'Epervier')
								pp8=valeur['percent'].values[9]
								st.markdown(f"<h6 style='text-align: center; color: PaleGreen;'>{txt.format(pp8)}</h6>", unsafe_allow_html=True)
							#colonne_calcule2 = ['Mort', 'Blessé', 'Autres victimes culture et matériel']
							


							




							
							lm1, lm2, lm3 = st.columns([0.5, 1, 0.5])
							lm2.markdown("""---""")
							info_text4="""Tableaux Statistiques des données de conflits"""
							st.markdown(f"<h2 style='text-align: center; color: white;'>{info_text4}</h2></body>", unsafe_allow_html=True)


							

							#st.subheader("Statistique des données conflits Homme-Faune")
							# ---- COMBINER ET GROUPER LES VALEURS EN FONCTION DE LA TYPOLOGIE
							colonne_calcule = ['Mort', 'Blessé', 'Autres victimes culture et matériel']
							conflit_groupe = df_conflit.groupby(['Typologie'], as_index = False)[colonne_calcule].sum()
							st.dataframe(conflit_groupe.rename(columns={'Mort': 'Nombre de personnes mortes', 'Blessé': 'Nombre de personnes blessées'}), height=700)
							

							tablo_plotly = go.Figure(data=[go.Table(header=dict(values=['Typologie', 														
																						'Mort',
																						'Blessé'
																						#'Autres victimes culture et matériel',
																						],
																						fill_color='#FD8E72',
                 																		align='center'),
                 													cells=dict(values=[conflit_groupe.Typologie, conflit_groupe.Mort, conflit_groupe.Blessé],
                 																fill_color='#5D6D7E',
                 																align='center'),


                 													)
                     										])
							#st.write(tablo_plotly)

							Tableau = pd.DataFrame(df_conflit['Typologie'].value_counts())
							valeur_foyer = pd.DataFrame(df_conflit['Département'].value_counts(dropna=True, normalize=False))

							px.set_mapbox_access_token("pk.eyJ1IjoiZnJlZGVyaWNkZWJlcmxpbiIsImEiOiJja3kxbnpwM2kwOGZ3MnZsamZ0aW14OG00In0.SGkMtaVK5Paq0SjH4zJ3sg")
							fig = px.scatter_mapbox(df_conflit, lat="Latitude", lon="Longitude",color="Typologie", center={"lat": 7.3056, "lon": -5.3888},
							                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=20,zoom=5, title = 'Most trafficked US airports<br>(Hover for airport names)')
							#st.write(fig)
							#fig.update_layout(
						        #title = 'Most trafficked US airports<br>(Hover for airport names)',
						        #geo_scope='africa')
							

							#table_1, table_2, table_3 = st.columns(3)
							

							#table_3.markdown("__Effectif des conflits en fonction des (localité)__")
							#table_3.dataframe(Tableau.rename(columns={'Typologie': 'Nombre de conflit'}), height=700)

							#group_mort = df_conflit.groupby("Typologie")["Mort"].sum()
							#table_1.markdown("__Nombre de mort par conflit__")
							#table_1.dataframe(group_mort, height=500, width=300)

							#group_blesse = df_conflit.groupby("Typologie")["Blessé"].sum()
							#table_2.markdown("__Nombre de blessé par conflit__")
							#table_2.dataframe(group_blesse, height=500, width=300)

							#autre_1, autre_2 = st.columns(2)
							#group_victime = df_conflit.groupby("Typologie")["Autres victimes culture et matériel"].sum()
							#autre_1.markdown("__Nombre de victime par conflit__")
							#autre_1.dataframe(group_victime, height=500, width=500)
							
							with st.expander("Cliquer ici pour autres informations"):
									deroulant_1, deroulant_2 = st.columns(2)
									valeur_foyer = df_conflit.groupby(by=['Département'], as_index=False)['Typologie'].count()
									deroulant_1.markdown("__Nombre de conflit par foyer (Département)__")
									deroulant_1.dataframe(valeur_foyer.rename(columns={'Typologie': 'Nombre de conflit'}))
									#deroulant_1.dataframe(valeur_foyer.rename(columns={'Département': 'Nombre de conflit'}), height=400, width=500)
									deroulant_2.markdown("__Effectif et pourcentage par type de conflit (Localité)__")
									deroulant_2.dataframe(valeur.rename(columns={'Typologie': 'Nombre de conflit', 'percent': 'Pourcentage estimé'}), height=500)


							lm1, lm2, lm3 = st.columns([0.5, 1, 0.5])
							lm2.markdown("""---""")
							info_text5="""Données collectées de 2011 à """ + info_text_1_1
							st.markdown(f"<h2 style='text-align: center; color: white;'>{info_text5}</h2></body>", unsafe_allow_html=True)

							#st.subheader("Données des Conflits Homme-Faune de 2011 à 2022")
							deroule_1, deroule_2 = st.columns([1.2, 1])

							list_conflit = ['TOUT'] + df_conflit['Typologie'].unique().tolist()
							s_station = deroule_1.selectbox('Quel conflit voulez-vous afficher ?', list_conflit, key='start_station')
							#deroule_2.download_button(label='Télécharger fichier', data = 'df_conflit', file_name = 'Donnees_CHF')
							
																															
							#conflit_selection = st.sidebar.multiselect('Type de conflit :', conflit_var, default='HOMME-ELEPHANT')

							# you can filter/alter the data based on user input and display the results in a plot
							st.markdown(f"<h5 style='text-align: left; color: yellow;'>{'Voir Données filtrées dans le tableau ci-dessous ⬇️'}</h5></body>", unsafe_allow_html=True)
							#st.write('Données filtrées')
							#with open('BD_conflitHommeFaune.xlsx', 'rb') as f:
								#st.download_button(label='Télécharger fichier', data = f)
							#st.download_button(label='Télécharger fichier', data = 's_station', file_name = 'Donnees_CHF', mime='.xlsx')
							if s_station != 'TOUT':
								display_data = df_conflit[df_conflit['Typologie'] == s_station]
								#mask = (df_conflit['Typologie'].isin(list_conflit))
								#number_of_result = df_conflit[mask].shape[0]
								#st.sidebar.markdown(f'*Resultat disponible:{number_of_result}*')

							else:
								display_data = df_conflit.copy()


							# display the dataset in a table format
							# if you'd like to customize it more, consider plotly tables: https://plotly.com/python/table/
							# I have a YouTube tutorial that can help you in this: https://youtu.be/CYi0pPWQ1Do
							st.dataframe(data=display_data, height=800)


							#st.markdown("""---""")
							#st.subheader("Données des Conflits Homme-Faune de 2011 à Juillet 2021")

							


							### --- BARRE LATERALE
							## st.sidebar.header('CONTROLEUR DE DONNEES')
							## selection_annee = st.sidebar.selectbox('Année de conflit', list(reversed(range(2011,2022))))

							### --- CHARGER DONNEES EXCEL ET LES METTRE DANS UN DATAFRAME

							#with st.expander("Cliquer ici pour afficher la liste"):
								#st.dataframe(data=df_conflit, height=700)
								#st.download_button(label='Telecharger données', data='df_conflit_conflit', file_name='donnees_CHF' )

							
							
							#REQUETE SUR LE TABLEUR

							#df_conflit_statistique = pd.read_excel(
												#io='conflit_faune.xlsx',
							                    #sheet_name='DATA',
							                    #usecols='K:O',
							                    #header=1)

							#conflit = st.sidebar.multiselect("Choisir conflit:",
									    #options=df_conflit["Typologie"].unique())
									    #default="HOMME-ELEPHANTS"
									

							#localite = st.sidebar.multiselect(
									    #"Choisir localité:",
									   # options=df_conflit["localite"].unique())
									    #default="ABIDJAN"
									

							#annee = st.sidebar.multiselect(
									    #"Choisir année:",
									    #options=df_conflit["Année"].unique(),
									    #default=[2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011])
									
							#df_conflit_selection = df_conflit.query("Typologie == @conflit & Année == @annee") #& localite == @localite
							
							#st.markdown("""---""")
							#st.subheader("Resultat du filtre ci-dessous")
							#st.dataframe(df_conflit_selection)
							#st.sidebar.text(f'voir le resultat ci-dessous')
				
		elif choix == "Tableau de bord 📈":
							st.sidebar.markdown("""---""")
							st.sidebar.markdown(f"<h6 style='text-align: center; color: yellow;'>{'Copyright : Decembre 2021 Service Cartographique DFRC'}</h6>", unsafe_allow_html=True)
							#st.markdown(f"<h6 style='text-align: center; color: yellow;'>{info_text}</h6>", unsafe_allow_html=True)
							st.sidebar.image("minef.png", width=150, caption='')
							#st.sidebar.image("dfrc.png", width=100, caption='DFRC')
							#st.markdown("https://app.powerbi.com/links/vkkaAgsrD6?ctid=eecc4b36-240a-4a05-b3bc-72718c4c513f&pbi_source=linkShare")
							#st.components.html
							#st.components.htmlst.markdownunsafe_allow_html=True

							#st.dataframe(data=df_conflit, height=600)
							#st.download_button(label='Telecharger données', data='conflit_faune.xlsx', file_name='donnees_CHF.xlsx')
							repre_1, repre_2, repre_3 = st.columns([0.7, 1.5, 0.5])
							repre_2.subheader("REPRESENTATION GRAPHIQUE DES DONNEES")
							st.markdown("""---""")

							part_typologie, part_annee = st.columns(2)
							user_type = df_conflit['Typologie'].value_counts().reset_index()
							user_type.columns = ['Conflit','valeur']

							fig = px.pie(user_type, values='valeur', names = 'Conflit', hover_name='Conflit')

							# TODO: change the values of the update_layout function and see the effect
							fig.update_layout(showlegend=True,
								title='Part de chaque type de conflit (%)',
								width=500,
								height=500,
								margin=dict(l=1,r=1,b=1,t=1),
								font=dict(color='#FFFFFF', size=12),
								paper_bgcolor='#5D6D7E',
    							plot_bgcolor='white',
    							legend=dict(
											orientation="v", 
											title_font_color="white", 
											y=1.30, 
											x=0.9, 
											xanchor="left",
											#yanchor="left", 
											title=''
													)
    							)

							# this function adds labels to the pie chart
							# for more information on this chart, visit: https://plotly.com/python/pie-charts/
							fig.update_traces(textposition='inside', textinfo='percent')

							# after creating the chart, we display it on the app's screen using this command
							#part_typologie.markdown('__Part de chaque type de conflit (%)__')
							part_typologie.write(fig, use_container_width=True)


							#st.subheader('Nombre de conflit par année')
							annee_diagramme = pd.DataFrame(df_conflit['Année'].value_counts())
							#part_annee.markdown('__Evolution des conflits au cours des années__')
							#part_annee.bar_chart(annee_diagramme, use_container_width=True)
							#st.write(annee_diagramme)

							anne_group = df_conflit.groupby(by=['Année'], as_index=False)['Typologie'].count()
							#st.write(anne_group)
							fig_annee = go.Figure()
							fig_annee.add_trace(go.Scatter(x=anne_group.Année, 
															y=anne_group.Typologie,
															mode= 'lines+markers', 
															name='Victimes', 
															line=dict(
																	color='goldenrod', 
																	width=2, 
																	dash='dashdot')
															)
												)

							fig_annee.update_layout(title="Evolution des conflits de 2011 à " + info_text_1_1,
												xaxis_title="Année de conflit", 
												yaxis_title="Effectif des conflit", 
												legend_title="Légende",
												xaxis=dict(
														showline=True,
														showgrid=True,
														showticklabels=True,
														linecolor='rgb(4, 4, 4)',
														linewidth=2,
													    ticks='outside',
													    tickfont=dict(
													    		family='Arial',
													    		size=12,
													    		color='rgb(255, 255, 255)')
													    ),
												    # Turn off everything on y axis
											    yaxis=dict(
											        showgrid=True,
											        zeroline=False,
											        showline=False,
											        showticklabels=True
												),
												paper_bgcolor='#5D6D7E',
    											plot_bgcolor='white')

							fig_annee.update_xaxes(
													gridcolor='black',
													tickfont=dict(
														family='Arial', 
														color='white', 
														size=12),
													title_font=dict(
														color='white', 
														size=16
														)
													)

							fig_annee.update_yaxes(
													gridcolor='black',
													tickfont=dict(
														family='Arial', 
														color='white', 
														size=12),
													title_font=dict(
														color='white', 
														size=16
														)
													)
							part_annee.write(fig_annee)

							#fig_annee = px.line(anne_group, 
												#x='Année', y='Typologie', labels={'Année':'Année de conflit', 'Typologie':'nombre de conflit'})
							#part_annee.write(fig_annee, use_container_width=True)

							colonne_calcule = ['Mort', 'Blessé', 'Autres victimes culture et matériel']
							conflit_groupe = df_conflit.groupby(['Année'], as_index = False)[colonne_calcule].sum()
							#st.write(conflit_groupe.rename(columns={'Autres victimes culture et matériel': 'Victimes'}))
							conflit_copie = conflit_groupe.copy()
							conflit_copie.rename(columns={'Autres victimes culture et matériel': 'Victimes'}, inplace=True)
							#fig_annee_victim_autre = px.line(conflit_groupe, 
												#x='Année', y=['Mort', 'Blessé'], labels={'Année':'Année de conflit'})
							#st.write(fig_annee_victim_autre, use_container_width=True)
							figure_1, figure_2 = st.columns(2)
							fig_1 = go.Figure()
							#figure_1.markdown('Evolution des effetifs des blessés et morts au cours des années')
							fig_1.add_trace(go.Scatter(x=conflit_groupe.Année, y=conflit_groupe.Blessé,
														mode= 'lines+markers', name='Blessé', line=dict(color='firebrick', width=2, dash='dashdot')))

							fig_1.add_trace(go.Scatter(x=conflit_groupe.Année, y=conflit_groupe.Mort,
														mode= 'lines+markers', 
														name='Mort', 
														line=dict(
																color='goldenrod', 
																width=2, 
																dash='dashdot'
																)
														)
											)
							fig_1.update_layout(title="Evolution des effectifs des blessés et morts de 2011 à " + info_text_1_1, 
												xaxis_title="Année de conflit", 
												yaxis_title="Nombre de Mort + Blessé", 
												legend_title="Légende",
												paper_bgcolor='#5D6D7E',
    											plot_bgcolor='white',
    											height=400, 
    											width=700)
							#fig_1.update_xaxes(gridcolor='black', range=[2011, 2030])
							fig_1.update_xaxes(gridcolor='black', 
													tickfont=dict(
														family='Arial', 
														color='white', 
														size=12),
													title_font=dict(
														color='white', 
														size=16
														)
													)
							fig_1.update_yaxes(gridcolor='black', 
													tickfont=dict(
														family='Arial', 
														color='white', 
														size=12),
													title_font=dict(
														color='white', 
														size=16
														)
													)
							figure_1.write(fig_1)
							

							fig_2 = go.Figure()
							fig_2.add_trace(go.Scatter(x=conflit_copie.Année, 
														y=conflit_copie.Victimes,
														mode= 'lines+markers', 
														name='Victimes', 
														line=dict(
															color='fuchsia', 
															width=2, 
															dash='dashdot')))

							fig_2.update_layout(title="Evolution des effectifs des victimes (matériels & cultures) de 2011 à " + info_text_1_1,
												xaxis_title="Année de conflit", yaxis_title="Nombre de victime", legend_title="Légende",
												xaxis=dict(
													showline=True,
													gridcolor='black',
													showgrid=True,
													showticklabels=True,
													linecolor='rgb(4, 4, 4)',
													linewidth=2,
													ticks='outside',
													tickfont=dict(
														family='Arial',
														size=12,
														color='rgb(255, 255, 255)')),
												    # Turn off everything on y axis
											    yaxis=dict(
											        showgrid=True,
											        gridcolor='black',
											        zeroline=False,
											        showline=False,
											        showticklabels=True
												),
												paper_bgcolor='#5D6D7E',
    											plot_bgcolor='white',
    											height=400, 
    											width=700)

							fig_2.update_xaxes(tickfont=dict(
														family='Arial', 
														color='white', 
														size=10),
													title_font=dict(
														color='white', 
														size=16
														)
													)

							fig_2.update_yaxes(gridcolor='black', 
													tickfont=dict(
														family='Arial', 
														color='white', 
														size=12),
													title_font=dict(
														color='white', 
														size=16
														)
													)
											    										    
							figure_2.write(fig_2)

							graph_4, graph_5, graph_6 = st.columns([0.5, 1, 0.5])
							#DIAGRAMME D'EVOLUTION DES DIFFERENTS TYPES DE CONFLITS
							fig_elephant = go.Figure()
							fig_elephant.add_trace(go.Scatter(x=valeur_foyer_select.Année, 
															y=valeur_foyer_select.Typologie,mode= 'lines+markers',name='Elephant',  
															line=dict(color='red', width=2, dash='dashdot')	
															))
												
							fig_elephant.add_trace(go.Scatter(x=valeur_foyer_select1.Année, y=valeur_foyer_select1.Typologie,
														mode= 'lines+markers', 
														name='Buffle', 
														line=dict(color='goldenrod', width=2, dash='dashdot')))

							fig_elephant.add_trace(go.Scatter(x=valeur_foyer_select2.Année, y=valeur_foyer_select2.Typologie,
														mode= 'lines+markers', name='Chimpanzé',
														line=dict(color='green',width=2,dash='dashdot' 
																)))
															
							fig_elephant.add_trace(go.Scatter(x=valeur_foyer_select3.Année, y=valeur_foyer_select3.Typologie,
														mode= 'lines+markers', 
														name='Hippopotame', 
														line=dict(
																color='violet', 
																width=2, 
																dash='dashdot'
																)
														)
											)

							fig_elephant.add_trace(go.Scatter(x=valeur_foyer_select4.Année, y=valeur_foyer_select4.Typologie,
														mode= 'lines+markers', 
														name='Crocodile', 
														line=dict(
																color='navy', 
																width=2, 
																dash='dashdot'
																)
														)
											)

							fig_elephant.add_trace(go.Scatter(x=valeur_foyer_select5.Année, y=valeur_foyer_select4.Typologie,
														mode= 'lines+markers', 
														name='Rhinoceros', 
														line=dict(
																color='lightskyblue', 
																width=2, 
																dash='dashdot'
																)
														)
											)

							fig_elephant.add_trace(go.Scatter(x=valeur_foyer_select6.Année, y=valeur_foyer_select6.Typologie,
														mode= 'lines+markers', 
														name='Léopard', 
														line=dict(color='darkviolet', width=2, dash='dashdot')))

							fig_elephant.add_trace(go.Scatter(x=valeur_foyer_select7.Année, y=valeur_foyer_select7.Typologie,
														mode= 'lines+markers', 
														name='Singe', 
														line=dict(color='black', width=2, dash='dashdot')))

							fig_elephant.add_trace(go.Scatter(x=valeur_foyer_select8.Année, y=valeur_foyer_select8.Typologie,
														mode= 'lines+markers', 
														name='Epervier', 
														line=dict(color='pink', width=2, dash='dashdot')))

							fig_elephant.add_trace(go.Scatter(x=valeur_foyer_select9.Année, y=valeur_foyer_select9.Typologie,
														mode= 'lines+markers', 
														name='Chauve-souris', 
														line=dict(color='yellow', width=2, dash='dashdot')))

							fig_elephant.update_layout(title="Evolution de chaque types de conflits de 2011 à " + info_text_1_1,
												xaxis_title="Année de conflit", 
												yaxis_title="Nombre de conflits", 
												legend_title="Conflit",
												xaxis=dict(
														showline=True,
														showgrid=True,
														showticklabels=True,
														linecolor='rgb(4, 4, 4)',
														linewidth=2,
													    ticks='outside',
													    tickfont=dict(
													    		family='Arial',
													    		size=12,
													    		color='rgb(255, 255, 255)')
													    ),
												    # Turn off everything on y axis
											    yaxis=dict(
											        showgrid=True,
											        zeroline=False,
											        showline=False,
											        showticklabels=True
												),
												paper_bgcolor='#5D6D7E',
    											plot_bgcolor='white')

							fig_elephant.update_xaxes(gridcolor='black',
													tickfont=dict(family='Arial', 
														color='white',size=12), 
													title_font=dict(
														color='white', 
														size=16
														)
													)

							fig_elephant.update_yaxes(
													gridcolor='black',
													tickfont=dict(
														family='Arial', 
														color='white', 
														size=12),
													title_font=dict(
														color='white', 
														size=16
														)
													)
							graph_5.write(fig_elephant)

							#st.write(annee_diagramme)
							#CREATION DE COLONNE POUR DISPOSITION ELEMENTS  
							left_column, right_column = st.columns(2)

							#st.markdown('__Effectif des morts, des blessés et des victimes par type de conflit__')
							bar_chart = px.bar(df_blesses_mort_victime,
												x = 'Typologie conflit',
												y = 'Nombre',
												color = 'Attribut',
												barmode="group",
												title='Effectif des morts, des blessés et des victimes par type de conflit de 2011 à ' + info_text_1_1,
												hover_name="Typologie conflit",
												#color_continuous_scale=['red', 'yellow', 'green'],
												#template='plotly_white',
												#title='hhhhf')
												text = 'Nombre')
							bar_chart.update_layout({
												'plot_bgcolor': 'white',
												'paper_bgcolor': '#5D6D7E'
												}, font_color="black", 
												title_font_color="white", 
												legend_font_color="white",
												legend=dict(
													orientation="v", 
													title_font_color="white", 
													#y=1.15, 
													#x=0.6, 
													xanchor="left", 
													title=''
													)
												)
							bar_chart.update_xaxes(tickfont=dict(
														family='Arial', 
														color='white', 
														size=10),
													title_font=dict(
														color='white', 
														size=16
														)
													)

							bar_chart.update_yaxes(gridcolor='black', 
													tickfont=dict(
														family='Arial', 
														color='white', 
														size=12),
													title_font=dict(
														color='white', 
														size=16
														)
													)#, range=[-1, 200]
							st.plotly_chart(bar_chart, use_container_width=True)

							#st.markdown('__Effectif des blèssés par conflit__')
							#bar_chart2 = px.bar(df_blesses,
												#x = 'ConflitBlessé',
												#y = 'NombreBlessé',
												#text = 'NombreBlessé')
							#st.write(bar_chart2)



							#st.subheader('Effectif total par type de conflits')
							#pie_chart_complet = pd.DataFrame(df_conflit['Typologie'].value_counts())					
							#left_column.markdown('__Effectif total par conflits__')
							#right_column.bar_chart(pie_chart_complet, use_container_width=True)

							
							posi1, posi2 = st.columns(2)
							#voir = df_conflit.groupby("Typologie")["Blessé"].sum()
							#posi1.markdown('__Effectif des blèssés par conflit__')
							#posi1.bar_chart(voir)

							#voir2 = df_conflit.groupby("Typologie")["Mort"].sum()
							#posi2.markdown('__Effectif des morts par conflit__')
							#posi2.bar_chart(voir2)


							#voir3 = df_conflit.groupby("Typologie")["Autres victimes culture et matériel"].sum()
							#st.markdown('__Effectif des victimes par conflit__')
							#st.bar_chart(voir3)

							departement_group = df_conflit.groupby(by=['Département'], as_index=False)['Typologie'].count()
							#st.write(departement_group)
							bar_chart_departement = px.bar(departement_group,
												x = 'Département',
												y = 'Typologie',
												
												
												title='Effectif des conflit par departement (Foyer de conflit) de 2011 à ' + info_text_1_1,
												hover_name="Département",
												#color_continuous_scale=['red', 'yellow', 'green'],
												#template='plotly_white',
												#title='hhhhf')
												text = 'Typologie')
							bar_chart_departement.update_layout({
												'plot_bgcolor': 'white',
												'paper_bgcolor': '#5D6D7E'
												}, xaxis_title="Foyer de conflit", yaxis_title="Nombre de conflit")
							
							bar_chart_departement.update_xaxes(tickangle=45, tickfont=dict(family='Arial', color='white', size=12),
													title_font=dict(color='white', size=16))
							bar_chart_departement.update_yaxes(gridcolor='black', tickfont=dict(family='Arial', color='white', size=12),
													title_font=dict(color='white', size=16))
							st.plotly_chart(bar_chart_departement, use_container_width=True)


							#pie_chart_foyer = pd.DataFrame(df_conflit['Département'].value_counts())
							#st.markdown('__Effectif par foyer de conflit__')
							#st.bar_chart(pie_chart_foyer, use_container_width=True)

							#voir3 = df_conflit["conflit", "annee"]("HOMME-ELEPHANTS")
							#st.dataframe(voir3)


				
							text_a, text_b, text_c = st.columns([0.5, 1, 0.5])
							text_b.markdown("""---""")
							text_b.header('Filtre avancée en mode graphique')
							info_text="""Pour filtrer, il faut choisir une ou plusieurs années de conflits ainsi que un ou plusieurs types de conflits.
													A titre d'exemple, nous avons selectionné l'an 2020 avec le type de conflit 'HOMME-ELEPHANT'.
													L'interpretation est qu'en 2020, nous avions eu 29 conflit HOMME-ELEPHANT"""
							st.markdown(f"<h6 style='text-align: center; color: yellow;'>{info_text}</h6>", unsafe_allow_html=True)

							#st.markdown(f"<h6 style='text-align: center; color: yellow;'>{txt.format(pp6)}</h6>", unsafe_allow_html=True)
							

							#AJOUT DES DONNEES DU FILTRE
							requete_1, requete_2 = st.columns(2)
							graph_1, graph_2, graph_3 = st.columns([0.5, 1, 0.5])

							annee_var = df_conflit['Année'].unique().tolist()
							annee_selection = requete_1.multiselect('Annee de conflit :', annee_var, default=2020)

							conflit_var = df_conflit['Typologie'].unique().tolist()
							conflit_selection = requete_2.multiselect('Type de conflit :', conflit_var, default='HOMME-ELEPHANT')

							
							## FILTRE DE DONNEES PAR CONFLIT

							mask = (df_conflit['Année'].isin(annee_selection)) & (df_conflit['Typologie'].isin(conflit_selection))
							number_of_result = df_conflit[mask].shape[0]
							graph_2.markdown(f'*Resultat disponible:{number_of_result}*')

							## GROUPER BLOC DE DONNEES APRES SELECTION
							df_conflit_grouper = df_conflit[mask].groupby(by=['Typologie']).count()[['Année']]
							df_conflit_grouper = df_conflit_grouper.rename(columns = {'Année':'Effectif'})
							df_conflit_grouper = df_conflit_grouper.reset_index()

							
							## AFFICHE LE DIAGRAMME DU FILTRE 
							#st.markdown("__Diagramme en Bande des données filtrées__")
							graphique = px.bar(df_conflit_grouper,
												x='Typologie',
												y='Effectif',
												text='Effectif',
												title='Diagramme en Bande des données filtrées',)
							#st.plotly_chart(graphique)
       
							
       						#st.subheader('Effectif total par type de conflits')
							#voir4 = px.df_conflit.groupby("conflit").count()["Victimes"].sum()				
							#st.markdown('__Effectif des victimes par conflits__')
							#graphique2 = px.bar(voir4,
							#	x='Victimes',
							#	y='Victimes',
							#	#text='Effectif'
        									#	)
							#st.plotly_chart(graphique2)
							
							graph_1, graph_2, graph_3 = st.columns([0.5, 1, 0.5])
							graphique.update_layout(title="Effectifs des conflits en fonction des années",
												xaxis_title="Type de conflit", yaxis_title="Nombre de conflit", legend_title="Légende",
												xaxis=dict(
													showline=True,
													gridcolor='black',
													showgrid=True,
													showticklabels=True,
													linecolor='rgb(4, 4, 4)',
													linewidth=2,
													ticks='outside',
													tickfont=dict(
														family='Arial',
														size=12,
														color='rgb(255, 255, 255)')),
												    # Turn off everything on y axis
											    yaxis=dict(
											        showgrid=True,
											        gridcolor='black',
											        zeroline=False,
											        showline=False,
											        showticklabels=True
												),
												paper_bgcolor='#5D6D7E',
    											plot_bgcolor='white',
    											height=400, 
    											width=700)

							graphique.update_xaxes(tickfont=dict(
														family='Arial', 
														color='white', 
														size=10),
													title_font=dict(
														color='white', 
														size=16
														)
													)

							graphique.update_yaxes(gridcolor='black', 
													tickfont=dict(
														family='Arial', 
														color='white', 
														size=12),
													title_font=dict(
														color='white', 
														size=16
														)
													)
											    										    
							graph_2.write(graphique)



		elif choix == "Cartographie 🌈":

			page_nom = ["Carte de conflits", "Carte de chaleur" ]
			page = st.sidebar.radio('Aller à', page_nom)

			st.sidebar.markdown("""---""")
			st.sidebar.markdown(f"<h6 style='text-align: center; color: yellow;'>{'Copyright : Decembre 2021 Service Cartographique DFRC'}</h6>", unsafe_allow_html=True)
			st.sidebar.image("minef.png", width=150, caption='')
			#st.sidebar.image("dfrc.png", width=100, caption='DFRC')



			#menu_deuxieme = ["CARTE DES CONFLITS", "CARTE DE CHALEUR"]
			#choix_deuxieme = st.sidebar.selectbox("Choisir type de carte", menu_deuxieme)

			if page == "Carte de conflits":
					#my_bar = st.progress(0)
					#for percent_complete in range(100):
						#time.sleep(0.05)
						#my_bar.progress(percent_complete + 1)

					#df_conflit1 = pd.read_csv("clean_data_sample.csv")
					#st.dataframe(df_conflit1)
					#st.header("CARTOGRAPHIE DES TYPES DE CONFLITS DE 2011 A 2021 ")
					
					#df_conflit = df_conflit[['Latitude'].notnull() & ['Longitude'].notnull()]

					df_conflit_elephant = pd.DataFrame(df_conflit[df_conflit["Typologie"] == "HOMME-ELEPHANT"])
					df_conflit_buffle = pd.DataFrame(df_conflit[df_conflit["Typologie"] == "HOMME-BUFFLE"])
					df_conflit_chauvesouris = pd.DataFrame(df_conflit[df_conflit["Typologie"] == "HOMME-CHAUVE-SOURIS"])
					df_conflit_chimpanze = pd.DataFrame(df_conflit[df_conflit["Typologie"] == "HOMME-CHIMPANZE"])
					df_conflit_rhinoceros = pd.DataFrame(df_conflit[df_conflit["Typologie"] == "HOMME-RHINOCEROS"])
					df_conflit_hippopotame = pd.DataFrame(df_conflit[df_conflit["Typologie"] == "HOMME-HIPPOPOTAME"])
					df_conflit_leopard = pd.DataFrame(df_conflit[df_conflit["Typologie"] == "HOMME-LEOPARD"])
					df_conflit_crocodile = pd.DataFrame(df_conflit[df_conflit["Typologie"] == "HOMME-CROCODILE"])
					df_conflit_singe = pd.DataFrame(df_conflit[df_conflit["Typologie"] == "HOMME-SINGE"])
					df_conflit_epervier = pd.DataFrame(df_conflit[df_conflit["Typologie"] == "HOMME-EPERVIER"])

					#ip = df_conflit[["Latitude", "Longitude", "conflit"]]
					
					#op = df_conflit.set_index("Latitude")#[("Latitude", "conflit")]
					#st.dataframe(ip)
					#coord = pd.DataFrame(df_conflit)
					#st.dataframe(coord)
					#****fichier = pd.DataFrame(coord, columns=['Latitude', 'Longitude'])
					#*****st.map(fichier)

					# VARIABLE POUR AFFICHER LA CARTE
					carte = folium.Map(location=[7.3056, -5.3888], zoom_start=7, control_scale=True,
										max_bounds=True) # min_lat=4.05, max_lat=10.80, min_lon=-8.86, max_lon=-2.30prefer_canvas=True
					

					#OUTILS DESSINS
					draw = plugins.Draw(export=True)

					#POSITION DE LA SOURIS
					MousePosition(separator=' | ', prefix="Coordonnée lat I lon :").add_to(carte)



					#AJOUTE PLEIN ECRAN A LA CARTE
					plugins.Fullscreen(position='topleft').add_to(carte)

					
					draw.add_to(carte)
					#INSERER LES DONNEES LAT LONG DANS LA CARTE
					#for (index, row) in df_conflit.iterrows():
					#for (i, row) in df_conflit.iterrows():
						#lat = df_conflit.at[i, 'Latitude']
						#lng = df_conflit.at[i, 'Longitude']
						#info = df_conflit.at[i, 'conflit']

						#popup = '<b>'+'<br>'+ "INFORMATION" + '</br>'+'</b>' + '<b>'+'<br>'+ "Conflit : "+'</b>'+ df_conflit.at[i, 'conflit'] +
						#'<b>'+'<br>'+ "Localité : "+'</b>'+ df_conflit.at[i, 'localite'] +
						#'<b>'+'<br>'+ "Annee : "+'</b>'+ df_conflit.at[i, 'annee']
						#folium.Marker(location=[lat, lng], popup=)

					#CREATION D'UN CLUSTER
					markerCluster_elephant = MarkerCluster(name='Conflit Homme-Faune').add_to(carte)
					#markerCluster_buffle = MarkerCluster(name='homme-buffle').add_to(carte)
					#markerCluster_chauvesouris = MarkerCluster(name='homme-chauve-souris').add_to(carte)
					#markerCluster_chimpanze = MarkerCluster(name='homme-chimpanzé').add_to(carte)
					#markerCluster_rhinoceros = MarkerCluster(name='homme-Rhinoceros').add_to(carte)
					#markerCluster_hippopotame = MarkerCluster(name='homme-Hippopotame').add_to(carte)
					#markerCluster_leopard = MarkerCluster(name='homme-Léopard').add_to(carte)
					#markerCluster_crocodile = MarkerCluster(name='homme-Crocodile').add_to(carte)
					#markerCluster_singe = MarkerCluster(name='homme-Singe').add_to(carte)
					#markerCluster_epervier = MarkerCluster(name='homme-Epervier').add_to(carte)
					#df_conflit_elephant = df_conflit_elephant[['Latitude'].notnull() & ['Longitude'].notnull()]
					#df_conflit_elephant = list(df_conflit_elephant[['Latitude', 'Longitude']].values)

					for (index, row) in df_conflit_elephant.iterrows():
						icon_elephant = folium.features.CustomIcon('./elephant2.png', icon_size=(30,30))
						iframe = folium.IFrame('<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["Typologie"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["Localité"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["Année"])+'</br>')
						popup = folium.Popup(iframe, min_width=300, max_width=300)
						folium.Marker(location=[row.loc["Latitude"], row.loc["Longitude"]],
							icon = icon_elephant,  
							popup = popup,
							tooltip="cliquer pour info").add_to(markerCluster_elephant)

					#BUFFLES UNIQUEMENT DANS LA CARTE
					#icon_buffle = folium.features.CustomIcon('Buffle.png', icon_size=(100,100))

					for (index, row) in df_conflit_buffle.iterrows():
						icon_buffle = folium.features.CustomIcon('./Buffle3.png', icon_size=(30,30))
						iframe = folium.IFrame('<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["Typologie"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["Localité"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["Année"])+'</br>')
						popup = folium.Popup(iframe, min_width=300, max_width=300, min_hight=300, max_hight=300)
						folium.Marker(location=[row.loc["Latitude"], row.loc["Longitude"]],
							icon = icon_buffle,  
							popup = popup,
							tooltip="cliquer pour info").add_to(markerCluster_elephant)


					#CHAUVE-SOURIS UNIQUEMENT DANS LA CARTE
					for (index, row) in df_conflit_chauvesouris.iterrows():
						icon_chauve = folium.features.CustomIcon('./chauve-souris2.png', icon_size=(30,30))
						iframe = folium.IFrame('<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["Typologie"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["Localité"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["Année"])+'</br>')
						popup = folium.Popup(iframe, min_width=300, max_width=300, min_hight=300, max_hight=300)
						folium.Marker(location=[row.loc["Latitude"], row.loc["Longitude"]],
							icon = icon_chauve,  
							popup = popup,
							tooltip="cliquer pour info").add_to(markerCluster_elephant)



					#CHIMPANZES UNIQUEMENT DANS LA CARTE
					for (index, row) in df_conflit_chimpanze.iterrows():
						icon_chimpanze = folium.features.CustomIcon('./chimpanzé2.png', icon_size=(30,30))
						iframe = folium.IFrame('<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["Typologie"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["Localité"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["Année"])+'</br>')
						popup = folium.Popup(iframe, min_width=300, max_width=300, min_hight=300, max_hight=300)
						folium.Marker(location=[row.loc["Latitude"], row.loc["Longitude"]],
							icon = icon_chimpanze,  
							popup = popup,
							tooltip="cliquer pour info").add_to(markerCluster_elephant)


					#rhinoceros UNIQUEMENT DANS LA CARTE
					for (index, row) in df_conflit_rhinoceros.iterrows():
						icon_rhino = folium.features.CustomIcon('./rhinoceros2.png', icon_size=(30,30))
						iframe = folium.IFrame('<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["Typologie"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["Localité"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["Année"])+'</br>')
						popup = folium.Popup(iframe, min_width=300, max_width=300, min_hight=300, max_hight=300)
						folium.Marker(location=[row.loc["Latitude"], row.loc["Longitude"]],
							icon = icon_rhino,  
							popup = popup,
							tooltip="cliquer pour info").add_to(markerCluster_elephant)


					#Hippopotame UNIQUEMENT DANS LA CARTE
					for (index, row) in df_conflit_hippopotame.iterrows():
						icon_hippo = folium.features.CustomIcon('./hippopotamus2.png', icon_size=(30,30))
						iframe = folium.IFrame('<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["Typologie"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["Localité"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["Année"])+'</br>')
						popup = folium.Popup(iframe, min_width=300, max_width=300, min_hight=300, max_hight=300)
						folium.Marker(location=[row.loc["Latitude"], row.loc["Longitude"]],
							icon = icon_hippo,  
							popup = popup,
							tooltip="cliquer pour info").add_to(markerCluster_elephant)


					#Leopard UNIQUEMENT DANS LA CARTE
					for (index, row) in df_conflit_leopard.iterrows():
						icon_leopard = folium.features.CustomIcon('./leopard2.png', icon_size=(30,30))
						iframe = folium.IFrame('<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["Typologie"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["Localité"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["Année"])+'</br>')
						popup = folium.Popup(iframe, min_width=300, max_width=300, min_hight=300, max_hight=300)
						folium.Marker(location=[row.loc["Latitude"], row.loc["Longitude"]],
							icon = icon_leopard,  
							popup = popup,
							tooltip="cliquer pour info").add_to(markerCluster_elephant)


					#crocodile UNIQUEMENT DANS LA CARTE
					for (index, row) in df_conflit_crocodile.iterrows():
						icon_crocodile = folium.features.CustomIcon('./crocodile2.png', icon_size=(30,30))
						iframe = folium.IFrame('<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["Typologie"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["Localité"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["Année"])+'</br>')
						popup = folium.Popup(iframe, min_width=300, max_width=300, min_hight=300, max_hight=300)
						folium.Marker(location=[row.loc["Latitude"], row.loc["Longitude"]],
							icon = icon_crocodile,  
							popup = popup,
							tooltip="cliquer pour info").add_to(markerCluster_elephant)


					#singe UNIQUEMENT DANS LA CARTE
					for (index, row) in df_conflit_singe.iterrows():
						icon_singe = folium.features.CustomIcon('./singe2.png', icon_size=(30,30))
						iframe = folium.IFrame('<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["Typologie"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["Localité"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["Année"])+'</br>')
						popup = folium.Popup(iframe, min_width=300, max_width=300, min_hight=300, max_hight=300)
						folium.Marker(location=[row.loc["Latitude"], row.loc["Longitude"]],
							icon = icon_singe,  
							popup = popup,
							tooltip="cliquer pour info").add_to(markerCluster_elephant)



					#epervier UNIQUEMENT DANS LA CARTE
					for (index, row) in df_conflit_epervier.iterrows():
						icon_epervier = folium.features.CustomIcon('./epervier2.png', icon_size=(30,30))
						iframe = folium.IFrame('<b>'+'<br>'+ "INFORMATION" +'</br>'+'</b>' + '<b>'+'<br>'+"Conflit : "+'</b>'+ row.loc["Typologie"] 
							+ '<br>'+'<b>'+'<br>'+"Localité : "+'</b>'+ row.loc["Localité"]+'</br>' + '<b>'+'<br>' 
							+ "Année : "+'</b>'+ str(row.loc["Année"])+'</br>')
						popup = folium.Popup(iframe, min_width=300, max_width=300, min_hight=300, max_hight=300)
						folium.Marker(location=[row.loc["Latitude"], row.loc["Longitude"]],
							icon = icon_epervier,  
							popup = popup,
							tooltip="cliquer pour info").add_to(markerCluster_elephant)


					# Add hover functionality.
					highlight_function = lambda x: {'fillColor': '#000000', 
					                                'color':'#000000', 
					                                'fillOpacity': 0.50, 
					                                'weight': 0.1}


        			#groupe_entite = FeatureGroup(name="Aire protégée")

					#AJOUT DE FICHIER DE FORME AU FORMAT GEOJSON
					foyer_conflit = folium.features.GeoJson('foyer_conflits.geojson', name='Foyer de conflit (Departement)', popup=folium.features.GeoJsonPopup(fields=["NOM"]+["REG_2012"], aliases=['Foyer de :','Region de :']), 
						highlight_function = highlight_function, tooltip=folium.features.GeoJsonTooltip(fields=['NOM','REG_2012'],aliases=['Foyer de : ','Region de : '], 
						style=("background-color: white; color: #333333; font-family:arial; font-size: 12px; padding: 10px;")),
						style_function=lambda x:{'fillColor': '#708090', 'color': '#000000', 'fillOpacity':4, 'weight':0.3}, show = False).add_to(carte)


					fc = folium.features.GeoJson('foret_classee.geojson', name='Forêt Classée', highlight_function = highlight_function, 
						tooltip=folium.features.GeoJsonTooltip(fields=['nom','sup'], aliases=['Nom FC :','Superficie (ha) :'], 
						style=("background-color: white; color: #333333; font-family:arial; font-size: 12px; padding: 10px;")), 
						popup=folium.features.GeoJsonPopup(fields=["nom"]+["sup"], aliases=['Nom FC :','Superficie (ha) :']), 
						style_function=lambda x:{'fillColor': '#00FF00', 'color': '#228B22', 'fillOpacity':0.1, 'weight':1}).add_to(carte)

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
													attr="google", name="google imagerie", control=True).add_to(carte)

					folium.raster_layers.TileLayer('Stamen Terrain', name="Topographie").add_to(carte)


					folium.raster_layers.TileLayer(tiles="http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", 
								attr="google", name="Aucun fond", control=True).add_to(carte)

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



					#Ajouter mini-carte
					mini_carte = plugins.MiniMap(toggle_display=True)
					carte.add_child(mini_carte)
					
					#Ajouter Zoom dans la mini-carte
					#plugins.ScrollZoomToggler().add_to(carte)


					# add layer control to show different maps
					folium.LayerControl(autoZIndex=True).add_to(carte) 

					#MESURE SUR LA CARTE
					carte.add_child(MeasureControl(position='bottomleft', primary_area_unit='hectares', secondary_area_unit='sqmeters', primary_length_unit='kilometers', secondary_length_unit='meters',))
					
					# AFFICHER LA CARTE DANS STREAMLIT
					folium_static(carte, width=1070, height=700)

			if page == "Carte de chaleur":

					carte = folium.Map(location=[7.3056, -5.3888], zoom_start=7, control_scale=True) 
					
					
					#st.dataframe(data=df_conflit, height=700)

					#df_conflit['Latitude'] = df_conflit['Latitude'].astype(float)
					#df_conflit['Longitude'] = df_conflit['Longitude'].astype(float)

					#df_conflit = df_conflit[['Latitude', 'Longitude']]
					#df_conflit = df_conflit.dropna(axis=0, subset=['Latitude','Longitude'])

					#CARTE DE CHALEUR
					heat_data = [[row.loc['Latitude'], row.loc['Longitude']] for index, row in df_conflit.iterrows()]

					HeatMap(heat_data, name="Carte de chaleur", radius=20).add_to(carte)


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