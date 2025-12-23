import streamlit as  st
import dados
import pandas as pd
        
st.title("discos de metal extremo")

banda = st.text_input("Banda")
disco = st.text_input("Disco")
ano = st.number_input("Ano de lançamento", min_value=1980, max_value=2025)
nota = st.slider("Nota", min_value=0.0, max_value=10.0)

if st.button("Adicionar Disco"):
    dados.insere_dados(banda, disco, ano, nota)
    st.success("Dados inseridos com sucesso!")

discos = dados.lista_dados()
st.header("Lista de Discos")

dados_df = pd.DataFrame(discos, columns=["ID", "Banda", "Disco", "Ano", "Nota"])
st.dataframe(dados_df, hide_index=True)

st.subheader("Editar disco")
if discos:
    id_editar = st.number_input("ID do disco a editar", min_value=1, step=1)

if discos:
    disco_sel = next((disco for disco in discos if disco[0] == id_editar), None)
    if disco_sel:
        banda_editar = st.text_input("banda", disco_sel[1])
        disco_editar = st.text_input("disco", disco_sel[2])
        ano_editar = st.number_input("Ano de lançamento", min_value=1980, max_value=2025, value=disco_sel[3])
        nota_editar = st.slider("Nota", min_value=0.0, max_value=10.0, value=disco_sel[4])

        if st.button("Salvar Alterações"):
            dados.editar_dados(id_editar, banda_editar, disco_editar, ano_editar, nota_editar)
            st.success("Disco atualizado com sucesso!")
            st.rerun()

st.subheader("Excluir Disco")

id_excluir = st.selectbox("Selecione o ID do disco para excluir", dados_df["ID"])
if st.button("Excluir Disco"):
    dados.excluir_disco(id_excluir)
    st.success("Disco excluído com sucesso!")
    st.rerun()

