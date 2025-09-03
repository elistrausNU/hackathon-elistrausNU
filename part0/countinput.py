def countchars(st):
    characters_to_exclude = " .!,"
    for char in characters_to_exclude:
        st = st.replace(char, "")
    print(len(st))

if __name__ == "__main__":
    countchars("Listen, Mr. Jones, calm down.")