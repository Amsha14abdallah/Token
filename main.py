from Databases import save_token, get_latest_token, delete_token
from Databases import get_token_history
import streamlit as st
from utils import generate_token
from Databases import save_token, get_latest_token

st.set_page_config(page_title="Electricity Token System", layout="centered")

st.title("🔌 Electricity Token Generator")
st.markdown("Tengeneza token ya umeme kwa kutumia namba ya mita")

meter = st.text_input("Ingiza namba ya mita", max_chars=10)
units = st.number_input("Idadi ya units kununua", min_value=1, max_value=100)

if st.button("Tengeneza Token"):
    if not meter or len(meter) < 4:
        st.error("Tafadhali ingiza namba halali ya mita")
    else:
        token = generate_token(meter, int(units))
        save_token(meter, token, units)
        st.success(f"✅ Token yako ni: {token}")

        #kutoa alert kwenye simu#
        # 🚨 Alert kama units ni chini ya 5
        if units < 5:
            st.warning("⚠️ Kumbuka: Units ulizonunua ni chache sana. Huenda zikaisha haraka!")
        if units <= 2:  # Alert ikiwa units zimebaki chini ya 2
            ujumbe = f"⚠️ Units zako ni {units}. Tafadhali ongeza kabla hazijaisha."
            (ujumbe, "+255783172101")  # Badilisha na simu halisi ya mtumiaji

        # 🎉 Ujumbe maalum kwa units kubwa
        elif units >= 20:
            st.success("🎉 Umenunua units za kutosha! Asante kwa kutumia huduma yetu.")

        st.success(f"✅ Token yako ni: {token}")
        if units >= 2:  # Alert ikiwa units zipo zaidi ya 2
            ujumbe = f"⚠️ Units zako ni {units}. Ahsante! endelea kutumia huduma zetu."
            (ujumbe, "+255783172101")  # Badilisha na simu halisi ya mtumiaji




if st.button("Angalia token ya mwisho"):
    if not meter:
        st.warning("Weka namba ya mita kwanza")
    else:
        data = get_latest_token(meter)
        if data:
            st.info(f"💾 Token ya mwisho: {data[0]} | {data[1]} units | {data[2]}")
        else:
            st.warning("Hakuna token iliyohifadhiwa kwa mita hiyo.")


if st.button("Angalia historia ya token"):
    if not meter:
        st.warning("Weka namba ya mita kwanza")
    else:
        history = get_token_history(meter)
        if history:
            st.markdown("### 🧾 Historia ya Token:")
            for i, item in enumerate(history, start=1):
                st.write(f"{i}. 🔐 Token: `{item[0]}` | ⚡ Units: {item[1]} | 🕒 Tarehe: {item[2]}")
        else:
            st.info("Hakuna historia ya token kwa mita hii.")


st.markdown("---")
st.subheader("🗑️ Futa token za mita")

if meter:
    confirm = st.checkbox("Nathibitisha kwamba nataka kufuta token zote za mita hii")
    
    if st.button("Futa token zote"):
        if confirm:
            delete_token(meter)
            st.success(f"🧹 Token zote kwa mita {meter} zimefutwa kikamilifu.")
        else:
            st.warning("Thibitisha kwanza kwa kuweka tiki kwenye kisanduku hapo juu.")
else:
    st.info("Weka namba ya mita kwanza ili kuweza kufuta token.")



#streamlit run main.py^  ina sanikisha system nzima an
