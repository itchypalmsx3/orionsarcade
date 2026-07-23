import streamlit as st
import random

# App Config
st.set_page_config(page_title="Orion's Arcade", page_icon="🎮")

# Sidebar Menu for Game Selection
st.sidebar.title("🎮 Orion's Arcade")
game_choice = st.sidebar.radio("Choose a game:", [
    "🎯 Number Guessing", 
    "🪙 Coin Toss", 
    "✊ Rock, Paper, Scissors",
    "🎲 Dice Roller",
    "🎱 Magic 8-Ball"
])

# ---------------------------------------------------------
# GAME 1: NUMBER GUESSING GAME
# ---------------------------------------------------------
if game_choice == "🎯 Number Guessing":
    st.title("🎯 Number Guessing Game")
    st.write("Guess a number between 1 and 10!")

    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 10)

    guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)

    if st.button("Submit Guess"):
        if guess == st.session_state.secret_number:
            st.balloons()
            st.success(f"🎉 WOW! You got it right! The number was {st.session_state.secret_number}.")
        else:
            st.error("❌ Oops! Try again!")

    if st.button("Reset Game"):
        st.session_state.secret_number = random.randint(1, 10)
        st.rerun()

# ---------------------------------------------------------
# GAME 2: COIN TOSS
# ---------------------------------------------------------
elif game_choice == "🪙 Coin Toss":
    st.title("🪙 Coin Toss Game")
    st.write("Predict the outcome and flip the coin!")

    user_choice = st.radio("Heads or Tails?", ["Heads", "Tails"])

    if st.button("Flip Coin"):
        outcome = random.choice(["Heads", "Tails"])
        st.write(f"The coin landed on **{outcome}**!")

        if user_choice == outcome:
            st.balloons()
            st.success("🎉 You predicted correctly!")
        else:
            st.error("❌ Tough luck! Try again.")

# ---------------------------------------------------------
# GAME 3: ROCK, PAPER, SCISSORS
# ---------------------------------------------------------
elif game_choice == "✊ Rock, Paper, Scissors":
    st.title("✊ Rock, Paper, Scissors")

    player_move = st.selectbox("Pick your move:", ["Rock", "Paper", "Scissors"])

    if st.button("Play!"):
        bot_move = random.choice(["Rock", "Paper", "Scissors"])
        st.write(f"You played **{player_move}** | Computer played **{bot_move}**")

        if player_move == bot_move:
            st.info("🤝 It's a tie!")
        elif (player_move == "Rock" and bot_move == "Scissors") or \
             (player_move == "Paper" and bot_move == "Rock") or \
             (player_move == "Scissors" and bot_move == "Paper"):
            st.balloons()
            st.success("🎉 You win!")
        else:
            st.error("❌ Computer wins!")

# ---------------------------------------------------------
# GAME 4: DICE ROLLER
# ---------------------------------------------------------
elif game_choice == "🎲 Dice Roller":
    st.title("🎲 High Roller Dice Game")
    st.write("Roll two dice and try to roll higher than the computer!")

    if st.button("Roll the Dice!"):
        user_roll = random.randint(1, 6) + random.randint(1, 6)
        bot_roll = random.randint(1, 6) + random.randint(1, 6)

        st.write(f"🎲 **Your Total:** {user_roll}")
        st.write(f"🤖 **Computer Total:** {bot_roll}")

        if user_roll > bot_roll:
            st.balloons()
            st.success("🎉 You beat the computer!")
        elif user_roll < bot_roll:
            st.error("❌ Computer won this round!")
        else:
            st.info("🤝 It's a tie!")

# ---------------------------------------------------------
# GAME 5: MAGIC 8-BALL
# ---------------------------------------------------------
elif game_choice == "🎱 Magic 8-Ball":
    st.title("🎱 Magic 8-Ball")
    st.write("Ask the Magic 8-Ball a yes-or-no question!")

    question = st.text_input("What is your question?")

    if st.button("Ask 8-Ball"):
        if question.strip() != "":
            responses = [
                "Yes, definitely! ✨",
                "Most likely! 👍",
                "Ask again later... 🤔",
                "Cannot predict now 🔮",
                "Don't count on it! ❌",
                "My sources say no 🛑"
            ]
            st.subheader(f"🎱 Answer: {random.choice(responses)}")
        else:
            st.warning("Please type a question first!")
