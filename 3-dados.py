import sqlite3

conexao = sqlite3.connect('titulos.db')
cursor = conexao.cursor()

# Inserindo dados na tabela discos
cursor.execute(
    """ 
        INSERT INTO discos(banda, disco, ano, nota)
         VALUES ('Deicide', 'Legion', 1990, 9.5),
         ('Cannibal Corpse', 'Tomb of the Mutilated', 1992, 9.0),
            ('Morbid Angel', 'Covenant', 1993, 9.3),
            ('Obituary', 'Cause of Death', 1990, 8.8);
    """
)
conexao.commit()
conexao.close()
print("Dados inseridos com sucesso!")


