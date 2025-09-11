import streamlit as st
import decimal
import streamlit.components.v1 as components
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="Final Exam", layout="centered")
st.title("Final Exam")
st.header("Student Information")

# Student Info
class_options = ["3/11", "3/12"]
selected_class = st.selectbox("Select your class:", class_options)
nickname = st.text_input("Nickname")
student_number = st.text_input("Student Number")

# ========== PART I: Sudoku Puzzle ==========
st.header("PART I: Sudoku Puzzle (4pts)")
st.write("**Instruction:** Solve the following Sudoku puzzles using the numbers 1 to 6 for No.1, and 1 to 9 for No.2")

puzzle6 = st.secrets["sudoku6"]["puzzle"]
solution6 = st.secrets["sudoku6"]["solution"]

puzzle9 = st.secrets["sudoku9"]["puzzle"]
solution9 = st.secrets["sudoku9"]["solution"]

# Sudoku Components
sudoku6 = components.declare_component("sudoku6x6", path="sudoku_component")
sudoku9 = components.declare_component("sudoku9x9", path="sudoku_component2")

st.write("1. Solve the following 6x6 Sudoku.")
board6 = sudoku6(key="sudoku6")

st.write("2. Solve the following 9x9 Sudoku.")
board9 = sudoku9(key="sudoku9")

# ========== PART II: Counting Combinations ==========
st.header("PART II: Counting Combinations (2pts)")
st.write("**Instruction:** Given the problem below, answer the following questions.")
st.markdown("""
Suppose that the four character code has the following restrictions:
- Numbers and letters
- Uppercase letters only (lowercase is not allowed)
- Cannot repeat characters
""")
st.image("4ch.png")

st.write("3. What characters can make up the code?")
q3 = st.radio("**3. What characters can make up the code?**", [
    "a. 10 numbers",
    "b. 26 letters",
    "c. 10 numbers and 26 letters",
    "d. 10 numbers and 52 letters"
], key="q3", label_visibility="collapsed")

st.write("4. How many possible numbers and letters are there for the **first** character of the code?")
q4 = st.radio("**4. How many possible numbers and letters are there for the first character of the code?**", [
    "a. 36 possible letters and numbers",
    "b. 62 possible letters and numbers",
    "c. 33 possible letters and numbers",
    "d. 59 possible letters and numbers"
], key="q4", label_visibility="collapsed")

st.write("5. How many possible numbers and letters are there for the **fourth** character of the code?")
q5 = st.radio("**5. How many possible numbers and letters are there for the fourth character of the code?**", [
    "a. 36 possible letters and numbers",
    "b. 58 possible letters and numbers",
    "c. 33 possible letters and numbers",
    "d. 59 possible letters and numbers"
], key="q5", label_visibility="collapsed")

st.write("6. How many different code combinations are possible given the statement above?")
q6 = st.radio("**6. How many different code combinations are possible given the statement above?**", [
    "a. 44,261,653,680 possible combinations",
    "b. 916,132,832 possible combinations",
    "c. 776,520,240 possible combinations",
    "d. 1,413,720 possible combinations"
], key="q6", label_visibility="collapsed")

# ========== PART III: Greatest Common Factor ==========
st.header("PART III: Greatest Common Factor (5pts)")
st.write("**Instruction:** Solve the following problems.")

# def gcf_input(q_num, prompt):
#     st.write(f"{q_num}. {prompt}")
#     return st.text_input(f"Answer", key=f"gcf_{q_num}", label_visibility="collapsed")

# gcf7 = gcf_input(7, "Find the GCF of **35**, **28** using the **factorization** method.")
# gcf8 = gcf_input(8, "Find the GCF of **33**, **36** using the **factorization** method.")
# gcf9 = gcf_input(9, "Find the GCF of **10**, **45** using the **subtraction** method.")
# gcf10 = gcf_input(10, "Find the GCF of **30**, **6** using the **subtraction** method.")

gcf7_factors_35 = st.secrets["gcf"]["gcf7_factors_35"]
gcf7_factors_28 = st.secrets["gcf"]["gcf7_factors_28"]
gcf7 = st.secrets["gcf"]["gcf7"]

