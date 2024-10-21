import streamlit

# Showing a button on the web page
isButton1Pressed: bool = streamlit.button("Click me")
print("---------------------------------")
if isButton1Pressed:
    print("Button1 is pressed")
else:
    print("Button1 has not been pressed yet")


# Each time you click any of the buttons, the script gets re-run.
isButton2Pressed: bool = streamlit.button("I'm the second button; click me too!")
if isButton2Pressed:
    print("Button2 is pressed")
else:
    print("Button2 has not been pressed yet")
print("---------------------------------")