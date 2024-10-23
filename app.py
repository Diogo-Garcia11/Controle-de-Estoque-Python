from conexao import Conexao
import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox

class EstoqueApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Controle de Estoque")

        # Labels e Entradas

        tk.Label(master, text="ID:").grid(row=0, column=0)
        self.id_entry = tk.Entry(master)
        self.id_entry.grid(row=0, column=1)

        tk.Label(master, text="Nome:").grid(row=1, column=0)
        self.nome_entry = tk.Entry(master)
        self.nome_entry.grid(row=1, column=1)

        tk.Label(master, text="Categoria:").grid(row=2, column=0)
        self.categoria_entry = tk.Entry(master)
        self.categoria_entry.grid(row=2, column=1)

        tk.Label(master, text="Quantidade:").grid(row=3, column=0)
        self.quantidade_entry = tk.Entry(master)
        self.quantidade_entry.grid(row=3, column=1)

        tk.Label(master, text="Preço(00.00):").grid(row=4, column=0)
        self.preco_entry = tk.Entry(master)
        self.preco_entry.grid(row=4, column=1)

        tk.Label(master, text="Data de Validade (YYYY/MM/DD):").grid(row=5, column=0)
        self.validade_entry = tk.Entry(master)
        self.validade_entry.grid(row=5, column=1)

        # Botões
        tk.Button(master, text="Cadastrar", command=self.cadastrar_produto).grid(row=6, column=0)
        tk.Button(master, text="Atualizar", command=self.atualizar_produto).grid(row=6, column=1)
        tk.Button(master, text="Consultar", command=self.consultar_produto).grid(row=7, column=0)
        tk.Button(master, text="Consultar Estoque", command=self.consultar_estoque).grid(row=7, column=1)
        tk.Button(master, text="Excluir", command=self.excluir_produto).grid(row=8, column=0)

    def conectar(self):
        self.conexao = Conexao.conectar()
        return self.conexao

    def desconectar(self):
        Conexao.desconectar()

    def cadastrar_produto(self):
        prod_nome = self.nome_entry.get()
        prod_categoria = self.categoria_entry.get()
        prod_quantidade = self.quantidade_entry.get()
        prod_preco = self.preco_entry.get()
        prod_validade = self.validade_entry.get() or None

        try:
            self.conectar()
            Conexao.cadastrar_produto(prod_nome, prod_categoria, int(prod_quantidade), float(prod_preco), prod_validade)
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar produto: {e}")
        finally:
            self.desconectar()

    def atualizar_produto(self):
        prod_id = self.id_entry.get()
        prod_nome = self.nome_entry.get()
        prod_categoria = self.categoria_entry.get()
        prod_quantidade = self.quantidade_entry.get()
        prod_preco = self.preco_entry.get()
        prod_validade = self.validade_entry.get() or None

        try:
            self.conectar()
            Conexao.atualizar_produto(prod_nome, prod_categoria, int(prod_quantidade), float(prod_preco), prod_validade, prod_id)
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar produto: {e}")
        finally:
            self.desconectar()

    def consultar_produto(self):
        prod_nome = self.nome_entry.get()
        prod_categoria = self.categoria_entry.get()
        prod_preco = self.preco_entry.get()

        try:
            self.conectar()
            resultado = Conexao.consultar_produto(prod_nome, prod_categoria, prod_preco)
            resultado_str = "\n".join(resultado) if resultado else "Nenhum produto encontrado."
            messagebox.showinfo("Resultado", resultado_str)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar produto: {e}")
        finally:
            self.desconectar()

    def consultar_estoque(self):
        try:
            self.conectar()
            resultado = Conexao.consultar_estoque()
            resultado_str = "\n".join(resultado) if resultado else "Estoque vazio."
            messagebox.showinfo("Estoque", resultado_str)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar estoque: {e}")
        finally:
            self.desconectar()

    def excluir_produto(self):
        prod_id = self.id_entry.get()  # Aqui você pode usar um campo separado para ID

        try:
            self.conectar()
            Conexao.excluir_produto(prod_id)
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir produto: {e}")
        finally:
            self.desconectar()

if __name__ == "__main__":
    root = tk.Tk()
    app = EstoqueApp(root)
    root.mainloop()