gcf8_factors_33 = st.secrets["gcf"]["gcf8_factors_33"]
gcf8_factors_36 = st.secrets["gcf"]["gcf8_factors_36"]
gcf8 = st.secrets["gcf"]["gcf8"]

# Q7
st.write(f"7. Find the GCF of **35**, **28** using the **factorization** method.")
factors_35 = st.text_input("Factors of 35 (comma separated):", key="factors_35", placeholder="e.g., 1, 5...")
factors_28 = st.text_input("Factors of 28 (comma separated):", key="factors_28", placeholder="e.g., 1, 2...")

# GCF answer input for Q7
gcf7_input = st.text_input("What is the GCF of 35 and 28?", key="gcf7_input", placeholder="Enter the GCF value")

# Q8
st.write("")
st.write("")
st.write(f"8. Find the GCF of **33**, **36** using the **factorization** method.")
factors_33 = st.text_input("Factors of 33 (comma separated):", key="factors_33", placeholder="e.g., 1, 3...")
factors_36 = st.text_input("Factors of 36 (comma separated):", key="factors_36", placeholder="e.g., 1, 2...")

# GCF answer input for Q8
gcf8_input = st.text_input("What is the GCF of 33 and 36?", key="gcf8_input", placeholder="Enter the GCF value")

# ========== Grading Functions ==========
def grade_factors(factors_str, correct_factors):
    # Clean the input
    factors = [int(x.strip()) for x in factors_str.split(",") if x.strip().isdigit()]
    correct_factors = set(correct_factors)
    
    # Check if all the entered factors are correct
    if set(factors) == correct_factors:
        return 1  # Full points if the factors are correct
    else:
        return 0  # No points if the factors are incorrect

def grade_numeric(q_key, expected):
    try:
        ans = st.session_state.get(q_key, "")
        if ans is None or ans == "":
            return 0.0
        student_val = float(str(ans).strip())
        return 1.0 if student_val == expected else 0.0
    except:
        return 0.0

# Q9

st.write("")
st.write("")
st.write("9. Find the GCF of **10**, **45** using the **subtraction** method.")

if "sub_steps_q9" not in st.session_state:
    st.session_state.sub_steps_q9 = []

if "input_error_q9" not in st.session_state:
    st.session_state.input_error_q9 = ""

def add_sub_step_q9():
    raw = st.session_state.sub_input_q9.strip()
    try:
        num, den = map(int, raw.split("-"))
        st.session_state.sub_steps_q9.append(f"{num} - {den} = {num - den}")
        st.session_state.sub_input_q9 = ""
        st.session_state.input_error_q9 = ""
    except:
        st.session_state.input_error_q9 = "❌ Invalid format. Use e.g., 45-10"

def remove_last_sub_step_q9():
    if st.session_state.sub_steps_q9:
        st.session_state.sub_steps_q9.pop()

# Show current steps
for step in st.session_state.sub_steps_q9:
    st.text(step)

# Input and buttons
st.text_input("Type a subtraction step (e.g., 45-10)", key="sub_input_q9")
if st.session_state.input_error_q9:
    st.warning(st.session_state.input_error_q9)

cols = st.columns([1.5, 6])
with cols[0]:
    st.button("Add subtraction step", on_click=add_sub_step_q9, key="add_sub_step_q9")
with cols[1]:
    st.button("Remove last step", on_click=remove_last_sub_step_q9, key="remove_sub_step_q9")

gcf9 = st.text_input(f"GCF:", placeholder="Enter a number (e.g., 2)", key=f"gcf9")


# Q10

st.write("")
st.write("")
st.write("10. Find the GCF of **30**, **6** using the **subtraction** method.")

if "sub_steps_q10" not in st.session_state:
    st.session_state.sub_steps_q10 = []

if "input_error_q10" not in st.session_state:
    st.session_state.input_error_q10 = ""

