from this import d
import streamlit as st

dummy_results = """
Whether you’re an experienced project manager looking to transition into the 
software industry or a software engineer looking to take on a management role, 
there’s never been a better time to consider a role in software project management.

According to Indeed, the median salary for software project managers is more than
$126,000 per year. What’s more, the projected job growth rate for this discipline 
is 11 percent, compared to seven percent for all management occupations.

Professionals looking to enter the field of software project management will 
find that many of the same principles that apply to project management in other 
fields translate to software, said Johan Roos, a professor in the Northeastern 
University College of Professional Studies.

“The work breakdown structure is the same irrespective of industry. Whether your 
team is working on a software application or an office building,” Roos says, a 
sprint is the same—a 1- to 4-week process of building one part of a larger project 
that may ultimately take months or years to build. “It’s how you organize the work 
and the people and the deliverable at the end.”

These 15 tips for managing a software project through the entire development life
cycle will benefit both new and veteran software project managers alike."
"""
def main():
    st.title("Hello! Are you looking for something? 🤔")    
    st.write("Search Engine by Team 9")
    st.write("Pooja Bhatia ( ), Rutuja Pansare ( ), Ella Dodor ( ), Samyak Jhaveri (13043185)")
    
    # Form for Text Input and Search Button.
    with st.form(key = 'form1'):
        search_keywords = st.text_input("We have  Search Engine to help you with that! 🔎")
        submit_button = st.form_submit_button("Search!")

    
    if submit_button:
        st.success(f"Showing results for '{search_keywords}'.")
        # The format thatshould be displayed here is the result and itss corresponsding TF-IDF value
        # Could you a table with this
        with st.container():
            st.write(dummy_results)


    


if __name__ == "__main__":
    main()
