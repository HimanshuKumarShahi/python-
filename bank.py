"""
bank.py

Simple Bank Management System (CLI) — pure Python, single file.
Data saved to 'bank_db.json' in the same directory.
"""

import os
import sys
import json
import random
import hashlib
import getpass
from datetime import datetime
from typing import Dict, Any

DB_FILE = "bank_db.json"
ADMIN_PASSWORD = "admin123"  # change if you want


# ---------- Utilities ----------

def now_ts() -> str:
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


def load_db() -> Dict[str, Any]:
    if not os.path.exists(DB_FILE):
        return {"accounts": {}}
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        print("Warning: couldn't read database file, starting fresh.")
        return {"accounts": {}}


def save_db(db: Dict[str, Any]) -> None:
    tmp = DB_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    os.replace(tmp, DB_FILE)


def gen_account_number(db: Dict[str, Any]) -> str:
    while True:
        acct = str(random.randint(10**9, 10**10 - 1))  # 10-digit number
        if acct not in db["accounts"]:
            return acct


def hash_pin(account_number: str, pin: str) -> str:
    h = hashlib.sha256()
    h.update((account_number + ":" + pin).encode("utf-8"))
    return h.hexdigest()


def pretty_money(x: float) -> str:
    return f"₹{x:,.2f}"


def input_pin(prompt="PIN (hidden): ") -> str:
    while True:
        pin = getpass.getpass(prompt)
        if not pin.isdigit() or not (4 <= len(pin) <= 6):
            print("PIN must be 4-6 digits.")
            continue
        return pin


# ---------- Banking Operations ----------

def create_account(db: Dict[str, Any]) -> None:
    print("\n--- Create New Account ---")
    name = input("Full name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    while True:
        try:
            initial = float(input("Initial deposit (min 0): ").strip() or "0")
            if initial < 0:
                print("Deposit cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid number.")

    pin = input_pin("Set a 4-6 digit PIN (hidden): ")
    acct = gen_account_number(db)
    pin_hash = hash_pin(acct, pin)
    db["accounts"][acct] = {
        "name": name,
        "pin_hash": pin_hash,
        "balance": round(initial, 2),
        "created_at": now_ts(),
        "transactions": []
    }
    if initial > 0:
        db["accounts"][acct]["transactions"].append({
            "type": "credit",
            "amount": round(initial, 2),
            "balance": round(initial, 2),
            "time": now_ts(),
            "note": "Initial deposit"
        })
    save_db(db)
    print(f"Account created! Number: {acct}")


def authenticate(db: Dict[str, Any]):
    acct = input("Account Number: ").strip()
    if acct not in db["accounts"]:
        print("Account not found.")
        return None
    pin = getpass.getpass("PIN (hidden): ")
    if db["accounts"][acct]["pin_hash"] != hash_pin(acct, pin):
        print("Incorrect PIN.")
        return None
    print(f"Welcome, {db['accounts'][acct]['name']}!")
    return acct


def show_balance(db: Dict[str, Any], acct: str) -> None:
    print(f"Current balance: {pretty_money(db['accounts'][acct]['balance'])}")


def deposit(db: Dict[str, Any], acct: str) -> None:
    try:
        amt = float(input("Deposit amount: "))
        if amt <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid number.")
        return

    acc = db["accounts"][acct]
    acc["balance"] += amt
    acc["transactions"].append({
        "type": "credit",
        "amount": amt,
        "balance": acc["balance"],
        "time": now_ts(),
        "note": "Deposit"
    })
    save_db(db)
    print(f"Deposited {pretty_money(amt)}. New balance: {pretty_money(acc['balance'])}")


def withdraw(db: Dict[str, Any], acct: str) -> None:
    try:
        amt = float(input("Withdraw amount: "))
        if amt <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid number.")
        return

    acc = db["accounts"][acct]
    if amt > acc["balance"]:
        print("Insufficient funds.")
        return

    acc["balance"] -= amt
    acc["transactions"].append({
        "type": "debit",
        "amount": amt,
        "balance": acc["balance"],
        "time": now_ts(),
        "note": "Withdrawal"
    })
    save_db(db)
    print(f"Withdrew {pretty_money(amt)}. New balance: {pretty_money(acc['balance'])}")


def transfer(db: Dict[str, Any], acct: str) -> None:
    to_acct = input("Recipient account number: ").strip()
    if to_acct not in db["accounts"]:
        print("Recipient not found.")
        return
    if to_acct == acct:
        print("Cannot transfer to self.")
        return
    try:
        amt = float(input("Transfer amount: "))
        if amt <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid number.")
        return

    from_acc = db["accounts"][acct]
    if amt > from_acc["balance"]:
        print("Insufficient funds.")
        return

    to_acc = db["accounts"][to_acct]
    from_acc["balance"] -= amt
    to_acc["balance"] += amt
    ttime = now_ts()
    from_acc["transactions"].append({
        "type": "debit",
        "amount": amt,
        "balance": from_acc["balance"],
        "time": ttime,
        "note": f"Transfer to {to_acct}"
    })
    to_acc["transactions"].append({
        "type": "credit",
        "amount": amt,
        "balance": to_acc["balance"],
        "time": ttime,
        "note": f"Transfer from {acct}"
    })
    save_db(db)
    print(f"Transferred {pretty_money(amt)} to {to_acct}.")


def mini_statement(db: Dict[str, Any], acct: str) -> None:
    txs = db["accounts"][acct]["transactions"][-10:]
    if not txs:
        print("No transactions yet.")
        return
    print("\n--- Mini Statement ---")
    for tx in reversed(txs):
        print(f"{tx['time']} | {tx['type'].upper():6} | {pretty_money(tx['amount']):>8} | Bal: {pretty_money(tx['balance'])} | {tx.get('note','')}")


# ---------- Admin ----------

def admin_view(db: Dict[str, Any]) -> None:
    total = sum(acc["balance"] for acc in db["accounts"].values())
    print("\n--- Admin Accounts ---")
    for acct, data in db["accounts"].items():
        print(f"{acct} | {data['name']} | Balance: {pretty_money(data['balance'])}")
    print(f"\nTotal accounts: {len(db['accounts'])}, Bank total: {pretty_money(total)}")


# ---------- Menus ----------

def account_menu(db: Dict[str, Any], acct: str) -> None:
    while True:
        print("\n--- Account Menu ---")
        print("1) Show balance")
        print("2) Deposit")
        print("3) Withdraw")
        print("4) Transfer")
        print("5) Mini statement")
        print("0) Logout")
        c = input("Choice: ").strip()
        if c == "1": show_balance(db, acct)
        elif c == "2": deposit(db, acct)
        elif c == "3": withdraw(db, acct)
        elif c == "4": transfer(db, acct)
        elif c == "5": mini_statement(db, acct)
        elif c == "0": break
        else: print("Invalid option.")


def main():
    db = load_db()
    print("=== Welcome to SimpleBank CLI ===")
    while True:
        print("\nMain Menu:")
        print("1) Create account")
        print("2) Login")
        print("3) Admin login")
        print("0) Exit")
        c = input("Choice: ").strip()
        if c == "1": create_account(db)
        elif c == "2":
            acct = authenticate(db)
            if acct: account_menu(db, acct)
            db = load_db()
        elif c == "3":
            pwd = getpass.getpass("Admin password: ")
            if pwd == ADMIN_PASSWORD:
                admin_view(db)
            else:
                print("Wrong password.")
        elif c == "0":
            print("Goodbye.")
            sys.exit(0)
        else:
            print("Invalid option.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting. Goodbye.")
        sys.exit(0)