def add_sub_step_q10():
    raw = st.session_state.sub_input_q10.strip()
    try:
        num, den = map(int, raw.split("-"))
        st.session_state.sub_steps_q10.append(f"{num} - {den} = {num - den}")
        st.session_state.sub_input_q10 = ""
        st.session_state.input_error_q10 = ""
    except:
        st.session_state.input_error_q10 = "❌ Invalid format. Use e.g., 30-6"

def remove_last_sub_step_q10():
    if st.session_state.sub_steps_q10:
        st.session_state.sub_steps_q10.pop()

# Show current steps
for step in st.session_state.sub_steps_q10:
    st.text(step)

# Input and buttons
st.text_input("Type a subtraction step (e.g., 30-6)", key="sub_input_q10")
if st.session_state.input_error_q10:
    st.warning(st.session_state.input_error_q10)

cols = st.columns([1.5, 6])
with cols[0]:
    st.button("Add subtraction step", on_click=add_sub_step_q10, key="add_sub_step_q10")
with cols[1]:
    st.button("Remove last step", on_click=remove_last_sub_step_q10, key="remove_sub_step_q10")

gcf10 = st.text_input(f"GCF:", placeholder="Enter a number (e.g., 2)", key=f"gcf10")





# Example: GCF Question with division steps (Question 11)

st.write("")
st.write("")
st.write("11. Find the GCF of **150**, **100** using the Euclidean **division** method.")

if "div_steps_q11" not in st.session_state:
    st.session_state.div_steps_q11 = []

if "input_error_q11" not in st.session_state:
    st.session_state.input_error_q11 = ""

def add_div_step_q11():
    raw = st.session_state.div_input_q11.strip()
    try:
        num, den = map(int, raw.split("/"))
        if den == 0:
            st.session_state.input_error_q11 = "❌ Division by zero is not allowed."
            return
        quotient = num // den
        remainder = num % den
        st.session_state.div_steps_q11.append(f"{num} ÷ {den} = {quotient} R {remainder}")
        st.session_state.div_input_q11 = ""
        st.session_state.input_error_q11 = ""
    except:
        st.session_state.input_error_q11 = "❌ Invalid format. Use e.g., 150/100"

def remove_last_div_step_q11():
    if st.session_state.div_steps_q11:
        st.session_state.div_steps_q11.pop()

# Show current steps
for step in st.session_state.div_steps_q11:
    st.text(step)

# Input and buttons
st.text_input("Type a division (e.g., 150/100)", key="div_input_q11")
if st.session_state.input_error_q11:
    st.warning(st.session_state.input_error_q11)

cols = st.columns([1.5, 6])
with cols[0]:
    st.button("Add division step", on_click=add_div_step_q11)
with cols[1]:
    st.button("Remove last step", on_click=remove_last_div_step_q11)

gcf11 = st.text_input(f"GCF:", placeholder = "Enter a number (e.g., 2)", key=f"gcf11")



# ========== PART IV: Graphs and Trees ==========
st.header("PART IV: Graphs and Trees (9pts)")
st.write("**Instruction:** Answer the following questions about the 4 Color Theorem and graphs.")

st.write("12. How many colors at most are needed to color ANY map, so that no two adjacent regions have the same color?")
q12 = st.radio("**12. How many colors at most are needed to color ANY map, so that no two adjacent regions have the same color?**", [
    "a. 2", "b. 3", "c. 4", "d. 5"
], key="q12", label_visibility="collapsed")
st.write("")
st.write("")

st.write("13. Given the following image, how many colors at most are needed so that no two adjacent regions have the same color?")
st.image("map1.png")
color13 = st.text_input("Number of colors needed", placeholder="Enter a number (e.g., 2)", key="color13")
st.write("")
st.write("")

st.write("14. Given the following image, how many colors at most are needed so that no two adjacent regions have the same color?")
st.image("map2.jpg")
color14 = st.text_input("Number of colors needed", placeholder="Enter a number (e.g., 2)", key="color14")
st.write("")
st.write("")

st.write("15. Color the graph below so that no two connected nodes have the same color.")
st.markdown("""
Use the following colors:
- **Y** = Yellow
- **B** = Blue
- **R** = Red
""")
# Could be interactive with a component if available
# Graph Coloring
graph = components.declare_component("graph", path="graph_component")

