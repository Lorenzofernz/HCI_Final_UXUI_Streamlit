import streamlit as st
import requests
import pandas as pd
import plotly.express as px




st.set_page_config(

    page_title= "OSRS HighScores API",
    # layout= "wide",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/',
        'Report a bug':  "http://localhost:8501",
        'About': '# Welcome to OSRS Live HighScores. Final HCI UX/UI Design Streamlit project developed by Lorenzo Fernandez'


    }

    )

st.title('Streamlit OSRS HighScores API')


add_selectbox = st.sidebar.selectbox(
    "Select an option",
    ["Homepage", "OSRS Personal HighScores", "OSRS Compare HighScores"]
)


if add_selectbox == "OSRS Personal HighScores":
    st.title("OSRS Personal HighScores")


    def experience_to_level(experience):
        level = 1
        points = 0
        for lvl in range(1, 100):
            points += int(lvl + 300 * 2 ** (lvl / 7.0))
            level = lvl
            if points // 4 > experience:
                break
        return level


    def fetch_player_data(player_name):
        url = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={player_name}"
        response = requests.get(url)

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            data = response.text.split("\n")  # Split the response into lines

            # Dictionary to store the data
            player_data = {}
            for i, activity in enumerate(activities):
                activity_data = data[i].split(",")
                level = experience_to_level(int(activity_data[2]))
                player_data[activity] = level

            return player_data
        else:
            st.write(f"Error: {response.status_code} - {response.text}")
            return None


    if __name__ == "__main__":
        player_name = st.text_input("Enter Player UserName:")
        activities = ["attack", "defense", "strength", "hitpoints", "ranged", "prayer", "magic",
                      "cooking", "woodcutting", "fletching", "fishing", "firemaking", "crafting", "smithing",
                      "mining", "herblore", "agility", "thieving", "slayer", "farming", "runecrafting", "hunter",
                      "construction"]

        fetch_data = st.button("Fetch Player Data")

        if fetch_data:
            player_data = fetch_player_data(player_name)

            if player_data:
                st.write("**Player Data:**", unsafe_allow_html=True)
                st.write(f"**Player Name:** {player_name}")
                st.success("Player data has been found!")

                # DataFrame for the bar chart
                chart_data = pd.DataFrame(list(player_data.items()), columns=['Activity', 'Level'])

                # Vertical bar chart with activities on X-axis and levels on Y-axis
                st.bar_chart(chart_data.set_index('Activity'), use_container_width=True)




elif add_selectbox == "OSRS Compare HighScores":
    st.title("Compare Player's HighScores")

    def experience_to_level(experience):
        level = 1
        points = 0
        for lvl in range(1, 100):
            points += int(lvl + 300 * 2 ** (lvl / 7.0))
            level = lvl
            if points // 4 > experience:
                break
        return level


    def fetch_player_data(player_name):
        url = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={player_name}"
        response = requests.get(url)

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            data = response.text.split("\n")  # Split the response into lines

            # Dictionary to store the data
            player_data = {}
            for i, activity in enumerate(activities):
                activity_data = data[i].split(",")
                level = experience_to_level(int(activity_data[2]))
                player_data[activity] = level

            return player_data
        else:
            st.write(f"Error: {response.status_code} - {response.text}")
            return None

    if __name__ == "__main__":
        # player_name = st.text_input("Enter Player UserName:")
        activities = ["attack", "defense", "strength", "hitpoints", "ranged", "prayer", "magic",
                      "cooking", "woodcutting", "fletching", "fishing", "firemaking", "crafting", "smithing",
                      "mining", "herblore", "agility", "thieving", "slayer", "farming", "runecrafting", "hunter",
                      "construction"]

        player1_name = st.text_input("Enter Player 1 UserName:")
        player2_name = st.text_input("Enter Player 2 UserName:")

        fetch_data = st.button("Fetch Player Data")

        if fetch_data:
            player1_data = fetch_player_data(player1_name)
            player2_data = fetch_player_data(player2_name)

            if player1_data:
                st.success(f"Player 1 data has been found for {player1_name}!")

            if player2_data:
                st.success(f"Player 2 data has been found for {player2_name}!")

            if player1_data and player2_data:
                # Create DataFrames for both players
                player1_df = pd.DataFrame(list(player1_data.items()), columns=['Activity', 'Player 1 Level'])
                player2_df = pd.DataFrame(list(player2_data.items()), columns=['Activity', 'Player 2 Level'])

                # Merge the DataFrames on the 'Activity' column
                merged_df = pd.merge(player1_df, player2_df, on='Activity')

                # Display a line chart to compare levels
                fig = px.line(merged_df, x='Activity', y=['Player 1 Level', 'Player 2 Level'],
                              title=f'Comparison of OSRS Highscores', labels={'value': 'Experience'})
                st.plotly_chart(fig)





else:
    st.subheader("Homepage")
    st.write("Welcome to my web application by Lorenzo Fernandez. "
             "This web app is based on an online MMORPG game called Old School Runescape. "
             "It is a game that I enjoy playing on my free time and love work on a theme related application recreationally.")
    st.info("Use the select box on the left hand to search up any OSRS player's data to display their stats with a visual bar graph, or to compare two different users in a line graph!")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    sliders = st.slider
    if sliders:
        st.info("User app rating slider")
        rate = st.slider("Please rate your experience with this web app!", 0,10,5)
        if  rate > 4:
                st.success("Thanks for using this wep app!")
        elif rate < 5:
                st.error("Sorry you didn't enjoy the app...")
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
            """
            <div style="text-align: center; font-size: 12px; color: gray;">
                © 2023 Streamlit OSRS HighScores API. All rights reserved. | Disclaimer: This web application is not affiliated with or endorsed by Jagex Ltd. "Old School RuneScape" and "OSRS" are trademarks of Jagex Ltd. All content related to the game is the property of Jagex Ltd. Use of the game's name, logo, or content is solely for descriptive and informational purposes. For official OSRS information, please visit www.runescape.com.
    
            </div>
            """,
            unsafe_allow_html=True
        )




