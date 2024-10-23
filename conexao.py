# Description: Conexão com o banco de dados MySQL
import mysql.connector
from mysql.connector import Error

class Conexao:
    def Dados():
        CONEXAO = mysql.connector.connect(host='localhost',
                                           user='root',
                                           password='', 
                                           database='pythonproj'
                                           )
        return CONEXAO

    def conectar():
        # """Cria uma conexão com o banco de dados MySQL."""
        try:
            CONEXAO = Conexao.Dados()
            if CONEXAO.is_connected():
                print("Conexão Aberta com sucesso com o banco de dados.")
            return CONEXAO
        except Error as e:
            print(f"Erro ao conectar: {e}")
            return None 
        
    def desconectar():
        # """Fecha a conexão com o banco de dados."""
        CONEXAO = Conexao.Dados()
        if CONEXAO.is_connected():
            CONEXAO.close()
            print("Conexão fechada com sucesso com o banco de dados.")

    def cadastrar_produto(prod_nome, prod_categoria, prod_quantidade, prod_preco, prod_validade):
        # """Insere um novo usuário na tabela."""
        CONEXAO = Conexao.Dados()
        CURSOR = CONEXAO.cursor()
        CURSOR.execute("""
            INSERT INTO Produtos (nome, categoria, quantidade_estoque, preco, data_validade) VALUES (%s, %s, %s, %s, %s)
        """, (prod_nome, prod_categoria, prod_quantidade, prod_preco, prod_validade))
        CONEXAO.commit()
        CURSOR.close()
        print("Dados Cadastrados com sucesso no banco de dados.")

    def atualizar_prod(prod_nome, prod_categoria, prod_quantidade, prod_preco, prod_validade):
        CONEXAO = Conexao.Dados()
        CURSOR = CONEXAO.cursor()
        CURSOR.execute("""
            UPDATE Produtos SET nome = %s, categoria = %s, quantidade_estoque = %s, preco = %s, data_validade = %s
        """, (prod_nome, prod_categoria, prod_quantidade, prod_preco, prod_validade))
        CONEXAO.commit()
        CURSOR.close()
        print("Dados atualizados com sucesso no banco de dados.")

    def consultar_produto(prod_nome,prod_categoria,prod_preco):
        CONEXAO = Conexao.Dados()
        CURSOR = CONEXAO.cursor()
        CURSOR.execute("""
            SELECT * FROM Produtos WHERE nome = %s OR categoria OR preco = %s
        """, (prod_nome,prod_categoria,prod_preco))
        resultado = CURSOR.fetchall()
        CURSOR.close()
        resultado_formatado = [", ".join(map(str, Linha)) for Linha in resultado]
        return resultado_formatado
    
    def consultar_estoque():
        CONEXAO = Conexao.Dados()
        CURSOR = CONEXAO.cursor()
        CURSOR.execute("""
            SELECT * FROM Produtos
        """)
        resultado = CURSOR.fetchall()
        CURSOR.close()
        resultado_formatado = [", ".join(map(str, Linha)) for Linha in resultado]
        return resultado_formatado
    
    def excluir_produto(prod_id):
        CONEXAO = Conexao.Dados()
        CURSOR = CONEXAO.cursor()
        CURSOR.execute("""
            DELETE FROM Produto WHERE id_produto = %s
        """, (prod_id,))
        CONEXAO.commit()
        CURSOR.close()
        print("Dados Deletados com sucesso no banco de dados.")
    