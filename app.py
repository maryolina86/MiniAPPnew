import streamlit as st
import pandas as pd

# Configurazione pagina
st.set_page_config(page_title="Mini Excel App", layout="wide")

# Titolo
st.title("📊 Mini App Excel (Streamlit)")

# Upload file Excel
uploaded_file = st.file_uploader("Carica file Excel", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    st.success("File caricato correttamente ✅")

    # Mostra dati
    if st.checkbox("Mostra dati originali"):
        st.dataframe(df)

    st.subheader("🔍 Filtri")

    col1, col2 = st.columns(2)

    with col1:
        col_index = st.selectbox("Scegli colonna", df.columns)

    with col2:
        valore = st.text_input("Valore da cercare")

    # Filtro dati
    if st.button("Applica filtro"):
        if valore:
            filtered = df[df[col_index].astype(str).str.contains(valore, case=False, na=False)]
        else:
            filtered = df

        st.write("Risultati filtro:")
        st.dataframe(filtered)

    # Distinct
    if st.button("Mostra DISTINCT"):
        distinct_values = df[col_index].dropna().unique()
        st.write("Valori unici:")
        st.write(pd.Series(distinct_values))

    # Download risultati
    st.subheader("💾 Download dati")

    if st.button("Esporta Excel filtrato"):
        if valore:
            filtered = df[df[col_index].astype(str).str.contains(valore, case=False, na=False)]
        else:
            filtered = df

        file_name = "output.xlsx"
        filtered.to_excel(file_name, index=False, engine="openpyxl")

        with open(file_name, "rb") as f:
            st.download_button("Scarica file", f, file_name=file_name)

else:
    st.info("Carica un file Excel per iniziare")

# Footer
st.markdown("---")

st.markdown("""
✅ Funzionalità disponibili:
- Filtri dinamici
- Ricerca testo
- Distinct valori
- Download Excel
""")