# This will receive the values sent from the component
graph_result = graph(key="graph")

# Show the received data for debugging
# st.write("Graph input values:", graph_result)

# Questions on tree diagram
st.write("")
st.write("")
st.write("**Instruction:** Use the graph below to answer the following questions.")
# Optional: Display tree image
st.image("tree.png")

st.write("16. Which node is the **root**?")
q16 = st.radio("**16. Which node is the root?**", [
    "a. Node A",
    "b. Nodes E, F, G, H, I",
    "c. Nodes B, C, D",
    "d. Nodes E, F, C, G, H, I"
], key="q16", label_visibility="collapsed")

st.write("17. Which nodes are **leaves**?")
q17 = st.radio("**17. Which nodes are leaves?**", [
    "a. Node A",
    "b. Nodes E, F, G, H, I",
    "c. Nodes B, C, D",
    "d. Nodes E, F, C, G, H, I"
], key="q17", label_visibility="collapsed")

import networkx as nx
import graphviz

st.write("")
st.write("")
st.write("**Instruction:** Draw a tree diagram about **Animals** in the space below using the nodes given. Then answer the questions.")
cols = st.columns([1,1,1,1])
with cols[0]:
    st.write("**Nodes:**")
with cols[1]:
    st.write("Animals")
    st.write("Eagle")
    st.write("Cat")
with cols[2]:
    st.write("Birds")
    st.write("Parrot")
with cols[3]:
    st.write("Dog")
    st.write("Mammals")
    
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 1)",  # White background
    stroke_width=3,
    stroke_color="black",
    background_color="white",
    height=600,
    width=700,
    drawing_mode="freedraw",  # or "line", "rect", "circle", "transform"
    key="canvas",
)

st.write("18. List the **edges** of your tree (e.g. Animals - Mammals).")

col1, col2 = st.columns([2, 5])
with col1:
    st.subheader("Edges:")
    edge_inputs = [st.text_input(f"Edge {i+1}", placeholder="Node1 - Node2", key=f"edge_{i}", label_visibility="collapsed")
               for i in range(6)]
# edges = [e.strip() for e in edge_inputs if e and "-" in e]

# # Build undirected graph
# G = nx.Graph()
# for e in edges:
#     n1, n2 = [s.strip() for s in e.split("-", 1)]
#     G.add_edge(n1, n2)

# root = "Animals"

edges = [e.strip() for e in edge_inputs if e and "-" in e]

# Build undirected graph with normalized node names
G = nx.Graph()
all_nodes = set()

for e in edges:
    parts = e.split("-", 1)
    if len(parts) == 2:
        n1, n2 = parts[0].strip().lower(), parts[1].strip().lower()
        G.add_edge(n1, n2)
        all_nodes.update([n1, n2])

# Accept variations of "Animals" as root
possible_roots = {"animals", "animal"}
root = None
for candidate in possible_roots:
    if candidate in G:
        root = candidate
        break

T = nx.DiGraph()

if root in G:
    visited = {root}
    queue = [root]
    while queue:
        parent = queue.pop(0)
        for neighbor in G.neighbors(parent):
            if neighbor not in visited:
                visited.add(neighbor)
                T.add_edge(parent, neighbor)
                queue.append(neighbor)

with col2:
    st.subheader("Tree Visualization")

    # Build Graphviz Digraph
    if T.number_of_edges() > 0:
        dot = graphviz.Digraph()
        for u, v in T.edges():
            dot.edge(u, v)

        st.graphviz_chart(dot)

        leaves = [n for n in T.nodes if T.out_degree(n) == 0]
        # st.markdown(f"**Root:** {root}")
        # st.markdown(f"**Leaves:** {', '.join(leaves)}" if leaves else "No leaves detected")
    else:
        st.info("Enter valid edges and ensure the root node is connected.")

# Q19 & Q20
st.write("19. Which node is the **root**?")
tree19 = st.text_input("Enter node name (e.g., Parrot)", key="tree19")

