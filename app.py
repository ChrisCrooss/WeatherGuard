import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
import openai

st.set_page_config(page_title="WeatherGuard", layout="centered")

# CSS with help of AI
st.markdown("""
<style>
    /* Remove default padding/margins */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    /* Fix blank map container */
    .stDeployButton, .st-emotion-cache-1v0mbvd {
        min-height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Fix folium map blank space */
    .folium-map {
        height: 500px !important;
        width: 100% !important;
        min-height: unset !important;
    }
    
    /* Remove empty column spaces */
    [data-testid="column"] {
        padding: 0 !important;
        margin: 0 !important;
        gap: 0 !important;
    }
    
    /* Fix form container spacing */
    [data-testid="stForm"] {
        padding: 0;
        border: none;
    }
    
    /* Button container fix */
    .stButton>button {
        margin: 0.5rem 0;
    }
    
    /* Remove default Streamlit header/footer space */
    header {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
st.title("WeatherGuard")


# Language selection
lang = st.selectbox("Choose language", ["English", "Español" ,"Français","Deutsch" ], help="Select the language for the interface", label_visibility="visible", key="lang_select")

# Language input
lang_code = "en" if lang == "English" else "es" if lang == "Español" else "fr" if lang == "Français" else "de"
# Translations for input fields
translations_input = {
    "en": {
        "City Input": "Enter your city and country code (e.g., Quito,EC or Paris,FR):",
        "Job Type": "Select your work type:",
        "Job Types": ["Construction", "Farming", "Gardening", "Delivery", "Other"]
    },
    "es": {
        "City Input": "Ingresa tu ciudad y código de país (ejemplo: Quito,EC o Paris,FR):",
        "Job Type": "Selecciona tu tipo de trabajo:",
        "Job Types": ["Construcción", "Agricultura", "Jardinería", "Reparto", "Otro"]
    },
    "fr": {
        "City Input": "Entrez votre ville et le code pays (ex: Quito,EC ou Paris,FR):",
        "Job Type": "Sélectionnez votre type de travail:",
        "Job Types": ["Construction", "Agriculture", "Jardinage", "Livraison", "Autre"]
    },
    "de": {
        "City Input": "Geben Sie Ihre Stadt und den Ländercode ein (z.B. Quito,EC oder Paris,FR):",
        "Job Type": "Wählen Sie Ihre Arbeitsart:",
        "Job Types": ["Bau", "Landwirtschaft", "Gartenarbeit", "Lieferung", "Andere"]
    }
}
t_input = translations_input[lang_code]

# Input fields
location = st.text_input(t_input["City Input"], key="location_input")
job_type = st.selectbox(t_input["Job Type"], t_input["Job Types"], key="job_type_select")

# OpenWeatherMap API
if location:
    api_key = "66ea62058eaf1a752a7e2042ab1b61e7"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description']
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        wind_speed = data.get('wind', {}).get('speed', None)  
        icon_code = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

        # Languages
        translations = {
        "en": {
                "Weather Info": "📊 Weather Info",
                "Temperature": "**Temperature:**",
                "Humidity": "**Humidity:**",
                "Weather": "**Weather:**",
                "Wind Speed": "**Wind Speed:**",
                "Health Risk Level": "🚨 Health Risk Level",
                "Risk Level": "**Risk Level:**",
                "Safety Tips": "**Safety Tips:**",
                "Safety Checklist": "✅ Safety Checklist",
                "Location Map": "🗺️ Location Map",
                "Ask Advice": "Ask for safety advice (optional):",
                "City Error": "City not found or invalid format. Try 'Quito,EC' or 'Paris,FR'.",
                "Checklist": [
                    "Drink water regularly",
                    "Wear appropriate clothing",
                    "Take breaks as needed",
                    "Check weather updates",
                    "Inform someone of your location",
                    "Apply sunscreen",
                    "Wear waterproof boots",
                    "Secure loose items",
                    "Wear thermal layers"
                ],
                "Construction1": "🦺 Wear a helmet and high-visibility vest.",
                "Construction2": "🔨 Check tools and equipment before use.",
                "Construction3": "🚧 Be cautious around heavy machinery.",
                "Farming1": "🌾 Use gloves and sun protection.",
                "Farming2": "🚜 Stay hydrated and take breaks in the shade.",
                "Farming3": "🐝 Watch for insects and allergens.",
                "Gardening1": "🌱 Wear gloves and knee pads.",
                "Gardening2": "🧴 Apply sunscreen regularly.",
                "Gardening3": "💧 Drink water often.",
                "Delivery1": "🚲 Wear a helmet and reflective gear.",
                "Delivery2": "📱 Keep your phone charged for emergencies.",
                "Delivery3": "🗺️ Plan your route to avoid hazardous areas.",
                "Other1": "🛡️ Use appropriate protective gear.",
                "Other2": "🕶️ Protect yourself from sun and rain.",
                "Other3": "🧃 Take regular hydration breaks.",
                "GPT System": "You are a health and safety assistant for outdoor workers.",
                "City Input": "Enter your city and country code (e.g., Quito,EC or Paris,FR):",
                "Job Type": "Select your work type:"
            },
            "es": {
                "Weather Info": "📊 Información del clima",
                "Temperature": "**Temperatura:**",
                "Humidity": "**Humedad:**",
                "Weather": "**Clima:**",
                "Wind Speed": "**Velocidad del viento:**",
                "Health Risk Level": "🚨 Nivel de riesgo para la salud",
                "Risk Level": "**Nivel de riesgo:**",
                "Safety Tips": "**Consejos de seguridad:**",
                "Safety Checklist": "✅ Lista de verificación de seguridad",
                "Location Map": "🗺️ Mapa de ubicación",
                "Ask Advice": "Pregunta por consejos de seguridad (opcional):",
                "City Error": "Ciudad no encontrada o formato inválido. Prueba 'Quito,EC' o 'Paris,FR'.",
                "Checklist": [
                    "Bebe agua regularmente",
                    "Usa ropa adecuada",
                    "Toma descansos según sea necesario",
                    "Revisa actualizaciones del clima",
                    "Informa a alguien tu ubicación",
                    "Aplica protector solar",
                    "Usa botas impermeables",
                    "Asegura objetos sueltos",
                    "Usa ropa térmica"
                ],
                "Construction1": "🦺 Usa casco y chaleco de alta visibilidad.",
                "Construction2": "🔨 Revisa herramientas y equipos antes de usar.",
                "Construction3": "🚧 Ten cuidado cerca de maquinaria pesada.",
                "Farming1": "🌾 Usa guantes y protección solar.",
                "Farming2": "🚜 Mantente hidratado y toma descansos a la sombra.",
                "Farming3": "🐝 Ten cuidado con insectos y alérgenos.",
                "Gardening1": "🌱 Usa guantes y rodilleras.",
                "Gardening2": "🧴 Aplica protector solar regularmente.",
                "Gardening3": "💧 Bebe agua con frecuencia.",
                "Delivery1": "🚲 Usa casco y ropa reflectante.",
                "Delivery2": "📱 Mantén tu teléfono cargado para emergencias.",
                "Delivery3": "🗺️ Planifica tu ruta para evitar áreas peligrosas.",
                "Other1": "🛡️ Usa equipo de protección adecuado.",
                "Other2": "🕶️ Protégete del sol y la lluvia.",
                "Other3": "🧃 Toma descansos regulares para hidratarte.",
                "GPT System": "Eres un asistente de salud y seguridad para trabajadores al aire libre.",
                "City Input": "Ingresa tu ciudad y código de país (ejemplo: Quito,EC o Paris,FR):",
                "Job Type": "Selecciona tu tipo de trabajo:"
            },
            "fr": {
                "Weather Info": "📊 Informations météorologiques",
                "Temperature": "**Température:**",
                "Humidity": "**Humidité:**",
                "Weather": "**Météo:**",
                "Wind Speed": "**Vitesse du vent:**",
                "Health Risk Level": "🚨 Niveau de risque pour la santé",
                "Risk Level": "**Niveau de risque:**",
                "Safety Tips": "**Conseils de sécurité:**",
                "Safety Checklist": "✅ Liste de contrôle de sécurité",
                "Location Map": "🗺️ Carte de localisation",
                "Ask Advice": "Demandez des conseils de sécurité (facultatif):",
                "City Error": "Ville non trouvée ou format invalide. Essayez 'Quito,EC' ou 'Paris,FR'.",
                "Checklist": [
                    "Buvez de l'eau régulièrement",
                    "Portez des vêtements appropriés",
                    "Faites des pauses si nécessaire",
                    "Vérifiez les mises à jour météorologiques",
                    "Informez quelqu'un de votre emplacement",
                    "Appliquez de la crème solaire",
                    "Portez des bottes imperméables",
                    "Fixez les objets lâches",
                    "Portez des couches thermiques"
                ],
                "Construction1": "🦺 Portez un casque et un gilet haute visibilité.",
                "Construction2": "🔨 Vérifiez les outils et équipements avant utilisation.",
                "Construction3": "🚧 Soyez prudent autour des machines lourdes.",
                "Farming1": "🌾 Utilisez des gants et une protection solaire.",
                "Farming2": "🚜 Restez hydraté et faites des pauses à l'ombre.",
                "Farming3": "🐝 Faites attention aux insectes et aux allergènes.",
                "Gardening1": "🌱 Portez des gants et des genouillères.",
                "Gardening2": "🧴 Appliquez régulièrement de la crème solaire.",
                "Gardening3": "💧 Buvez souvent de l'eau.",
                "Delivery1": "🚲 Portez un casque et des vêtements réfléchissants.",
                "Delivery2": "📱 Gardez votre téléphone chargé pour les urgences.",
                "Delivery3": "🗺️ Planifiez votre itinéraire pour éviter les zones dangereuses.",
                "Other1": "🛡️ Utilisez un équipement de protection approprié.",
                "Other2": "🕶️ Protégez-vous du soleil et de la pluie.",
                "Other3": "🧃 Faites des pauses régulières pour vous hydrater.",
                "GPT System": "Vous êtes un assistant de santé et de sécurité pour les travailleurs en plein air.",
                "City Input": "Entrez votre ville et le code pays (ex: Quito,EC ou Paris,FR):",
                "Job Type": "Sélectionnez votre type de travail:"
            },
            "de": {
                "Weather Info": "📊 Wetterinformationen",
                "Temperature": "**Temperatur:**",
                "Humidity": "**Luftfeuchtigkeit:**",
                "Weather": "**Wetter:**",
                "Wind Speed": "**Windgeschwindigkeit:**",
                "Health Risk Level": "🚨 Gesundheitsrisikostufe",
                "Risk Level": "**Risikostufe:**",
                "Safety Tips": "**Sicherheitstipps:**",
                "Safety Checklist": "✅ Sicherheitscheckliste",
                "Location Map": "🗺️ Standortkarte",
                "Ask Advice": "Fragen Sie nach Sicherheitstipps (optional):",
                "City Error": "Stadt nicht gefunden oder ungültiges Format. Versuchen Sie 'Quito,EC' oder 'Paris,FR'.",
                "Checklist": [
                    "Regelmäßig Wasser trinken",
                    "Geeignete Kleidung tragen",
                    "Pausen nach Bedarf einlegen",
                    "Wetter-Updates überprüfen",
                    "Jemanden über Ihren Standort informieren",
                    "Sonnencreme auftragen",
                    "Wasserdichte Stiefel tragen",
                    "Lose Gegenstände sichern",
                    "Thermische Schichten tragen"
                ],
                "Construction1": "🦺 Tragen Sie einen Helm und eine Warnweste.",
                "Construction2": "🔨 Überprüfen Sie Werkzeuge und Ausrüstung vor Gebrauch.",
                "Construction3": "🚧 Seien Sie vorsichtig in der Nähe von schweren Maschinen.",
                "Farming1": "🌾 Tragen Sie Handschuhe und Sonnenschutz.",
                "Farming2": "🚜 Bleiben Sie hydratisiert und machen Sie Pausen im Schatten.",
                "Farming3": "🐝 Achten Sie auf Insekten und Allergene.",
                "Gardening1": "🌱 Tragen Sie Handschuhe und Knieschützer.",
                "Gardening2": "🧴 Tragen Sie regelmäßig Sonnencreme auf.",
                "Gardening3": "💧 Trinken Sie oft Wasser.",
                "Delivery1": "🚲 Tragen Sie einen Helm und reflektierende Kleidung.",
                "Delivery2": "📱 Halten Sie Ihr Telefon für Notfälle aufgeladen.",
                "Delivery3": "🗺️ Planen Sie Ihre Route, um gefährliche Bereiche zu vermeiden.",
                "Other1": "🛡️ Verwenden Sie geeignete Schutzausrüstung.",
                "Other2": "🕶️ Schützen Sie sich vor Sonne und Regen.",
                "Other3": "🧃 Machen Sie regelmäßig Pausen zur Hydratation.",
                "GPT System": "Sie sind ein Gesundheits- und Sicherheitsassistent für Außenarbeiter.",
                "City Input": "Geben Sie Ihre Stadt und den Ländercode ein (z.B. Quito,EC oder Paris,FR):",
                "Job Type": "Wählen Sie Ihre Arbeitsart:"
            }
        }

        lang_code = "en" if lang == "English" else "es" if lang == "Español" else "fr" if lang == "Français" else "de" if lang == "Deutsch" else "es"
        t = translations[lang_code]


        st.subheader(t["Weather Info"])
        st.write(f"{t['Temperature']} {temp}°C")
        st.write(f"{t['Humidity']} {humidity}%")
        st.write(f"{t['Weather']} {weather_desc.capitalize()}")
        st.write(f"{t['Wind Speed']} {wind_speed} m/s" if wind_speed else "")
        st.image(icon_url, caption=weather_desc.capitalize())

        # Risk
        risk_level = "Low"
        tips = []

        # levels
        if temp >= 35:
            risk_level = "Extreme"
            tips.append("🚨 Avoid working during peak heat hours. Seek shade and rest often.")
        elif temp >= 32 and humidity >= 60:
            risk_level = "High"
            tips.append("⚠️ Take frequent breaks in the shade. Drink plenty of water. Wear lightweight clothing.")
        elif temp >= 28 and humidity >= 50:
            risk_level = "Moderate"
            tips.append("☀️ Use sun protection, stay cool, and hydrate often.")

        if humidity >= 95 and "rain" in weather_desc.lower():
            risk_level = max(risk_level, "Moderate", key=lambda x: ["Low","Moderate","High","Extreme"].index(x))
            tips.append("🌧️ High humidity and rain can make surfaces slippery. Wear shoes with grip and watch your footing.")

        if temp < 10:
            risk_level = max(risk_level, "Moderate", key=lambda x: ["Low","Moderate","High","Extreme"].index(x))
            tips.append("🥶 Cold weather increases risk of fatigue. Wear warm waterproof clothing and stay dry.")

        if wind_speed and wind_speed > 10:
            risk_level = max(risk_level, "High", key=lambda x: ["Low","Moderate","High","Extreme"].index(x))
            tips.append("💨 Strong winds: Secure loose items and wear wind-resistant clothing.")

        # advice for each job type
        job_advices = {
            "Construction": [
                t.get("Construction1", "🦺 Wear a helmet and high-visibility vest."),
                t.get("Construction2", "🔨 Check tools and equipment before use."),
                t.get("Construction3", "🚧 Be cautious around heavy machinery.")
            ],
            "Farming": [
                t.get("Farming1", "🌾 Use gloves and sun protection."),
                t.get("Farming2", "🚜 Stay hydrated and take breaks in the shade."),
                t.get("Farming3", "🐝 Watch for insects and allergens.")
            ],
            "Gardening": [
                t.get("Gardening1", "🌱 Wear gloves and knee pads."),
                t.get("Gardening2", "🧴 Apply sunscreen regularly."),
                t.get("Gardening3", "💧 Drink water often.")
            ],
            "Delivery": [
                t.get("Delivery1", "🚲 Wear a helmet and reflective gear."),
                t.get("Delivery2", "📱 Keep your phone charged for emergencies."),
                t.get("Delivery3", "🗺️ Plan your route to avoid hazardous areas.")
            ],
            "Other": [
                t.get("Other1", "🛡️ Use appropriate protective gear."),
                t.get("Other2", "🕶️ Protect yourself from sun and rain."),
                t.get("Other3", "🧃 Take regular hydration breaks.")
            ]
        }

        job_type_map = {
            "Construction": "Construction", "Construcción": "Construction", "Construction": "Construction", "Bau": "Construction",
            "Farming": "Farming", "Agricultura": "Farming", "Agriculture": "Farming", "Landwirtschaft": "Farming",
            "Gardening": "Gardening", "Jardinería": "Gardening", "Jardinage": "Gardening", "Gartenarbeit": "Gardening",
            "Delivery": "Delivery", "Reparto": "Delivery", "Livraison": "Delivery", "Lieferung": "Delivery",
            "Other": "Other", "Otro": "Other", "Autre": "Other", "Andere": "Other"
        }
        job_type_en = job_type_map.get(job_type, "Other")
        tips.extend(job_advices.get(job_type_en, []))


        st.subheader(t["Health Risk Level"])
        st.markdown(f"{t['Risk Level']} `{risk_level}`")
        st.markdown(t["Safety Tips"])
        for tip in tips:
            st.markdown(f"- {tip}")

        # Safety Checklist
        st.subheader(t["Safety Checklist"])
        checklist = t["Checklist"][:5]
        if temp >= 30:
            checklist.append(t["Checklist"][5])
        if "rain" in weather_desc.lower():
            checklist.append(t["Checklist"][6])
        if wind_speed and wind_speed > 10:
            checklist.append(t["Checklist"][7])
        if temp < 10:
            checklist.append(t["Checklist"][8])

        for item in checklist:
            st.checkbox(item, value=False, key=item)

        # Map
        st.subheader(t["Location Map"])
        if "map_zoom" not in st.session_state:
            st.session_state["map_zoom"] = 12
        if "map_center" not in st.session_state:
            st.session_state["map_center"] = [lat, lon]

        m = folium.Map(location=st.session_state["map_center"], zoom_start=st.session_state["map_zoom"])
        folium.Marker([lat, lon], popup=location).add_to(m)
        map_data = st_folium(m, width=700, height=500)

        if map_data and "zoom" in map_data and "center" in map_data:
            center = map_data["center"]
            if isinstance(center, dict):
                st.session_state["map_center"] = [center["lat"], center["lng"]]
            else:
                st.session_state["map_center"] = center
            st.session_state["map_zoom"] = map_data["zoom"]

        # GPT Chat (in process)
        openai.api_key = ""
        user_question = st.text_input(t["Ask Advice"], "")
        if user_question:
            try:
                response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": t["GPT System"]},
                        {"role": "user", "content": user_question}
                    ]
                )
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"OpenAI API error: {e}")
    else:
        st.error(t["City Error"])

    # Severe weather alert
    if temp >= 35 or "storm" in weather_desc.lower():
        st.warning("⚠️ " + t.get("Severe Weather", "Severe weather alert! Take extra precautions."))

    # Feedback
    feedback = st.text_area("Feedback / Sugerencias / Rückmeldung / Retour d'information")
    if feedback:
        st.success("Thank you for your feedback!")
