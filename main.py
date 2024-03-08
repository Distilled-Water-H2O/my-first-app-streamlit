# introduction
"""
- this is a my first streamlit application to be deployed. 
- it's as simple as possible. 
<_ streamlit run main.py
"""

# libraries
import streamlit as st

# setting up the page
st.set_page_config(page_title="@Dist-Wat", page_icon=":rocket:", layout="wide")

option = st.sidebar.selectbox(
    "select page from here:",
    ("Homepage", "About me", "About YT channel")
)

# Homepage
if option == "Homepage":
    st.subheader("Hi, I'm Divit :wave:")
    st.title("Welcome to my mainpage")
    st.write("**I'm a 13yo developing computer science expert in python and streamlit and a part time content creator**")
    st.divider()
    st.header("About this page :spider:")
    st.write(
        "This is a based webpage I build for fun or as a short portfolio for my freelancing projects. I made it "
        "completely with python with help of streamlit library and this gave me confidence of taking programming "
        "seriously and python became my idol language. this website also contains more about me and my Youtube "
        "channel and links to my other streamlit projects too. This page I've created can't be made by a full "
        "time web development programmer. I hope you like it too :smile:"
    )
    st.divider()
    st.subheader("Thanks for visiting that webpage :thumbsup:")
    st.write("**you can visit more of my webpages using that sidebar button**")

elif option == "About me":
    st.header("About me :eyes:")
    st.divider()
    st.write(
        "I've been doing Python for 1.5 months now from nothing and I've made a Gargantuan progress that I wanna show "
        "you in this project of mine. I am well at content writing even though english is not my first language. I'm "
        "also good at Researching and you can see my webpage for comparing a normal grownup web developer. I'm an "
        "ambitious and genius Indian boy that wanna own a million dollar Ai company. Simply the answer for why is that "
        "Ai is taking over everything and Ai has influenced me so much that I wanna do this because \"**Ai will never "
        "take your job but a person who knows Ai will**\" that quote changed my whole ideology and it's true."
    )
    st.divider()

    # faq section
    st.header(":raising_hand: FAQ")
    l_col, r_col = st.columns((2, 1))
    with l_col:
        with st.expander("**What are my main Streamlit projects?**"):
            st.divider()
            st.write(
                """
            I've made python projects normally but then I fall in love with Streamlit library
        
            :rocket: Here are my projects:
            - Based streamlit Web application
            - Full AI Web application
            - Finance Web application
            - Data analysis Web application
                """
            )
        with st.expander("**What is relation between me and Coding?**"):
            st.divider()
            st.write(
                """
            I had to code when I was in 4th grade. Funny but I wanted to make games but i fell in game addiction
            myself. Then become mature and I thought it's waste of time and it's time to do other stuff and as i told
            AI caught my attention and I start to code and i banged up.  
                """
            )
    st.divider()

    st.subheader("Thanks for visiting that webpage :thumbsup:")
    st.write("**you can visit more of my webpages using that sidebar button**")

elif option == "About YT channel":
    st.header("About my Youtube channel :clapper:")
    st.divider()
    st.write(
                """
            I became a youtuber because I had editing skills and i thought I can do this. I became GOD of editing later.
            I was in success but then it faced loss because i was making videos about old trend but after i started to  
            make videos about the updated topics i gained support and I usually do this job.      
                
            on my youtube channel i usually upload videos mainly of following content: 
            - Roasting the right-wing media.
            - Map videos because easy revenue.
            - country, boywithuke, trending, 8D music/lyric videos. 
            - edits both in full and yt Shorts.
                
            I create such a high quality content :flag-ps: that your eyes gonna love it. Make sure to subscribe.  
                """
            )
    st.write("[Check out my youtube channel](https://youtube.com/@DistilledWater-HQ)")
    st.write("---")
    st.subheader("Thanks for visiting that webpage :thumbsup:")
    st.write("**you can visit more of my webpages using that sidebar button**")