st.write("20. Which nodes are **leaves**?")
tree20 = st.text_area("Enter node names separated by commas", label_visibility="collapsed", key="tree20")





# ==== Grading Functions ====

# Sudoku
def grade_sudoku6(user_board, puzzle, solution):
    total = correct = 0
    if not user_board:
        return 0
    for i in range(6):
        for j in range(6):
            if puzzle[i][j] == 0:
                total += 1
                if user_board[i][j] == solution[i][j]:
                    correct += 1
    return round(correct / total * 1.5, 2) if total else 0

def grade_sudoku9(user_board, puzzle, solution):
    total = correct = 0
    if not user_board:
        return 0
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                total += 1
                if user_board[i][j] == solution[i][j]:
                    correct += 1
    return round(correct / total * 2.5, 2) if total else 0
    
def grade_sudoku():
    return grade_sudoku6(board6, puzzle6, solution6) + grade_sudoku9(board9, puzzle9, solution9)

# Multiple choice
def grade_code():
    correct = 0
    for i in range(3, 7):
        ans = st.session_state.get(f"q{i}", "")
        corr = st.secrets["answers"][f"q{i}"]
        if ans and ans[0].lower() == corr:
            correct += 0.5
    return round(correct, 2)

def grade_other_mcq():
    correct = 0
    for q in ["q12", "q16", "q17"]:
        ans = st.session_state.get(q, "")
        corr = st.secrets["answers"][q]
        if ans and ans[0].lower() == corr:
            correct += 1
    return round(correct, 2)

# def grade_numeric(q_key, expected):
#     try:
#         ans = st.session_state.get(q_key, "")
#         if ans is None:
#             return 0.0
#         student_val = float(str(ans).strip())
#         return 1.0 if student_val == expected else 0.0
#     except:
#         return 0.0

# Short answer (Graphs and Trees)
def grade_sa():
    correct = 0
    for q in ["color13", "color14"]:
        # ans = st.session_state.get(q, "")
        corr = st.secrets["answers"][q]
        # if ans and ans.strip().lower() == corr.lower():
        #     correct += 1
        correct += grade_numeric(q, corr)
    return round(correct, 2)

# Q19
def grade_q19():
    correct = st.secrets["answers"]["tree19"]
    raw = st.session_state.get("tree19", "")
    cleaned = clean_text(raw)

    if fuzzy_match(cleaned, [correct], threshold=0.7):
        return 1.0
    return 0.0

# Coloring
def validate_coloring(graph_data):
    if not graph_data or "graph1" not in graph_data:
        return False, "No graph data received."

    coloring = graph_data["graph1"]
    
    # Ensure all nodes are colored and with valid colors
    for node, color in coloring.items():
        if color not in {"Y", "B", "R"}:
            return False, f"Node {node} has an invalid or missing color."

    # Check for edge conflicts
    edges = [
        ("2", "4"), ("2", "3"), ("3", "5"), ("4", "9"), ("5", "9"),
        ("5", "8"), ("4", "5"), ("4", "8"), ("7", "8"), ("6", "8"),
        ("5", "6"), ("5", "7"), ("3", "7"), ("1", "3")
    ]

    for a, b in edges:
        node_a = f"node{a}"
        node_b = f"node{b}"
        if coloring.get(node_a) == coloring.get(node_b):
            return False, f"Nodes {a} and {b} are connected and have the same color ({coloring.get(node_a)})."

    return True, "Graph coloring is valid!"

# if graph_result:
#     valid, message = validate_coloring(graph_result)
#     if valid:
#         st.success(message)
#     else:
#         st.error(message)

def grade_coloring():
    if graph_result:
        valid, message = validate_coloring(graph_result)
        if valid:
            return 1
    return 0

def grade_tree18():
    # Reference edges as frozensets (order doesn’t matter, all lowercase)
    correct_edges = {frozenset([a.lower(), b.lower()]) for a, b in st.secrets["answers"]["tree18"]}

    # Collect student input edges
    student_edges = set()
    for i in range(6):
        raw = st.session_state.get(f"edge_{i}", "").strip()
        if "-" in raw:
            parts = raw.split("-", 1)
            if len(parts) == 2:
                n1 = parts[0].strip().lower()
                n2 = parts[1].strip().lower()
                student_edges.add(frozenset([n1, n2]))

    # Count how many edges match
    matched = correct_edges & student_edges
    score = len(matched) / len(correct_edges)

    return round(score * 1, 2)  # Score out of 1


