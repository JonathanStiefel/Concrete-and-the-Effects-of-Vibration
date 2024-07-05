import sqlite3
from sqlite3 import Error
from datetime import datetime

class App:

  def __init__(self, gui=True):
    """ create a database connection to a SQLite database """
    self.conn = None
    self.populated = False
    try:
      self.conn = sqlite3.connect(r"database.db")
      self.cursor = self.conn.cursor()
      print("Database Connection established.")

      self.cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
      rows = self.cursor.fetchall()

      self.populated = len(rows) > 0

      if gui:
        self.menu()

    except Error as e:
      print(e)

  def menu(self):
    choice = None
    while choice != "e":
      print("\nMain Menu Options:")
      print("(s) setup database")
      # show additional options if database has been populated
      if self.populated:
        print("(1) Withdraw Money")
        print("(2) Deposit Money")
        print("(3) Transaction History")
        print("(4) Lock Card")

      print("(e) exit application")
      choice = input("\nChoose an option: ").strip()

      if choice == 's':
        self.setup()
      elif choice == "1":
        self.withdraw_money(name, balance)
      elif choice == "2":
        self.deposit_money(name, balance)
      elif choice == "3":
        self.transaction_history(name)
      elif choice == "4":
        self.lock_card(card_number)


      elif choice == 'c':
        self.get_customer_by_email()

      elif choice == 't':
        self.top10()

  def setup(self):
    print("Resetting Database. This may take a while...")
    file = open("setup.sql")
    self.conn.executescript(file.read())
    file.close()
    self.populated = True
    print("Database successfully restored.")

  def __del__(self):
    self.conn.close()
    print("Database Connection closed.")

  def withdraw_money(self):
    pin = input("Pin: ")
    self.cursor.execute(f"SELECT account_id FROM DebitCards WHERE pin={pin}")
    #result = self.cursor.fetchone()
    # first write comments SQL commands that you need
    # 2. if inputs are required 

    # pin = input("Pin: ")
    #.execute(f"SELECT account_id FROM cards WHERE ... AND pin={pin};")
   # --> fetchone

    #print out
  def deposit_money(self):
    amount = float(input("Amount to desposit: "))
    account_id = input("Account ID: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.cursor.execute(f"INSERT INTO Transactions (amount, date_time, account_id)"f"VALUES ({amount}, '{timestamp}', {account_id})")
    self.conn.commit()
    print(f"Deposit of ${amount} successful")

