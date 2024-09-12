import streamlit as st
import os
st.markdown("<h1 style='text-align: center; color: white;'>Notes <3</h1>", unsafe_allow_html=True)

notes_folder = "Notes"
if not os.path.exists(notes_folder):
    os.makedirs(notes_folder)
def save_note_to_folder(title, content):
    file_name = f"{title}.txt"
    file_path = os.path.join(notes_folder, file_name)
    
    with open(file_path, "w") as f:
        f.write(content)
def load_notes():
    notes = {}
    for note_file in os.listdir(notes_folder):
        if note_file.endswith(".txt"):
            file_path = os.path.join(notes_folder, note_file)
            with open(file_path, "r") as f:
                notes[note_file] = f.read()
    return notes
st.subheader("Our Notes <3")

notes = load_notes()
if notes:
    for note_title, note_content in notes.items():
        with st.expander(note_title.replace(".txt", "")):
            st.write(note_content)
else:
    st.write("No notes found! Add your first one using the button below.")
add_note_mode = st.checkbox("Add a Note")
if add_note_mode:
    st.subheader("New Note")

    title = st.text_input("Title")
    content = st.text_area("Content")

    if st.button("Save Note"):
        if title and content:
            save_note_to_folder(title, content)
            st.success(f"Note '{title}' added successfully!") 
            st.rerun()
        else:
            st.error("Both title and content are required!")
