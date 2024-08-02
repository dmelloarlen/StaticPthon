import streamlit as sl
import anaylsis as an
import webbrowser

obj=an.Ana
def navbar():
    sl.markdown("""
    <style>
    .st-emotion-cache-bm2z3a{
        align-items:start;
        justify-content:center;
        flex-direction:row;
    }
    .st-emotion-cache-13ln4jf {
        padding:0px;
    }
    .st-emotion-cache-h4xjwg {
        background:rgb(14 17 23 / 0%);
        margin-top:-100px;
    }
    #nav {
        display: flex;
        font-family: 'Times New Roman', Times, serif;
        justify-content:center;
        width:100%;
        margin-top:15px;
    }
    #nav ul {
        display: flex;
        /* border: 2px solid red; */
    }
    #nav ul li {
        list-style: none;
    }
    #nav ul li a {
        text-decoration: none;
        padding: 7px 45px;
        font-size: 1.2rem;
        border-radius: 20px;
        color: #92f57f;
        font-weight: bold;
    }
    #nav ul li a:hover {
        border-bottom:2px solid red;
    }
    </style>

    <div id="nav">
        <ul id="ul">
            <li class="item"><a href="/?page=home" target="_self">Home</a></li>
            <li class="item"><a href="/?page=visualisation" target="_self">Visualisation</a></li>
            <li class="item"><a href="/?page=data" target="_self">Data</a></li>
            <li class="item"><a href="https://github.com/dmelloarlen/Glass_classification-/blob/main/README.md" target="_blank">About</a></li>
        </ul>  
    </div>
    """, unsafe_allow_html=True)

    qp = sl.query_params
    page = qp.get("page","home")

    if page == "home":
        obj.home()
    elif page == "visualisation":
        obj.plot()
    elif page == "about":
        pass
        # webbrowser.open_new_tab("https://github.com/dmelloarlen/Glass_classification-/blob/main/README.md")
    elif page == "data":
       obj.info()
    else:
        sl.title("404")
        sl.write("Page not found")

navbar()

