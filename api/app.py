import streamlit as st
from pygame import mixer

st.set_page_config(page_title="Interface de gestion de prédication", layout="wide")


title = "Interface de gestion de prédication"
st.title(title)
st.write("Bienvenue sur l'interface de gestion des prédications en ligne de l'ACY Port Bouet 2")
st.markdown("##")
# with st.container():
#     col1, col2,col3,col4 = st.columns((2,0.5,0.5,0.5))
#     with col3:
#         st.markdown("***Choose your genre:***")
#         genre = st.radio(
#             "",
#             "Test 2", index=[1, 2])
#     with col1:
#         st.markdown("***Choose features to customize:***")
#         start_year, end_year = st.slider(
#             'Select the year range',
#             1990, 2019, (2015, 2019)
#         )
#         acousticness = st.slider(
#             'Acousticness',
#             0.0, 1.0, 0.5)
#         danceability = st.slider(
#             'Danceability',
#             0.0, 1.0, 0.5)
#         energy = st.slider(
#             'Energy',
#             0.0, 1.0, 0.5)
#         instrumentalness = st.slider(
#             'Instrumentalness',
#             0.0, 1.0, 0.0)
#         valence = st.slider(
#             'Valence',
#             0.0, 1.0, 0.45)
#         tempo = st.slider(
#             'Tempo',
#             0.0, 244.0, 118.0)



# from google.oauth2 import service_account
# from google.cloud import storage

# Create API client.
# credentials = service_account.Credentials.from_service_account_info(
#     st.secrets["gcp_service_account"]
# )
# client = storage.Client(credentials=credentials)

mixer.init()

music = st.file_uploader("Ajouter une prédication ...")

try : 
    mixer.music.load(music)
except Exception : 
    st.write("Ajouter une prédication svp ...")

if st.button("Play") : 
    mixer.music.play()

if st.button("Pause") : 
    mixer.music.pause()
    
if st.button("Stop") : 
    mixer.music.stop()


