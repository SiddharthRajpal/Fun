import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
st.set_page_config(page_title="For The Best Person Ever", page_icon="💝", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.markdown("<h1 style='text-align: center; color: black;'>For Isha <3</h1>", unsafe_allow_html=True)

st.markdown("""
<style>
body {
    background-color: #00ff00;
}
</style>
""", unsafe_allow_html=True)
st.write("""
**To my dearest Isha,**

In the quiet solitude of my heart, I find your name etched into every corner, a melody that hums with the rhythm of my soul. The sky itself seems to envy the shade of your hair, for in that ethereal blue, I see an expanse far wider than the heavens, filled with dreams as infinite as the stars.

Your presence, delicate as the baby's breath you so love, adorns my life with a softness that makes each moment with you a cherished memory. Just as those dainty blossoms whisper of purity and grace, you too breathe life into every space you touch, leaving behind a fragrance not just of flowers, but of unspoken love and serenity.

Every glance of yours, like a fleeting petal caught in the wind, captivates me. And as the day drifts into the stillness of the night, it is your smile that remains my guiding light, shimmering with the promise of tomorrow.

Know this, my love: the world could crumble, the stars could fall from the sky, but my love for you would remain unshaken, as constant and enduring as the tides. I am yours, as the moon belongs to the night, as the sea to the shore—bound eternally, yet forever in awe of your beauty.

With all the love my heart can hold,  
**Yours forever,**  
Barnman
        """)
pdf_viewer("woah.pdf")