import re
import difflib
import string

def clean_text(s):
    return s.lower().translate(str.maketrans("", "", string.punctuation)).strip()

def fuzzy_match(word, targets, threshold=0.8):
    # Returns True if close match is found
    matches = difflib.get_close_matches(word, targets, n=1, cutoff=threshold)
    return bool(matches)


def grade_tree20():
    correct_leaves_raw = st.secrets["answers"]["tree20"]
    correct_leaves = [clean_text(s) for s in correct_leaves_raw]

    raw_input = st.session_state.get("tree20", "")
    # Now includes spaces as delimiters too
    items = re.split(r"[ ,;\n]+|(?:\band\b)", raw_input, flags=re.IGNORECASE)
    student_leaves = [clean_text(s) for s in items if clean_text(s)]

    matched = set()
    for student_leaf in student_leaves:
        if fuzzy_match(student_leaf, correct_leaves):
            matched.add(student_leaf)

    score = len(matched) / len(correct_leaves)
    return round(score, 2)


# Grading function for Subtraction Questions (Q9 and Q10)
def grade_subtraction(steps_key, gcf_key, expected_steps, expected_gcf):
    # Grading for steps
    student_steps = st.session_state.get(steps_key, [])
    steps_correct = 0.0
    if student_steps == expected_steps:
        steps_correct = 0.5  # Full points for correct steps

    # Grading for final GCF
    gcf_feedback = grade_numeric(gcf_key, expected_gcf) * 0.5
    
    # Total score for the question
    total_score = steps_correct + gcf_feedback
    return total_score


# Grading function for Division Question (Q11)
def grade_division(steps_key, gcf_key, expected_steps, expected_gcf):
    # Grading for steps
    student_steps = st.session_state.get(steps_key, [])
    steps_correct = 0.0
    if student_steps == expected_steps:
        steps_correct = 0.5  # Full points for correct steps

    # Grading for final GCF
    gcf_feedback = grade_numeric(gcf_key, expected_gcf) * 0.5
    
    # Total score for the question
    total_score = steps_correct + gcf_feedback
    return total_score


decimal.getcontext().rounding = decimal.ROUND_HALF_UP

