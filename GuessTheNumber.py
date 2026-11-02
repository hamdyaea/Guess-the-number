#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
"""Guess a secret number from 1 to 20 using a lightweight Tkinter window."""
from __future__ import annotations
import secrets
import tkinter as tk


def compare(guess: int, secret: int) -> str:
    if not 1 <= guess <= 20:
        raise ValueError("Guess must be between 1 and 20")
    if not 1 <= secret <= 20:
        raise ValueError("Secret must be between 1 and 20")
    return "Correct!" if guess == secret else ("Too low" if guess < secret else "Too high")


class GuessApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Guess the Number · Hamdy Abou El Anein")
        self.geometry("430x350")
        self.minsize(360, 320)
        self.configure(bg="#101827")
        self.message = tk.StringVar(value="Choose a number between 1 and 20.")
        self.count = 0
        self.secret = 1
        self.value = tk.StringVar()
        box = tk.Frame(self, bg="#101827", padx=28, pady=25)
        box.pack(fill="both", expand=True)
        tk.Label(box, text="GUESS THE NUMBER", bg="#101827", fg="#8bd6c1",
                 font=("DejaVu Sans", 14, "bold")).pack(pady=10)
        tk.Label(box, text="1 — 20", bg="#101827", fg="#f2c879",
                 font=("DejaVu Sans", 34, "bold")).pack(pady=10)
        self.entry = tk.Entry(box, textvariable=self.value, justify="center", width=9,
                              font=("DejaVu Sans", 18))
        self.entry.pack(pady=5)
        tk.Label(box, textvariable=self.message, bg="#101827", fg="#e2eaf4",
                 font=("DejaVu Sans", 11), wraplength=340).pack(pady=13)
        buttons = tk.Frame(box, bg="#101827")
        buttons.pack()
        self.submit = tk.Button(buttons, text="Guess", command=self.guess, bg="#7ddcc0",
                                fg="#10211c", relief="flat", padx=20, pady=9)
        self.submit.pack(side="left", padx=6)
        tk.Button(buttons, text="New game", command=self.reset, bg="#2a3a51",
                  fg="white", relief="flat", padx=15, pady=9).pack(side="left", padx=6)
        self.bind("<Return>", lambda _event: self.guess())
        self.reset()

    def reset(self) -> None:
        self.secret = secrets.randbelow(20) + 1
        self.count = 0
        self.value.set("")
        self.message.set("Choose a number between 1 and 20.")
        self.submit.config(state="normal")
        self.entry.focus_set()

    def guess(self) -> None:
        try:
            value = int(self.value.get().strip())
            result = compare(value, self.secret)
        except ValueError:
            self.message.set("Enter a whole number between 1 and 20.")
            return
        self.count += 1
        self.message.set(f"{result} · {self.count} attempt(s)")
        self.value.set("")
        if result == "Correct!":
            self.submit.config(state="disabled")


if __name__ == "__main__":
    GuessApp().mainloop()
