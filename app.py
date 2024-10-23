from conexao import Conexao
import mysql.connector
from mysql.connector import Error

class App:
    def run_app():
        while True:
            
            print("""
                  1. Cadastrar Produto
                  2. Atualizar Produto
                  3. Consultar Produto
                  4. Consultar Estoque
                  5. Excluir Produto
                  6. Sair
                  """)
            
            opcao = input("Escolha uma opção: ")
            try:
                if opcao == '1':

                    Conexao.conectar()
                    prod_nome = input("Insira o nome do produto: ")
                    prod_categoria = input("Insira a categoria do produto:")
                    prod_quantidade = input("Insira a quantidade em estoque:")
                    prod_preco = input("Insira o preco do produto:")
                    prod_validade = input("Insira a data de validade:")
                    Conexao.cadastrar_produto(prod_nome, prod_categoria, prod_quantidade, prod_preco, prod_validade)
                    Conexao.desconectar() 

                elif opcao == '2':

                    Conexao.conectar()
                    prod_nome = input("Insira o nome do produto: ")
                    prod_categoria = input("Insira a categoria do produto:")
                    prod_quantidade = input("Insira a quantidade em estoque:")
                    prod_preco = input("Insira o preco do produto:")
                    prod_validade = input("Insira a data de validade:")
                   
                    Conexao.atualizar_produto(prod_nome, prod_categoria, prod_quantidade, prod_preco, prod_validade)
                    Conexao.desconectar()

                elif opcao == '3':

                    Conexao.conectar()
                    prod_nome = input("Insira o nome do produto: ")
                    prod_categoria = input("Insira a categoria do produto:")
                    prod_preco = input("Insira o preco do produto:")
                    resultado = Conexao.consultar_produto(prod_nome, prod_categoria, prod_preco)
                    for busca in resultado:
                        print(busca)
                    Conexao.desconectar()

                elif opcao == '4':

                    Conexao.conectar()
                    resultado = Conexao.consultar_estoque()
                    for busca in resultado:
                        print(busca)
                    Conexao.desconectar()
                    
                elif opcao == '5':

                    Conexao.conectar()
                    prod_id = input("Insira o id do produto: ")
                    Conexao.excluir_produto(prod_id)
                    Conexao.desconectar()

                elif opcao == '6':

                    break

                else:

                    print("Opção inválida.") 

            except Error as e:

                print(f"Erro: {e}")
                Conexao.desconectar()
                
if __name__ == "__main__":
    App.run_app()