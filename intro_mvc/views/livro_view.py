import tkinter as tk
from tkinter import ttk, messagebox
from controllers.livro_controller import LivroController

class LivroView:
    def __init__(self, controller):
        self.controller = controller
        self._show_livros_tela()
        
    @staticmethod
    def iniciar_login_banco():
        def conectar():
            db_config = {
                "dbname":db_entry.get(),
                "user": user_entry.get(),
                "password":password_entry.get(),
                "host":host_entry.get(),
                "port":port_entry.get()
            }
            try:
                controller = LivroController(db_config)
                login_win.destroy()
                LivroView(controller)
                
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possivel conctar ao banco de dados:\n{e}")
                
        login_win = tk.Tk()
        login_win.title("Conectar ao Banco de Dados")
        login_win.geometry("350x300")
        
        tk.Label(login_win, text="Host:").pack(padx=2)
        host_entry = tk.Entry(login_win)
        host_entry.pack()
        
        tk.Label(login_win, text="Porta:").pack(padx=2)
        port_entry = tk.Entry(login_win)
        port_entry.pack()
        
        tk.Label(login_win, text="Usuário:").pack(padx=2)
        user_entry = tk.Entry(login_win)
        user_entry.pack()
        
        tk.Label(login_win, text="Senha:").pack(padx=2)
        password_entry = tk.Entry(login_win, show="*")
        password_entry.pack()
        
        tk.Label(login_win, text="Nome do Banco:").pack(padx=2)
        db_entry = tk.Entry(login_win)
        db_entry.pack()
        
        tk.Button(login_win, text="Conectar", command=conectar).pack(pady=15)
        
    def _show_livros_tela(self):
        livros = self.controller.lista_livro()
        win = tk.Tk()
        win.title("Livro Cadastrado")
        win.geometry("700x400")
        columns = ("ID", "Título", "Autor", "Ano")
        tree = ttk.Treeview(win, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col.capitalize())
            tree.column(col, width=120)
        for livro in livros:
            tree.insert("",tk.END, values=(livro['id'], livro['tittulo'],livro['autor'],livro['ano'],livro['ISBN'],))
        tree.pack(expand=True, fill='both')
        win.mainloop()