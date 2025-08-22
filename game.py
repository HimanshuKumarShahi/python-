import tkinter as tk
from tkinter import ttk, messagebox
import textwrap

# Mind Reader (binary card trick) — GUI
# No external dependencies. Works with Python's built-in tkinter.

CARD_COUNT = 6  # 6 cards handle numbers 1..63

def build_cards(max_num=63):
    """Return list of cards. Each card is a sorted list of ints.
       Cards are built so that card i contains numbers with bit i set (1-based numbering).
    """
    cards = []
    for bit in range(CARD_COUNT):
        card = [n for n in range(1, max_num+1) if (n >> bit) & 1]
        cards.append(card)
    return cards

class MindReaderApp:
    def __init__(self, root):
        self.root = root
        root.title("Mind Reader — Guess Your Number")
        root.geometry("720x520")
        root.minsize(640, 480)
        self.style = ttk.Style(root)
        # Try default theme then fallback
        try:
            self.style.theme_use("clam")
        except Exception:
            pass

        self.cards = build_cards()
        self.current = 0
        self.total = 0
        self.max_num = 2**CARD_COUNT - 1

        self._build_ui()
        self._show_intro()

    def _build_ui(self):
        self.frame = ttk.Frame(self.root, padding=12)
        self.frame.pack(fill=tk.BOTH, expand=True)

        title = ttk.Label(self.frame, text="🧠 Mind Reader", font=("Segoe UI", 20, "bold"))
        title.pack(anchor=tk.N, pady=(2,8))

        subtitle = ttk.Label(self.frame, text=f"Think of a number between 1 and {self.max_num} (inclusive).", font=("Segoe UI", 11))
        subtitle.pack(anchor=tk.N)

        self.card_box = ttk.Frame(self.frame)
        self.card_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=12)

        # Card title
        self.card_title = ttk.Label(self.card_box, text="", font=("Segoe UI", 14, "bold"))
        self.card_title.pack(anchor=tk.N, pady=(6,4))

        # Numbers display area (use text widget for easy wrap)
        self.numbers_text = tk.Text(self.card_box, height=12, wrap=tk.WORD, state=tk.DISABLED,
                                    font=("Consolas", 11), bg="#f7f7f7")
        self.numbers_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=6)

        # Buttons
        btn_frame = ttk.Frame(self.frame)
        btn_frame.pack(fill=tk.X, pady=(2,12), padx=20)

        self.yes_btn = ttk.Button(btn_frame, text="Yes — It's on this card", command=self.on_yes)
        self.yes_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0,6))

        self.no_btn = ttk.Button(btn_frame, text="No — Not on this card", command=self.on_no)
        self.no_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(6,0))

        control_frame = ttk.Frame(self.frame)
        control_frame.pack(fill=tk.X, padx=20)

        self.replay_btn = ttk.Button(control_frame, text="Play Again", command=self.reset, state=tk.DISABLED)
        self.replay_btn.pack(side=tk.RIGHT)

        self.explain_btn = ttk.Button(control_frame, text="How does it work?", command=self.show_explanation)
        self.explain_btn.pack(side=tk.RIGHT, padx=(0,8))

        self.hint_label = ttk.Label(self.frame, text="Tip: Don't tell the program the number — only answer if the number appears on each card.", wraplength=680)
        self.hint_label.pack(pady=(8,2))

    def _show_intro(self):
        self.current = 0
        self.total = 0
        self._show_card()

    def _show_card(self):
        # If finished
        if self.current >= len(self.cards):
            self._reveal()
            return

        card = self.cards[self.current]
        bit_value = 1 << self.current
        self.card_title.config(text=f"Card {self.current + 1} — Numbers with bit value {bit_value}")
        # Format numbers in columns
        lines = []
        per_row = 8
        row = []
        for i, n in enumerate(card, start=1):
            row.append(f"{n:2d}")
            if i % per_row == 0:
                lines.append("  ".join(row))
                row = []
        if row:
            lines.append("  ".join(row))

        display = "\n".join(lines) if lines else "(no numbers on this card)"
        # Show in text widget
        self.numbers_text.config(state=tk.NORMAL)
        self.numbers_text.delete("1.0", tk.END)
        self.numbers_text.insert(tk.END, display)
        self.numbers_text.config(state=tk.DISABLED)

        # Enable buttons
        self.yes_btn.config(state=tk.NORMAL)
        self.no_btn.config(state=tk.NORMAL)
        self.replay_btn.config(state=tk.DISABLED)

    def on_yes(self):
        bit_value = 1 << self.current
        self.total += bit_value
        # Simple cheeky UI effect: flash text
        self._flash(f"Added {bit_value} (bit {self.current}) — running total: {self.total}")
        self.current += 1
        self._show_card()

    def on_no(self):
        self._flash(f"No bit {self.current} added — running total: {self.total}")
        self.current += 1
        self._show_card()

    def _flash(self, message):
        # temporary small message in hint label
        old = self.hint_label.cget("text")
        self.hint_label.config(text=message)
        self.root.after(800, lambda: self.hint_label.config(text=old))

    def _reveal(self):
        # Buttons disabled
        self.yes_btn.config(state=tk.DISABLED)
        self.no_btn.config(state=tk.DISABLED)
        # If total 0 maybe user thought of 0 or answered all no — handle it
        if self.total < 1 or self.total > self.max_num:
            msg = f"I think you picked... {self.total}.\nHmm — that seems outside 1–{self.max_num}. Did you follow instructions?"
            messagebox.showinfo("Mind Read Result", msg)
        else:
            # celebratory reveal
            msg = f"🎉 I read your mind! Your number is {self.total}."
            messagebox.showinfo("Mind Read Result", msg)
        self.replay_btn.config(state=tk.NORMAL)

    def reset(self):
        self.current = 0
        self.total = 0
        self.replay_btn.config(state=tk.DISABLED)
        self._show_card()

    def show_explanation(self):
        expl = """
        This is the classic binary card trick.

        Each card corresponds to one binary digit (a "bit").
        When you say 'Yes' for a card, you are telling me that
        the bit for that card is 1 in your number.

        The program adds up the bit values for every 'Yes' answer.
        The final sum reconstructs your original number!

        Example:
          - If your number has bits 1 and 4 set (values 1 and 8),
            the program will add 1 + 8 = 9 → your number is 9.

        Try thinking of any number between 1 and 63 and watch the magic.
        """
        messagebox.showinfo("How the trick works", textwrap.dedent(expl).strip())


if __name__ == "__main__":
    root = tk.Tk()
    app = MindReaderApp(root)
    root.mainloop()
