import mysql.connector
import customtkinter as ctk


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="godsAvou1r",
    database="Store"
)

# récupérer les catégories
def get_categories():
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM category")
    categories = cursor.fetchall()
    cursor.close()
    return {cat[1]: cat[0] for cat in categories}  

#  récupérer les produits d'une catégorie
def get_products_by_category(category_id):
    cursor = db.cursor()
    query = "SELECT id, name, description, price, quantity FROM product WHERE id_category = %s"
    cursor.execute(query, (category_id,))
    products = cursor.fetchall()
    cursor.close()
    return products  


CATEGORIES = get_categories()

# Interface custom-tkinter
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Menu Principal")
        self.geometry("800x600")  

        # Config  colonnes et lignes
        self.grid_columnconfigure(list(range(len(CATEGORIES))), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Label principal
        self.label = ctk.CTkLabel(self, text="Bienvenue dans le Store", font=("Arial", 30))
        self.label.grid(row=0, column=0, columnspan=len(CATEGORIES), pady=20, sticky="nsew")

        #  afficher les produits
        self.frame_produits = ctk.CTkFrame(self)
        self.frame_produits.grid(row=2, column=0, columnspan=len(CATEGORIES), pady=20, sticky="nsew")

        #  boutons en fonction des catégories SQL
        for idx, (category_name, category_id) in enumerate(CATEGORIES.items()):
            button = ctk.CTkButton(self, text=category_name, height=50, command=lambda cat=category_name: self.afficher_produits(cat))
            button.grid(row=1, column=idx, padx=10, pady=(0, 20), sticky="ew")

        # Formulaire d'ajout
        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.grid(row=3, column=0, columnspan=len(CATEGORIES), pady=10, sticky="nsew")

        self.init_formulaire()

    def afficher_produits(self, categorie):
        # Affiche produits des catégorie sous forme de grille.
        for widget in self.frame_produits.winfo_children():
            widget.destroy()

        category_id = CATEGORIES[categorie]
        produits = get_products_by_category(category_id)

        label = ctk.CTkLabel(self.frame_produits, text=f"Produits - {categorie}", font=("Arial", 18, "bold"))
        label.grid(row=0, column=0, columnspan=4, pady=10)

        if produits:
            cols = 3  
            for i, produit in enumerate(produits):
                product_id, name, description, price, quantity = produit
                product_info = f"{name}\n{description}\n💰 {price}€ | 🛒 {quantity} en stock"

                produit_label = ctk.CTkLabel(self.frame_produits, text=product_info, font=("Arial", 14), width=300, height=100)
                produit_label.grid(row=(i // cols) + 1, column=(i % cols), padx=10, pady=10, sticky="nsew")

                # Bouton Modifier
                btn_modifier = ctk.CTkButton(self.frame_produits, text="Modifier", command=lambda p=produit: self.afficher_modification(p))
                btn_modifier.grid(row=(i // cols) + 1, column=(i % cols) + 1, padx=5, pady=10)

                # Bouton Supprimer
                btn_supprimer = ctk.CTkButton(self.frame_produits, text="🗑", fg_color="red", command=lambda pid=product_id: self.supprimer_produit(pid))
                btn_supprimer.grid(row=(i // cols) + 1, column=(i % cols) + 2, padx=5, pady=10)

            for col in range(cols):
                self.frame_produits.grid_columnconfigure(col, weight=1)
        else:
            no_product_label = ctk.CTkLabel(self.frame_produits, text="Aucun produit disponible", font=("Arial", 14))
            no_product_label.grid(row=1, column=0, columnspan=3, pady=10)

    def afficher_modification(self, produit):
        
        product_id, name, description, price, quantity = produit

        self.entry_name.delete(0, "end")
        self.entry_price.delete(0, "end")
        self.entry_quantity.delete(0, "end")

        self.entry_name.insert(0, name)
        self.entry_price.insert(0, str(price))
        self.entry_quantity.insert(0, str(quantity))

        self.btn_save.configure(command=lambda: self.modifier_produit(product_id))

    def modifier_produit(self, product_id):
        
        new_name = self.entry_name.get()
        new_price = float(self.entry_price.get())
        new_quantity = int(self.entry_quantity.get())

        cursor = db.cursor()
        query = "UPDATE product SET name=%s, price=%s, quantity=%s WHERE id=%s"
        cursor.execute(query, (new_name, new_price, new_quantity, product_id))
        db.commit()
        cursor.close()

        self.afficher_produits(list(CATEGORIES.keys())[0])  

    def supprimer_produit(self, product_id):
        
        cursor = db.cursor()
        query = "DELETE FROM product WHERE id=%s"
        cursor.execute(query, (product_id,))
        db.commit()
        cursor.close()

        self.afficher_produits(list(CATEGORIES.keys())[0])  

    def init_formulaire(self):
        # formulaire ajout  produit
        self.entry_name = ctk.CTkEntry(self.frame_form, placeholder_text="Nom du produit")
        self.entry_name.grid(row=0, column=0, padx=5)

        self.entry_price = ctk.CTkEntry(self.frame_form, placeholder_text="Prix")
        self.entry_price.grid(row=0, column=1, padx=5)

        self.entry_quantity = ctk.CTkEntry(self.frame_form, placeholder_text="Stock")
        self.entry_quantity.grid(row=0, column=2, padx=5)

        self.btn_save = ctk.CTkButton(self.frame_form, text="Ajouter", command=self.ajouter_produit)
        self.btn_save.grid(row=0, column=3, padx=5)

    def ajouter_produit(self):
        
        name = self.entry_name.get()
        price = float(self.entry_price.get())
        quantity = int(self.entry_quantity.get())

        cursor = db.cursor()
        query = "INSERT INTO product (name, price, quantity, id_category) VALUES (%s, %s, %s, 1)"
        cursor.execute(query, (name, price, quantity))
        db.commit()
        cursor.close()

        self.afficher_produits(list(CATEGORIES.keys())[0])  

if __name__ == "__main__":
    app = App()
    app.mainloop()
