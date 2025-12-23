import sqlite3

def conecta_bd():
    conexao = sqlite3.connect('titulos.db')
    return conexao

#Insere dados
def insere_dados(banda, disco, ano, nota):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO discos (banda, disco, ano, nota) VALUES (?, ?, ?, ?)", (banda, disco, ano, nota))
    conexao.commit()
    conexao.close()

#Lista dados
def lista_dados():
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM discos")
    dados = cursor.fetchall()
    conexao.close()
    return dados

#Editar dados
def editar_dados(id, banda, disco, ano, nota):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("UPDATE discos SET banda = ?, disco = ?, ano = ?, nota = ? WHERE id = ?", (banda, disco, ano, nota, id))
    conexao.commit()
    conexao.close()

#Excluir disco
def excluir_disco(id):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM discos WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