if st.button("Submit Test"):
    if not nickname or not student_number:
        st.error("Please fill in your nickname and student number.")
    else:
        # Grade parts
        # Grading Q7
        
        grade_q7_factors = grade_factors(st.session_state.get("factors_35", ""), gcf7_factors_35) + grade_factors(st.session_state.get("factors_28", ""), gcf7_factors_28)
        grade_q7_gcd = grade_numeric("gcf7_input", gcf7)
        total_grade_q7 = (grade_q7_factors + grade_q7_gcd)

        # Grading Q8
        grade_q8_factors = grade_factors(st.session_state.get("factors_33", ""), gcf8_factors_33) + grade_factors(st.session_state.get("factors_36", ""), gcf8_factors_36)
        grade_q8_gcd = grade_numeric("gcf8_input", gcf8)
        total_grade_q8 = (grade_q8_factors + grade_q8_gcd)

        grade_factorization = (total_grade_q7 + total_grade_q8) * 0.33

        # Retrieve correct answers and steps from secrets
        gcf9_steps = st.secrets['gcf']['gcf9_steps']
        gcf9 = st.secrets['gcf']['gcf9']

        gcf10_steps = st.secrets['gcf']['gcf10_steps']
        gcf10 = st.secrets['gcf']['gcf10']

        gcf11_steps = st.secrets['gcf']['gcf11_steps']
        gcf11 = st.secrets['gcf']['gcf11']

        sudoku = grade_sudoku()
        code = grade_code()
        gcf = grade_subtraction('sub_steps_q9', 'gcf9', gcf9_steps, gcf9) + grade_subtraction('sub_steps_q10', 'gcf10', gcf10_steps, gcf10)
        gcf += grade_division('div_steps_q11', 'gcf11', gcf11_steps, gcf11)
        gcf += grade_factorization
        graphs = grade_other_mcq() + grade_sa() + grade_coloring() + grade_tree18() + grade_q19() + grade_tree20()
        total = sudoku + code + graphs + gcf

        # Build submission record
        submission = {
            "nickname": nickname,
            "student_number": student_number,
            "scores": {
                "part1_sudoku": sudoku,
                "part2_code": code,
                "part3_gcf": gcf,
                "part4_graphs": graphs,
                "total": total
            },
            "answers": {
                "sudoku": [board6, board9],

                "code": {
                    # Q3 to Q7 multiple choice answers
                    **{f"q{q}": st.session_state.get(f"q{q}", "") for q in range(3, 7)}
                },

                # Part III: Counting Combinations (Q8 to Q17)
                "gcf": {
                    "factors_35": st.session_state.get("factors_35", ""),
                    "factors_28": st.session_state.get("factors_28", ""),
                    "gcf7_input": st.session_state.get("gcf7_input", ""),

                    "factors_33": st.session_state.get("factors_33", ""),
                    "factors_36": st.session_state.get("factors_36", ""),
                    "gcf8_input": st.session_state.get("gcf8_input", ""),

                    "sub_steps_q9": st.session_state.get("sub_steps_q9", ""),
                    "gcf9": st.session_state.get("gcf9", ""),

                    "sub_steps_q10": st.session_state.get("sub_steps_q10", ""),
                    "gcf10": st.session_state.get("gcf10", ""),

                    "div_steps_q11": st.session_state.get("div_steps_q11", ""),
                    "gcf11": st.session_state.get("gcf11", ""),
                },

                "graphs": {
                    "q12": st.session_state.get("q12", ""),
                    "color13": st.session_state.get("color13", ""),
                    "color14": st.session_state.get("color14", ""),
                    "graph": st.session_state.get("graph", ""),
                    "q16": st.session_state.get("q16", ""),
                    "q17": st.session_state.get("q17", ""),
                    "edges": [st.session_state.get(f"edge_{i}", "") for i in range(6)],
                    "tree19": st.session_state.get("tree19", ""),
                    "tree20": st.session_state.get("tree20", ""),
                }
            }
                    }

        
        # Save to file
        import json, os
        os.makedirs("submissions", exist_ok=True)
        
        import gspread
        from google.oauth2.service_account import Credentials

        # Set up creds and open your sheet
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        
        # Load credentials from Streamlit secrets
        service_account_info = st.secrets["gcp_service_account"]
        creds = Credentials.from_service_account_info(service_account_info, scopes=scopes)
        
        client = gspread.authorize(creds)
        import datetime
        
        # Timestamp for filenames and sheets
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename_ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        
        json_path = f'{selected_class.replace("/", "-")}_{nickname}_{student_number}_{filename_ts}.json'
        with open(json_path, "w") as f:
            json.dump(submission, f, indent=2)
            
        

        try:
            sheet = client.open("Final").worksheet(selected_class)
        except gspread.WorksheetNotFound:
            st.error(f"Worksheet '{selected_class}' not found. Please check your Google Sheet.")

        # Convert your submission dict into a list of values (flatten if needed)
        row = [
            submission["student_number"],
            submission["nickname"],
            submission["scores"]["part1_sudoku"],
            submission["scores"]["part2_code"],
            submission["scores"]["part3_gcf"],
            submission["scores"]["part4_graphs"],
            submission["scores"]["total"],
            timestamp
            # add other fields or stringify answers if needed
        ]

        sheet.append_row(row)
        # st.success("Submission sent to Google Sheets! ✅")
        st.success(f"Submission received! ✅ Total Score: {round(total)}/20")
        
        with open(json_path, "rb") as f:
            st.download_button(
            "Download answers",
                data=f,
                file_name=os.path.basename(json_path),
                mime="application/json"
            )

