import streamlit as st
import random
import re

def generate_sequence():
    m = random.randint(1, 7)
    seed1 = random.randint(1, 15)
    seed2 = random.randint(1, 15)
    A = random.randint(-2, 2)
    B = random.randint(1, 2)
    C = random.randint(-1, 1)
    X = random.randint(1, 5)
    Y = random.randint(1, 5)
    Z = random.randint(-15, 15)
    K = list(range(1, 11)) 

    if m == 1:
        method = "Odd-Even"
        seq = [X + ((k + A) // B) if k % 2 == 1 else Y + ((k + A) // B) for k in K]
        formula_latex = r"a_n = \begin{cases} X + \left\lfloor \dfrac{n + A}{B} \right\rfloor & \text{if } n \text{ is odd} \\ Y + \left\lfloor \dfrac{n + A}{B} \right\rfloor & \text{if } n \text{ is even} \end{cases}"
        
    elif m == 2:
        method = "Recursive"
        seq = [seed1 + A, seed2 + A]
        for i in range(2, 10):
            next_term = seq[i-2] + seq[i-1] + A
            seq.append(next_term)
        formula_latex = r"a_n = a_{n-2} + a_{n-1} + A"
        
    elif m == 3:
        method = "Position-based"
        seq = [X*k + Y for k in K]
        formula_latex = r"a_n = X \cdot n + Y"
        
    elif m == 4:
        method = "Digit dependent"
        def sum_of_digits(n):
            return sum(int(digit) for digit in str(n))
        seq = [seed1]
        for i in range(9):
            next_term = seq[-1] + sum_of_digits(seq[-1]) + A
            seq.append(next_term)
        formula_latex = r"a_n = a_{n-1} + S(a_{n-1}) + A \text{ where } S(m) \text{ is the sum of digits of } m"
        
    elif m == 5:
        method = "Geometric"
        seq = [seed1, seed2]
        for i in range(2, 10):
            next_term = seq[i-2] * X + seq[i-1] * B
            seq.append(next_term)
        formula_latex = r"a_n = X \cdot a_{n-2} + B \cdot a_{n-1}"
        
    elif m == 6:
        method = "Perfect power"
        seq = [(k + X) ** 2 for k in K]  # Fixed: ^ to **
        formula_latex = r"a_n = (n + X)^2"
        
    elif m == 7:
        method = "Geometric-arithmetic"
        seq = [seed1]
        for i in range(2, 10):
            next_term = seq[i-2] * X + Y
            seq.append(next_term)
        formula_latex = r"a_n = X \cdot a_{n-2} + Y"

    # Replace variables in formula with actual values
    formula_latex = formula_latex.replace("A", str(A))
    formula_latex = formula_latex.replace("B", str(B))
    formula_latex = formula_latex.replace("X", str(X))
    formula_latex = formula_latex.replace("Y", str(Y))
    
    return {
        'method': method,
        'sequence': seq,
        'formula_latex': formula_latex,
        'variables': {'A': A, 'B': B, 'X': X, 'Y': Y}
    }

def main():
    st.set_page_config(page_title="Sequence Guessing Game", layout="centered")
    
    st.title("Sequence")
    st.markdown("Guess the next numbers in the sequence!")
    
    # Initialize session state
    if 'game_data' not in st.session_state:
        st.session_state.game_data = generate_sequence()
        st.session_state.current_guess = 7  # Start guessing term 7
        st.session_state.show_hint = False
        st.session_state.game_over = False
        st.session_state.gave_up = False
        st.session_state.correct_guesses = 0
        st.session_state.display_sequence = []  # To show progressively revealed sequence
    
    # Initialize display sequence with first 6 terms
    seq = st.session_state.game_data['sequence']
    if not st.session_state.display_sequence:
        st.session_state.display_sequence = seq[:6].copy()
    
    # Display current sequence (shows progressively revealed terms)
    st.subheader("Sequence:")
    display_text = ", ".join(map(str, st.session_state.display_sequence))
    if st.session_state.current_guess <= 8:  # Only show ? for remaining terms if not all guessed
        display_text += ", ?, ?"
    st.write(f"**{display_text}**")
    
    # Game status - only need to guess 2 numbers
    remaining_guesses = 2 - st.session_state.correct_guesses
    if remaining_guesses > 0 and not st.session_state.game_over:
        st.write(f"**Guess term #{st.session_state.current_guess}** ({remaining_guesses} more to win)")
    
    # Input for guessing
    if not st.session_state.game_over and st.session_state.current_guess <= 8:
        guess = st.number_input("Enter your guess:", step=1, format="%d", key="guess_input")
    else:
        guess = 0
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Check") and not st.session_state.game_over and st.session_state.current_guess <= 8:
            if guess == seq[st.session_state.current_guess - 1]:
                st.success("Yuppp")
                # Add correct guess to display sequence
                st.session_state.display_sequence.append(seq[st.session_state.current_guess - 1])
                st.session_state.current_guess += 1
                st.session_state.correct_guesses += 1
                
                # Check if player won (guessed 2 terms correctly)
                if st.session_state.correct_guesses >= 2:
                    st.session_state.game_over = True
                    st.balloons()
                    st.success("Niceeeeeeeeeeeeeeee")
            else:
                st.error("Nah. Try again.")
    
    with col2:
        if not st.session_state.show_hint and not st.session_state.game_over and st.session_state.current_guess <= 8:
            if st.button("Show Next Term"):
                st.session_state.show_hint = True
                st.info(f"Term #{st.session_state.current_guess} is: **{seq[st.session_state.current_guess - 1]}**")
                # Add revealed term to display sequence
                st.session_state.display_sequence.append(seq[st.session_state.current_guess - 1])
                st.session_state.current_guess += 1
                # Player needs to guess the remaining terms
                st.session_state.correct_guesses = max(0, st.session_state.correct_guesses - 1)  # Penalty for using hint
    
    with col3:
        if st.button("I'm dumb so I give up") and not st.session_state.game_over:
            st.session_state.game_over = True
            st.session_state.gave_up = True
            st.warning("You gave up! Here's the solution:")
    
    # Display formula when game is over
    if st.session_state.game_over:
        st.markdown("---")
        st.subheader("Sequence Formula")
        st.latex(st.session_state.game_data['formula_latex'])
        
        st.subheader("Full Sequence")
        full_seq = st.session_state.game_data['sequence']
        st.write(f"**{', '.join(map(str, full_seq))}**")
        
        if st.button("New Game"):
            # Reset game state
            st.session_state.game_data = generate_sequence()
            st.session_state.current_guess = 7
            st.session_state.show_hint = False
            st.session_state.game_over = False
            st.session_state.gave_up = False
            st.session_state.correct_guesses = 0
            st.session_state.display_sequence = []
            st.rerun()
    

if __name__ == "__main__":
    main()
