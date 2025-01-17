import streamlit as st
from pymongo import MongoClient
import datetime
import streamlit.components.v1 as components
def main():
    # MongoDB setup
    username = "ocramayora"
    password = "Arsic969!"
    cluster_address = "cluster0.ckteqa9.mongodb.net"
    connection_string = f"mongodb+srv://{username}:{password}@{cluster_address}/?retryWrites=true&w=majority"

    try:
        client = MongoClient(connection_string)
        db = client["copa_piston"]
        collection = db["daily_points"]
        st.success("Connected to MongoDB successfully!")
    except Exception as e:
        st.error(f"Failed to connect to MongoDB: {e}")

    st.title("Registrar Puntos Diarios 📋")

    participants = [
        "Alvarito", "Marco", "Xavi", "Suja", "Joel", "Monta", "Perez", "Cater", "Juan", "Jordi", "Folch"
    ]

    participant = st.selectbox("Selecciona tu nombre", participants)

    st.subheader("Sistema de Puntos")

    points = {
        "Cubata": 3, "Chupito": 1, "Cerveza": 1, "Zumito/agua": 1, "Llegar a casa a + de las 7:00": 1,
        "Lio": 3, "Pico": 2, "Sexo novia": 5, "Sexo el resto": 10, "Trio": 15,
        "Pico entre nosotros": -1, "Menor": -5, "Potar": -3, "Poner cuernos": -15, "Drogas duras": -5,
        "Deporte": 3, "Hacerse a una ex o alguien a quien has querido mucho (preguntar) sino DESCALIFICADO DIRECTO": 0
    }

    # Add a number input for each activity
    accomplishments = {task: st.number_input(task, min_value=0, step=1, value=0) for task in points}

    if st.button("Enviar"):
        # Calculate the total points
        total_points = sum(points[task] * accomplishments[task] for task in accomplishments if accomplishments[task] > 0)

        # Get the current date and time
        current_date = datetime.datetime.now()

        data = {
            "participant": participant,
            "date": current_date,  # Store the current date and time
            "points": total_points,
            "details": accomplishments  # Store the number of times each task was performed
        }
        collection.insert_one(data)
        st.success("¡Puntos registrados exitosamente!")

    # Custom CSS for additional styling
    # st.markdown(
    #     """
    #     <style>
    #     .stApp {
    #         background-color: #222222;
    #         color: #ffffff;
    #     }
    #     .stApp header {
    #         background: rgba(0, 0, 0, 0.7);
    #         padding: 10px;
    #         border-radius: 10px;
    #     }
    #     .stApp footer {
    #         background: rgba(0, 0, 0, 0.7);
    #         padding: 10px;
    #         border-radius: 10px;
    #         text-align: center;
    #     }
    #     .stMarkdownContainer p {
    #         text-align: justify;
    #         text-justify: inter-word;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )

if __name__ == "__main__":
    main()
