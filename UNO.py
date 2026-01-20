# from tkinter import *
# from tkinter import messagebox, simpledialog
# import random

# # ==================== CONSTANTS ====================
# COLORS = ["Red", "Green", "Blue", "Yellow"]
# VALUES = list(range(0, 10))
# ACTIONS = ["Skip", "Reverse", "Draw Two"]
# CARD_WIDTH = 90
# CARD_HEIGHT = 120

# # ==================== DECK CREATION ====================
# def create_deck():
#     """Create a standard UNO deck with 108 cards"""
#     deck = []
    
#     # Number cards: 0 (one per color), 1-9 (two per color)
#     for color in COLORS:
#         deck.append((color, "0"))
#         for value in range(1, 10):
#             deck.extend([(color, str(value)), (color, str(value))])
    
#     # Action cards: 2 of each per color
#     for color in COLORS:
#         for action in ACTIONS:
#             deck.extend([(color, action), (color, action)])
    
#     # Wild cards: 4 Wild and 4 Wild Draw Four
#     for _ in range(4):
#         deck.extend([("Wild", "Wild"), ("Wild", "Wild Draw Four")])
    
#     random.shuffle(deck)
#     return deck

# # ==================== UNO GAME CLASS ====================
# class UnoGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title(" UNO Card Game")
#         self.root.geometry("1400x850")
#         self.root.config(bg="#16213e")
#         self.root.resizable(False, False)
        
#         # Game state
#         self.deck = create_deck()
#         self.discard_pile = []
#         self.player_hand = []
#         self.computer_hand = []
#         self.current_card = None
#         self.current_player = "player"
#         self.game_direction = 1
#         self.draw_stack = 0
#         self.player_said_uno = False
#         self.computer_said_uno = False
#         self.game_over = False
#         self.skip_next = False
#         self.wild_color = None
#         self.drawn_this_turn = False
        
#         # Initialize game
#         self.deal_initial_cards()
#         self.build_ui()
#         self.update_display()
    
#     def deal_initial_cards(self):
#         """Deal 7 cards to each player and set first card"""
#         # Deal 7 cards to each player
#         for _ in range(7):
#             self.player_hand.append(self.deck.pop())
#             self.computer_hand.append(self.deck.pop())
        
#         # Find valid starting card (not Wild or action)
#         while True:
#             self.current_card = self.deck.pop()
#             color, value = self.current_card
#             if color != "Wild" and value in [str(i) for i in range(10)]:
#                 break
#             self.deck.insert(0, self.current_card)
        
#         self.discard_pile.append(self.current_card)
    
#     # ==================== UI CONSTRUCTION ====================
#     def build_ui(self):
#         """Build the entire user interface"""
#         # Header
#         header = Frame(self.root, bg="#0f3460", height=80)
#         header.pack(fill=X, pady=(0, 10))
        
#         Label(header, text=" UNO GAME ", font=("Arial", 32, "bold"),
#               bg="#0f3460", fg="#00d4ff").pack(pady=15)
        
#         # Game status bar
#         self.status_frame = Frame(self.root, bg="#16213e")
#         self.status_frame.pack(fill=X, padx=20, pady=5)
        
#         self.status_label = Label(self.status_frame, text="", font=("Arial", 14, "bold"),
#                                   bg="#16213e", fg="#ffffff", height=2)
#         self.status_label.pack()
        
#         # Computer hand section
#         comp_frame = Frame(self.root, bg="#16213e")
#         comp_frame.pack(pady=15)
        
#         Label(comp_frame, text="💻 Computer", font=("Arial", 16, "bold"),
#               bg="#16213e", fg="#ff6b6b").pack()
        
#         self.comp_hand_frame = Frame(comp_frame, bg="#16213e")
#         self.comp_hand_frame.pack(pady=5)
        
#         # Center game area
#         center_frame = Frame(self.root, bg="#16213e")
#         center_frame.pack(pady=20)
        
#         # Draw pile
#         draw_frame = Frame(center_frame, bg="#16213e")
#         draw_frame.pack(side=LEFT, padx=40)
        
#         Label(draw_frame, text="DRAW PILE", font=("Arial", 11, "bold"),
#               bg="#16213e", fg="#ffffff").pack()
        
#         self.draw_btn = Button(draw_frame, text="🂠", font=("Arial", 48),
#                                width=4, height=2, bg="#1a1a2e", fg="#00d4ff",
#                                command=self.player_draw, cursor="hand2",
#                                relief=RAISED, bd=4)
#         self.draw_btn.pack(pady=5)
        
#         self.deck_count = Label(draw_frame, text="", font=("Arial", 10),
#                                 bg="#16213e", fg="#ffffff")
#         self.deck_count.pack()
        
#         # Discard pile (current card)
#         discard_frame = Frame(center_frame, bg="#16213e")
#         discard_frame.pack(side=LEFT, padx=40)
        
#         Label(discard_frame, text="CURRENT CARD", font=("Arial", 11, "bold"),
#               bg="#16213e", fg="#ffffff").pack()
        
#         self.current_card_canvas = Canvas(discard_frame, width=CARD_WIDTH+10,
#                                           height=CARD_HEIGHT+10, bg="#16213e",
#                                           highlightthickness=0)
#         self.current_card_canvas.pack(pady=5)
        
#         self.direction_label = Label(discard_frame, text="", font=("Arial", 12),
#                                      bg="#16213e", fg="#ffff00")
#         self.direction_label.pack()
        
#         # Player hand section
#         player_frame = Frame(self.root, bg="#16213e")
#         player_frame.pack(pady=15)
        
#         Label(player_frame, text="👤 Your Hand", font=("Arial", 16, "bold"),
#               bg="#16213e", fg="#00ff88").pack()
        
#         # Scrollable frame for player cards
#         player_canvas_frame = Frame(player_frame, bg="#16213e")
#         player_canvas_frame.pack(pady=5)
        
#         self.player_scroll_canvas = Canvas(player_canvas_frame, bg="#16213e", 
#                                            height=150, width=1200, highlightthickness=0)
#         self.player_scroll_canvas.pack()
        
#         self.player_hand_frame = Frame(self.player_scroll_canvas, bg="#16213e")
#         self.player_scroll_canvas.create_window((0, 0), window=self.player_hand_frame, anchor="nw")
        
#         # Control buttons
#         control_frame = Frame(self.root, bg="#16213e")
#         control_frame.pack(pady=15)
        
#         self.uno_btn = Button(control_frame, text=" UNO!", font=("Arial", 14, "bold"),
#                               bg="#ff0000", fg="white", width=10, height=2,
#                               command=self.call_uno, cursor="hand2", relief=RAISED, bd=3)
#         self.uno_btn.pack(side=LEFT, padx=8)
        
#         self.pass_btn = Button(control_frame, text="PASS", font=("Arial", 14, "bold"),
#                                bg="#ff8c00", fg="white", width=10, height=2,
#                                command=self.player_pass, cursor="hand2", relief=RAISED, bd=3)
#         self.pass_btn.pack(side=LEFT, padx=8)
        
#         Button(control_frame, text="NEW GAME", font=("Arial", 14, "bold"),
#                bg="#28a745", fg="white", width=12, height=2,
#                command=self.new_game, cursor="hand2", relief=RAISED, bd=3).pack(side=LEFT, padx=8)
    
#     # ==================== CARD DRAWING ====================
#     def draw_card_on_canvas(self, canvas, color, value, x=0, y=0):
#         """Draw a UNO card on a canvas"""
#         # Card background
#         if color == "Wild":
#             # Rainbow gradient effect for wild cards
#             segment_width = CARD_WIDTH // 4
#             colors_list = ["#ff0000", "#00ff00", "#0000ff", "#ffff00"]
#             for i, col in enumerate(colors_list):
#                 canvas.create_rectangle(x + i*segment_width, y, 
#                                        x + (i+1)*segment_width, y + CARD_HEIGHT,
#                                        fill=col, outline="")
#             # Inner black rectangle
#             canvas.create_rectangle(x+12, y+12, x+CARD_WIDTH-12, y+CARD_HEIGHT-12,
#                                    fill="black", outline="white", width=3)
#         else:
#             # Colored card
#             color_map = {"Red": "#e74c3c", "Green": "#27ae60",
#                         "Blue": "#3498db", "Yellow": "#f1c40f"}
#             bg_color = color_map.get(color, "#2c3e50")
            
#             # Card rectangle
#             canvas.create_rectangle(x, y, x + CARD_WIDTH, y + CARD_HEIGHT,
#                                    fill=bg_color, outline="white", width=4)
#             # Inner white oval
#             canvas.create_oval(x+18, y+25, x+CARD_WIDTH-18, y+CARD_HEIGHT-25,
#                               fill="white", outline="white", width=2)
        
#         # Card value/text
#         text_color = "black" if color in ["Yellow"] else "white"
#         if color == "Wild":
#             text_color = "white"
        
#         # Determine display text
#         if value == "Draw Two":
#             display_text = "+2"
#         elif value == "Wild Draw Four":
#             display_text = "+4"
#         elif value == "Skip":
#             display_text = "⊘"
#         elif value == "Reverse":
#             display_text = "⇄"
#         else:
#             display_text = value
        
#         # Main text (center)
#         font_size = 32 if value in ["Skip", "Reverse", "Draw Two", "Wild Draw Four"] else 36
#         canvas.create_text(x + CARD_WIDTH//2, y + CARD_HEIGHT//2,
#                           text=display_text, font=("Arial", font_size, "bold"),
#                           fill=text_color if color != "Wild" else "white")
        
#         # Corner values
#         corner_size = 12
#         canvas.create_text(x + 18, y + 18, text=display_text,
#                           font=("Arial", corner_size, "bold"), 
#                           fill=text_color if color != "Wild" else "white")
#         canvas.create_text(x + CARD_WIDTH - 18, y + CARD_HEIGHT - 18,
#                           text=display_text, font=("Arial", corner_size, "bold"), 
#                           fill=text_color if color != "Wild" else "white")
    
#     def create_card_button(self, parent, card, command=None):
#         """Create a clickable card button"""
#         color, value = card
#         can_play = self.can_play_card(card) and self.current_player == "player" and not self.game_over
        
#         card_frame = Frame(parent, bg="#16213e")
#         card_frame.pack(side=LEFT, padx=4)
        
#         canvas = Canvas(card_frame, width=CARD_WIDTH, height=CARD_HEIGHT,
#                        bg="#16213e", highlightthickness=0, 
#                        cursor="hand2" if can_play else "arrow")
#         canvas.pack()
        
#         # Always draw the card fully visible - no overlays
#         self.draw_card_on_canvas(canvas, color, value)
        
#         if can_play and command:
#             # Only playable cards can be clicked
#             canvas.bind("<Button-1>", lambda e: command(card))
#             # Hover effect - raise the card
#             def on_enter(e):
#                 canvas.configure(relief=RAISED, bd=3)
#             def on_leave(e):
#                 canvas.configure(relief=FLAT, bd=0)
#             canvas.bind("<Enter>", on_enter)
#             canvas.bind("<Leave>", on_leave)
    
#     # ==================== DISPLAY UPDATE ====================
#     def update_display(self):
#         """Update all UI elements"""
#         if self.game_over:
#             return
        
#         # Status bar
#         turn_text = "YOUR TURN" if self.current_player == "player" else "COMPUTER'S TURN"
#         stack_info = f" | Draw Stack: +{self.draw_stack}" if self.draw_stack > 0 else ""
        
#         status_text = (f"{turn_text} | 👤 Your Cards: {len(self.player_hand)} | "
#                       f"💻 Computer Cards: {len(self.computer_hand)}{stack_info}")
        
#         status_color = "#00ff88" if self.current_player == "player" else "#ff6b6b"
#         self.status_label.config(text=status_text, fg=status_color)
        
#         # Deck count
#         self.deck_count.config(text=f"📦 {len(self.deck)} cards")
        
#         # Current card
#         self.current_card_canvas.delete("all")
#         display_color, display_value = self.current_card
#         if self.wild_color and display_color == "Wild":
#             display_color = self.wild_color
#         self.draw_card_on_canvas(self.current_card_canvas, display_color, display_value, 5, 5)
        
#         # Direction indicator
#         direction_text = "➡️ Normal" if self.game_direction == 1 else "⬅️ Reversed"
#         self.direction_label.config(text=direction_text)
        
#         # Computer hand (face down)
#         for widget in self.comp_hand_frame.winfo_children():
#             widget.destroy()
        
#         for i in range(len(self.computer_hand)):
#             canvas = Canvas(self.comp_hand_frame, width=CARD_WIDTH, height=CARD_HEIGHT,
#                            bg="#16213e", highlightthickness=0)
#             canvas.pack(side=LEFT, padx=3)
            
#             # Card back
#             canvas.create_rectangle(0, 0, CARD_WIDTH, CARD_HEIGHT,
#                                    fill="#1a1a2e", outline="#ff6b6b", width=4)
#             canvas.create_text(CARD_WIDTH//2, CARD_HEIGHT//2, text="UNO",
#                               font=("Arial", 20, "bold"), fill="#ff6b6b")
#             canvas.create_text(CARD_WIDTH//2, CARD_HEIGHT//2 + 30, text="🂠",
#                               font=("Arial", 24), fill="#ff6b6b")
        
#         # Player hand - show all cards
#         for widget in self.player_hand_frame.winfo_children():
#             widget.destroy()
        
#         for card in self.player_hand:
#             self.create_card_button(self.player_hand_frame, card,
#                                    command=self.play_card)
        
#         # Update scroll region
#         self.player_hand_frame.update_idletasks()
#         self.player_scroll_canvas.config(scrollregion=self.player_scroll_canvas.bbox("all"))
        
#         # Button states
#         is_player_turn = self.current_player == "player" and not self.game_over
#         self.draw_btn.config(state=NORMAL if is_player_turn else DISABLED)
#         self.uno_btn.config(state=NORMAL if is_player_turn else DISABLED)
#         self.pass_btn.config(state=NORMAL if (is_player_turn and self.drawn_this_turn) else DISABLED)
    
#     # ==================== GAME LOGIC ====================
#     def can_play_card(self, card):
#         """Check if a card can be played"""
#         card_color, card_value = card
#         current_color, current_value = self.current_card
        
#         # Use wild color if set
#         if self.wild_color:
#             current_color = self.wild_color
        
#         # Wild cards can always be played
#         if card_color == "Wild":
#             return True
        
#         # If draw stack exists, only +2 or +4 can be played
#         if self.draw_stack > 0:
#             return card_value == "Draw Two" or (card_color == "Wild" and card_value == "Wild Draw Four")
        
#         # Normal matching: color or value
#         return card_color == current_color or card_value == current_value
    
#     def play_card(self, card):
#         """Player plays a card"""
#         if self.current_player != "player" or not self.can_play_card(card) or self.game_over:
#             return
        
#         # Check if player has 2 cards and should call UNO before playing
#         if len(self.player_hand) == 2 and not self.player_said_uno:
#             response = messagebox.askyesno("Call UNO?", 
#                 "You have 2 cards! Do you want to call UNO before playing?\n\n(If you don't call UNO now and play your second-to-last card, you'll get a penalty!)")
#             if response:
#                 self.player_said_uno = True
#                 messagebox.showinfo("UNO!", "✅ You called UNO!")
        
#         self.player_hand.remove(card)
#         self.discard_pile.append(card)
#         self.drawn_this_turn = False
        
#         # Handle wild cards
#         if card[0] == "Wild":
#             self.choose_wild_color(card)
#         else:
#             self.current_card = card
#             self.wild_color = None
#             self.apply_card_effect(card)
        
#         # Check for win
#         if len(self.player_hand) == 0:
#             self.end_game("🎉 CONGRATULATIONS! YOU WIN! 🎉")
#             return
        
#         # Check UNO status
#         if len(self.player_hand) == 1 and not self.player_said_uno:
#             self.root.after(1000, lambda: self.check_forgot_uno("player"))
        
#         # Reset UNO flag after playing down to 0 cards or if player has more than 1 card
#         if len(self.player_hand) != 1:
#             self.player_said_uno = False
        
#         # Handle turn switching
#         if self.skip_next:
#             self.skip_next = False
#             self.update_display()
#         else:
#             self.switch_turn()
    
#     def choose_wild_color(self, card):
#         """Let player choose color for wild card"""
#         dialog = Toplevel(self.root)
#         dialog.title("Choose Color")
#         dialog.geometry("400x180")
#         dialog.config(bg="#16213e")
#         dialog.transient(self.root)
#         dialog.grab_set()
        
#         # Center the dialog
#         dialog.geometry("+%d+%d" % (self.root.winfo_x() + 500, self.root.winfo_y() + 300))
        
#         Label(dialog, text="Choose a color for your Wild card:", 
#               font=("Arial", 14, "bold"),
#               bg="#16213e", fg="white").pack(pady=15)
        
#         btn_frame = Frame(dialog, bg="#16213e")
#         btn_frame.pack(pady=10)
        
#         colors = [("Red", "#e74c3c"), ("Green", "#27ae60"),
#                  ("Blue", "#3498db"), ("Yellow", "#f1c40f")]
        
#         for color, hex_color in colors:
#             text_color = "black" if color == "Yellow" else "white"
#             Button(btn_frame, text=color, font=("Arial", 13, "bold"),
#                    bg=hex_color, fg=text_color,
#                    width=9, height=2, 
#                    command=lambda c=color: self.set_wild_color(c, card, dialog),
#                    cursor="hand2", relief=RAISED, bd=3).pack(side=LEFT, padx=5)
        
#         dialog.wait_window()
    
#     def set_wild_color(self, color, card, dialog):
#         """Set the chosen color for wild card"""
#         self.wild_color = color
#         self.current_card = card
        
#         if card[1] == "Wild Draw Four":
#             self.draw_stack += 4
        
#         dialog.destroy()
#         self.apply_card_effect(card)
        
#         if not self.skip_next:
#             self.switch_turn()
    
#     def apply_card_effect(self, card):
#         """Apply special card effects"""
#         card_color, card_value = card
        
#         if card_value == "Skip":
#             self.skip_next = True
#         elif card_value == "Reverse":
#             self.game_direction *= -1
#             self.skip_next = True  # In 2-player, acts like skip
#         elif card_value == "Draw Two":
#             self.draw_stack += 2
    
#     def player_draw(self):
#         """Player draws card(s)"""
#         if self.current_player != "player" or self.game_over:
#             return
        
#         if self.draw_stack > 0:
#             # Draw penalty cards
#             cards_drawn = self.draw_stack
#             self.draw_cards(self.player_hand, cards_drawn)
#             self.draw_stack = 0
#             self.drawn_this_turn = False
#             self.update_display()
#             messagebox.showinfo("Cards Drawn", f"You drew {cards_drawn} penalty cards!")
#             self.switch_turn()
#         else:
#             # Normal draw
#             drawn_card = self.draw_cards(self.player_hand, 1)
#             self.drawn_this_turn = True
#             self.update_display()
            
#             # Check if drawn card is playable
#             if drawn_card and self.can_play_card(drawn_card):
#                 response = messagebox.askyesno("Playable Card!", 
#                     f"You drew a playable card: {drawn_card[0]} {drawn_card[1]}\n\nDo you want to play it now?")
#                 if response:
#                     self.play_card(drawn_card)
#                     return
            
#             # If not played, player can pass or keep it
    
#     def player_pass(self):
#         """Player passes turn after drawing"""
#         if self.current_player != "player" or not self.drawn_this_turn:
#             return
        
#         self.drawn_this_turn = False
#         self.switch_turn()
    
#     def computer_turn(self):
#         """Computer's turn logic"""
#         if self.game_over:
#             return
        
#         self.update_display()
#         self.root.update()
#         self.root.after(1000)
        
#         # Handle draw stack - computer MUST draw if can't counter
#         if self.draw_stack > 0:
#             # Check if computer can counter
#             can_counter = False
#             counter_card = None
            
#             # Can only counter +2 with +2, or +4 with +4
#             last_played = self.discard_pile[-1] if self.discard_pile else None
            
#             if last_played and last_played[1] == "Draw Two":
#                 # Can counter with another Draw Two
#                 plus_two = [c for c in self.computer_hand if c[1] == "Draw Two"]
#                 if plus_two:
#                     can_counter = True
#                     counter_card = random.choice(plus_two)
            
#             if last_played and last_played[1] == "Wild Draw Four":
#                 # Can only counter with Wild Draw Four
#                 wild_plus_four = [c for c in self.computer_hand if c[1] == "Wild Draw Four"]
#                 if wild_plus_four:
#                     can_counter = True
#                     counter_card = random.choice(wild_plus_four)
            
#             if can_counter and counter_card:
#                 # Counter with the card
#                 self.computer_play_card(counter_card)
#                 return
#             else:
#                 # Must draw all penalty cards
#                 cards_to_draw = self.draw_stack
#                 self.draw_cards(self.computer_hand, cards_to_draw)
#                 self.draw_stack = 0
#                 self.status_label.config(text=f"Computer drew {cards_to_draw} penalty cards!")
#                 self.root.update()
#                 self.root.after(1500)
#                 self.switch_turn()
#                 return
        
#         # Find playable cards
#         playable = [c for c in self.computer_hand if self.can_play_card(c)]
        
#         if playable:
#             # Strategy: prioritize action cards, save wilds
#             actions = [c for c in playable if c[1] in ACTIONS]
#             wilds = [c for c in playable if c[0] == "Wild"]
#             normal = [c for c in playable if c[0] != "Wild" and c[1] not in ACTIONS]
            
#             if actions:
#                 card = random.choice(actions)
#             elif normal:
#                 card = random.choice(normal)
#             else:
#                 card = random.choice(playable)
            
#             self.computer_play_card(card)
#         else:
#             # Must draw
#             self.draw_cards(self.computer_hand, 1)
#             self.root.after(500)
            
#             # Try to play drawn card
#             if self.can_play_card(self.computer_hand[-1]):
#                 self.root.after(500, lambda: self.computer_play_card(self.computer_hand[-1]))
#             else:
#                 self.switch_turn()
    
#     def computer_play_card(self, card):
#         """Computer plays a card"""
#         self.computer_hand.remove(card)
#         self.discard_pile.append(card)
        
#         # Handle wild cards
#         if card[0] == "Wild":
#             # Choose most common color in hand
#             color_count = {c: sum(1 for cd in self.computer_hand if cd[0] == c) for c in COLORS}
#             chosen = max(color_count, key=color_count.get)
#             self.wild_color = chosen if color_count[chosen] > 0 else random.choice(COLORS)
#             self.current_card = card
            
#             if card[1] == "Wild Draw Four":
#                 self.draw_stack += 4
            
#             self.status_label.config(text=f"Computer chose {self.wild_color}!")
#             self.root.update()
#             self.root.after(1000)
#         else:
#             self.current_card = card
#             self.wild_color = None
        
#         self.apply_card_effect(card)
        
#         # Check for win
#         if len(self.computer_hand) == 0:
#             self.end_game("COMPUTER WINS! Better luck next time!")
#             return
        
#         # Auto-call UNO
#         if len(self.computer_hand) == 1:
#             self.computer_said_uno = True
#             self.status_label.config(text=" Computer called UNO!", fg="#ff0000")
#             self.root.update()
#             self.root.after(1500)
#         else:
#             self.computer_said_uno = False
        
#         # Handle turn
#         if self.skip_next:
#             self.skip_next = False
#             self.update_display()
#             self.root.after(1000, self.computer_turn)
#         else:
#             self.switch_turn()
    
#     def switch_turn(self):
#         """Switch between player and computer"""
#         self.current_player = "computer" if self.current_player == "player" else "player"
#         self.update_display()
        
#         if self.current_player == "computer":
#             self.root.after(1000, self.computer_turn)
    
#     def draw_cards(self, hand, count):
#         """Draw cards from deck to hand"""
#         last_drawn = None
#         for _ in range(count):
#             if not self.deck:
#                 self.reshuffle_discard()
#             if self.deck:
#                 card = self.deck.pop()
#                 hand.append(card)
#                 last_drawn = card
#         self.update_display()
#         return last_drawn
    
#     def reshuffle_discard(self):
#         """Reshuffle discard pile into deck"""
#         if len(self.discard_pile) > 1:
#             self.deck = self.discard_pile[:-1]
#             self.discard_pile = [self.discard_pile[-1]]
#             random.shuffle(self.deck)
    
#     def call_uno(self):
#         """Player calls UNO"""
#         if len(self.player_hand) == 1:
#             self.player_said_uno = True
#             messagebox.showinfo("UNO!", "You called UNO!")
#         else:
#             messagebox.showwarning("Invalid", "You can only call UNO with 1 card!\nPenalty: Draw 2 cards")
#             self.draw_cards(self.player_hand, 2)
    
#     def check_forgot_uno(self, player):
#         """Check if player forgot to call UNO"""
#         if player == "player" and len(self.player_hand) == 1 and not self.player_said_uno:
#             messagebox.showwarning("Forgot UNO!", "You forgot to call UNO!\nPenalty: Draw 2 cards")
#             self.draw_cards(self.player_hand, 2)
    
#     def end_game(self, message):
#         """End the game"""
#         self.game_over = True
#         self.status_label.config(text=message, font=("Arial", 18, "bold"), fg="#ffff00")
#         self.update_display()
#         messagebox.showinfo("Game Over", message)
    
#     def new_game(self):
#         """Start a new game"""
#         self.deck = create_deck()
#         self.discard_pile = []
#         self.player_hand = []
#         self.computer_hand = []
#         self.current_player = "player"
#         self.game_direction = 1
#         self.draw_stack = 0
#         self.player_said_uno = False
#         self.computer_said_uno = False
#         self.game_over = False
#         self.skip_next = False
#         self.wild_color = None
#         self.drawn_this_turn = False
        
#         self.deal_initial_cards()
#         self.update_display()

# # ==================== MAIN ====================
# if __name__ == "__main__":
#     root = Tk()
#     game = UnoGame(root)
#     root.mainloop()







from tkinter import *
from tkinter import messagebox, simpledialog
import random


COLORS = ["Red", "Green", "Blue", "Yellow"]
VALUES = list(range(0, 10))
ACTIONS = ["Skip", "Reverse", "Draw Two"]
CARD_WIDTH = 90
CARD_HEIGHT = 120


def create_deck():
    """Create a standard UNO deck with 108 cards"""
    deck = []
    
    # Number cards: 0 (one per color), 1-9 (two per color)
    for color in COLORS:
        deck.append((color, "0"))
        for value in range(1, 10):
            deck.extend([(color, str(value)), (color, str(value))])
    
    # Action cards: 2 of each per color
    for color in COLORS:
        for action in ACTIONS:
            deck.extend([(color, action), (color, action)])
    
    # Wild cards: 4 Wild and 4 Wild Draw Four
    for _ in range(4):
        deck.extend([("Wild", "Wild"), ("Wild", "Wild Draw Four")])
    
    random.shuffle(deck)
    return deck


class UnoGame:
    def __init__(self, root):
        self.root = root
        self.root.title(" UNO Card Game")
        

        self.root.state('zoomed')  
        try:
            self.root.attributes('-zoomed', True) 
        except:
            pass
        
        # self.root.attributes('-fullscreen', True)
        
        self.root.config(bg="#16213e")
        self.root.resizable(True, True)
        
        
        self.root.bind('<Escape>', lambda e: self.toggle_fullscreen())
        
        
        self.deck = create_deck()
        self.discard_pile = []
        self.player_hand = []
        self.computer_hand = []
        self.current_card = None
        self.current_player = "player"
        self.game_direction = 1
        self.draw_stack = 0
        self.player_said_uno = False
        self.computer_said_uno = False
        self.game_over = False
        self.skip_next = False
        self.wild_color = None
        self.drawn_this_turn = False
        
        
        self.deal_initial_cards()
        self.build_ui()
        self.update_display()
    
    def deal_initial_cards(self):
        """Deal 7 cards to each player and set first card"""
        # Deal 7 cards to each player
        for _ in range(7):
            self.player_hand.append(self.deck.pop())
            self.computer_hand.append(self.deck.pop())
        
        # Find valid starting card 
        while True:
            self.current_card = self.deck.pop()
            color, value = self.current_card
            if color != "Wild" and value in [str(i) for i in range(10)]:
                break
            self.deck.insert(0, self.current_card)
        
        self.discard_pile.append(self.current_card)
    
    def build_ui(self):
        """Build the entire user interface"""
        # Header
        header = Frame(self.root, bg="#0f3460", height=80)
        header.pack(fill=X, pady=(0, 10))
        
        Label(header, text="🎴 UNO GAME 🎴", font=("Arial", 32, "bold"),
              bg="#0f3460", fg="#00d4ff").pack(pady=15)
        
        # Game status bar
        self.status_frame = Frame(self.root, bg="#16213e")
        self.status_frame.pack(fill=X, padx=20, pady=5)
        
        self.status_label = Label(self.status_frame, text="", font=("Arial", 14, "bold"),
                                  bg="#16213e", fg="#ffffff", height=2)
        self.status_label.pack()
        
        # Computer hand section
        comp_frame = Frame(self.root, bg="#16213e")
        comp_frame.pack(pady=15)
        
        Label(comp_frame, text="💻 Computer", font=("Arial", 16, "bold"),
              bg="#16213e", fg="#ff6b6b").pack()
        
        self.comp_hand_frame = Frame(comp_frame, bg="#16213e")
        self.comp_hand_frame.pack(pady=5)
        
        # Center game area
        center_frame = Frame(self.root, bg="#16213e")
        center_frame.pack(pady=20)
        
        # Draw pile
        draw_frame = Frame(center_frame, bg="#16213e")
        draw_frame.pack(side=LEFT, padx=40)
        
        Label(draw_frame, text="DRAW PILE", font=("Arial", 11, "bold"),
              bg="#16213e", fg="#ffffff").pack()
        
        self.draw_btn = Button(draw_frame, text="🂠", font=("Arial", 48),
                               width=4, height=2, bg="#1a1a2e", fg="#00d4ff",
                               command=self.player_draw, cursor="hand2",
                               relief=RAISED, bd=4)
        self.draw_btn.pack(pady=5)
        
        self.deck_count = Label(draw_frame, text="", font=("Arial", 10),
                                bg="#16213e", fg="#ffffff")
        self.deck_count.pack()
        
        # Current card
        discard_frame = Frame(center_frame, bg="#16213e")
        discard_frame.pack(side=LEFT, padx=40)
        
        Label(discard_frame, text="CURRENT CARD", font=("Arial", 11, "bold"),
              bg="#16213e", fg="#ffffff").pack()
        
        self.current_card_canvas = Canvas(discard_frame, width=CARD_WIDTH+10,
                                          height=CARD_HEIGHT+10, bg="#16213e",
                                          highlightthickness=0)
        self.current_card_canvas.pack(pady=5)
        
        self.direction_label = Label(discard_frame, text="", font=("Arial", 12),
                                     bg="#16213e", fg="#ffff00")
        self.direction_label.pack()
        
        # Player hand section
        player_frame = Frame(self.root, bg="#16213e")
        player_frame.pack(pady=15)
        
        Label(player_frame, text="👤 Your Hand", font=("Arial", 16, "bold"),
              bg="#16213e", fg="#00ff88").pack()
        
        # Scrollable frame for player cards
        player_canvas_frame = Frame(player_frame, bg="#16213e")
        player_canvas_frame.pack(pady=5, fill=BOTH, expand=True)
        
        # Get screen width for canvas
        screen_width = self.root.winfo_screenwidth()
        self.player_scroll_canvas = Canvas(player_canvas_frame, bg="#16213e", 
                                           height=150, width=screen_width-100, highlightthickness=0)
        self.player_scroll_canvas.pack(fill=BOTH, expand=True)
        
        self.player_hand_frame = Frame(self.player_scroll_canvas, bg="#16213e")
        self.player_scroll_canvas.create_window((0, 0), window=self.player_hand_frame, anchor="nw")
        
        # Control buttons
        control_frame = Frame(self.root, bg="#16213e")
        control_frame.pack(pady=15)
        
        self.uno_btn = Button(control_frame, text="UNO!", font=("Arial", 14, "bold"),
                              bg="#ff0000", fg="white", width=10, height=2,
                              command=self.call_uno, cursor="hand2", relief=RAISED, bd=3)
        self.uno_btn.pack(side=LEFT, padx=8)
        
        self.pass_btn = Button(control_frame, text="PASS", font=("Arial", 14, "bold"),
                               bg="#ff8c00", fg="white", width=10, height=2,
                               command=self.player_pass, cursor="hand2", relief=RAISED, bd=3)
        self.pass_btn.pack(side=LEFT, padx=8)
        
        Button(control_frame, text="NEW GAME", font=("Arial", 14, "bold"),
               bg="#28a745", fg="white", width=12, height=2,
               command=self.new_game, cursor="hand2", relief=RAISED, bd=3).pack(side=LEFT, padx=8)
    
    def draw_card_on_canvas(self, canvas, color, value, x=0, y=0):
        """Draw a UNO card on a canvas"""
        # Card background
        if color == "Wild":
            # Rainbow effect for wild cards
            segment_width = CARD_WIDTH // 4
            colors_list = ["#ff0000", "#00ff00", "#0000ff", "#ffff00"]
            for i, col in enumerate(colors_list):
                canvas.create_rectangle(x + i*segment_width, y, 
                                       x + (i+1)*segment_width, y + CARD_HEIGHT,
                                       fill=col, outline="")
            # Inner black rectangle
            canvas.create_rectangle(x+12, y+12, x+CARD_WIDTH-12, y+CARD_HEIGHT-12,
                                   fill="black", outline="white", width=3)
        else:
            # Colored card
            color_map = {"Red": "#e74c3c", "Green": "#27ae60",
                        "Blue": "#3498db", "Yellow": "#f1c40f"}
            bg_color = color_map.get(color, "#2c3e50")
            
            # Card rectangle
            canvas.create_rectangle(x, y, x + CARD_WIDTH, y + CARD_HEIGHT,
                                   fill=bg_color, outline="white", width=4)
            # Inner white oval
            canvas.create_oval(x+18, y+25, x+CARD_WIDTH-18, y+CARD_HEIGHT-25,
                              fill="white", outline="white", width=2)
        
        # Card value/text
        text_color = "black" if color in ["Yellow","Red","Green","Blue"] else "white"
        if color == "Wild":
            text_color = "white"
        
        # Determine display text
        if value == "Draw Two":
            display_text = "+2"
        elif value == "Wild Draw Four":
            display_text = "+4"
        elif value == "Skip":
            display_text = "⊘"
        elif value == "Reverse":
            display_text = "⇄"
        else:
            display_text = value
        
        # Main text (center)
        font_size = 32 if value in ["Skip", "Reverse", "Draw Two", "Wild Draw Four"] else 36
        canvas.create_text(x + CARD_WIDTH//2, y + CARD_HEIGHT//2,
                          text=display_text, font=("Arial", font_size, "bold"),
                          fill=text_color if color != "Wild" else "white")
        
        # Corner values
        corner_size = 12
        canvas.create_text(x + 18, y + 18, text=display_text,
                          font=("Arial", corner_size, "bold"), 
                          fill=text_color if color != "Wild" else "white")
        canvas.create_text(x + CARD_WIDTH - 18, y + CARD_HEIGHT - 18,
                          text=display_text, font=("Arial", corner_size, "bold"), 
                          fill=text_color if color != "Wild" else "white")
    
    def create_card_button(self, parent, card, command=None):
        """Create a clickable card button"""
        color, value = card
        can_play = self.can_play_card(card) and self.current_player == "player" and not self.game_over
        
        card_frame = Frame(parent, bg="#16213e")
        card_frame.pack(side=LEFT, padx=4)
        
        canvas = Canvas(card_frame, width=CARD_WIDTH, height=CARD_HEIGHT,
                       bg="#16213e", highlightthickness=0, 
                       cursor="hand2" if can_play else "arrow")
        canvas.pack()
        
        
        self.draw_card_on_canvas(canvas, color, value)
        
        if can_play and command:
            # Only playable cards can be clicked
            canvas.bind("<Button-1>", lambda e: command(card))
            # Hover effect - raise the card
            def on_enter(e):
                canvas.configure(relief=RAISED, bd=3)
            def on_leave(e):
                canvas.configure(relief=FLAT, bd=0)
            canvas.bind("<Enter>", on_enter)
            canvas.bind("<Leave>", on_leave)
    
   
    def update_display(self):
        """Update all UI elements"""
        if self.game_over:
            return
        
        # Status bar
        turn_text = "YOUR TURN" if self.current_player == "player" else " COMPUTER'S TURN"
        stack_info = f" | 📚 Draw Stack: +{self.draw_stack}" if self.draw_stack > 0 else ""
        
        status_text = (f"{turn_text} | 👤 Your Cards: {len(self.player_hand)} | "
                      f"💻 Computer Cards: {len(self.computer_hand)}{stack_info}")
        
        status_color = "#00ff88" if self.current_player == "player" else "#ff6b6b"
        self.status_label.config(text=status_text, fg=status_color)
        
        # Deck count
        self.deck_count.config(text=f"📦 {len(self.deck)} cards")
        
        # Current card
        self.current_card_canvas.delete("all")
        display_color, display_value = self.current_card
        if self.wild_color and display_color == "Wild":
            display_color = self.wild_color
        self.draw_card_on_canvas(self.current_card_canvas, display_color, display_value, 5, 5)
        
        # Direction indicator
        direction_text = "➡️ Normal" if self.game_direction == 1 else "⬅️ Reversed"
        self.direction_label.config(text=direction_text)
        
        # Computer hand (face down)
        for widget in self.comp_hand_frame.winfo_children():
            widget.destroy()
        
        for i in range(len(self.computer_hand)):
            canvas = Canvas(self.comp_hand_frame, width=CARD_WIDTH, height=CARD_HEIGHT,
                           bg="#16213e", highlightthickness=0)
            canvas.pack(side=LEFT, padx=3)
            
            # Card back
            canvas.create_rectangle(0, 0, CARD_WIDTH, CARD_HEIGHT,
                                   fill="#1a1a2e", outline="#ff6b6b", width=4)
            canvas.create_text(CARD_WIDTH//2, CARD_HEIGHT//2, text="UNO",
                              font=("Arial", 20, "bold"), fill="#ff6b6b")
            canvas.create_text(CARD_WIDTH//2, CARD_HEIGHT//2 + 30, text="🂠",
                              font=("Arial", 24), fill="#ff6b6b")
        
        # Player hand - show all cards
        for widget in self.player_hand_frame.winfo_children():
            widget.destroy()
        
        for card in self.player_hand:
            self.create_card_button(self.player_hand_frame, card,
                                   command=self.play_card)
        
        # Update scroll region
        self.player_hand_frame.update_idletasks()
        self.player_scroll_canvas.config(scrollregion=self.player_scroll_canvas.bbox("all"))
        
        # Button states
        is_player_turn = self.current_player == "player" and not self.game_over
        self.draw_btn.config(state=NORMAL if is_player_turn else DISABLED)
        self.uno_btn.config(state=NORMAL if is_player_turn else DISABLED)
        self.pass_btn.config(state=NORMAL if (is_player_turn and self.drawn_this_turn) else DISABLED)
    
   
    def can_play_card(self, card):
        """Check if a card can be played"""
        card_color, card_value = card
        current_color, current_value = self.current_card
        
        # Use wild color if set
        if self.wild_color:
            current_color = self.wild_color
        
        # Wild cards can always be played
        if card_color == "Wild":
            return True
        
        # If draw stack exists, only +2 or +4 can be played
        if self.draw_stack > 0:
            return card_value == "Draw Two" or (card_color == "Wild" and card_value == "Wild Draw Four")
        
        # Normal matching: color or value
        return card_color == current_color or card_value == current_value
    
    def play_card(self, card):
        """Player plays a card"""
        if self.current_player != "player" or not self.can_play_card(card) or self.game_over:
            return
        
        # Check if player has 2 cards and should call UNO before playing
        if len(self.player_hand) == 2 and not self.player_said_uno:
            response = messagebox.askyesno("Call UNO?", 
                "You have 2 cards! Do you want to call UNO before playing?\n\n(If you don't call UNO now and play your second-to-last card, you'll get a penalty!)")
            if response:
                self.player_said_uno = True
                messagebox.showinfo("UNO!", "You called UNO!")
        
        self.player_hand.remove(card)
        self.discard_pile.append(card)
        self.drawn_this_turn = False
        
        # Handle wild cards
        if card[0] == "Wild":
            self.choose_wild_color(card)
        else:
            self.current_card = card
            self.wild_color = None
            self.apply_card_effect(card)
        
        # Check for win
        if len(self.player_hand) == 0:
            self.end_game("🎉 CONGRATULATIONS! YOU WIN! 🎉")
            return
        
        # Check UNO status
        if len(self.player_hand) == 1 and not self.player_said_uno:
            self.root.after(1000, lambda: self.check_forgot_uno("player"))
        
        # Reset UNO flag after playing down to 0 cards or if player has more than 1 card
        if len(self.player_hand) != 1:
            self.player_said_uno = False
        
        # Handle turn switching
        if self.skip_next:
            self.skip_next = False
            self.update_display()
        else:
            self.switch_turn()
    
    def choose_wild_color(self, card):
        """Let player choose color for wild card"""
        dialog = Toplevel(self.root)
        dialog.title("Choose Color")
        dialog.geometry("400x180")
        dialog.config(bg="#16213e")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.geometry("+%d+%d" % (self.root.winfo_x() + 500, self.root.winfo_y() + 300))
        
        Label(dialog, text="Choose a color for your Wild card:", 
              font=("Arial", 14, "bold"),
              bg="#16213e", fg="white").pack(pady=15)
        
        btn_frame = Frame(dialog, bg="#16213e")
        btn_frame.pack(pady=10)
        
        colors = [("Red", "#e74c3c"), ("Green", "#27ae60"),
                 ("Blue", "#3498db"), ("Yellow", "#f1c40f")]
        
        for color, hex_color in colors:
            text_color = "black" if color == "Yellow" else "white"
            Button(btn_frame, text=color, font=("Arial", 13, "bold"),
                   bg=hex_color, fg=text_color,
                   width=9, height=2, 
                   command=lambda c=color: self.set_wild_color(c, card, dialog),
                   cursor="hand2", relief=RAISED, bd=3).pack(side=LEFT, padx=5)
        
        dialog.wait_window()
    
    def set_wild_color(self, color, card, dialog):
        """Set the chosen color for wild card"""
        self.wild_color = color
        self.current_card = card
        
        if card[1] == "Wild Draw Four":
            self.draw_stack += 4
        
        dialog.destroy()
        self.apply_card_effect(card)
        
        if not self.skip_next:
            self.switch_turn()
    
    def apply_card_effect(self, card):
        """Apply special card effects"""
        card_color, card_value = card
        
        if card_value == "Skip":
            self.skip_next = True
        elif card_value == "Reverse":
            self.game_direction *= -1
            self.skip_next = True  
        elif card_value == "Draw Two":
            self.draw_stack += 2
    
    # def player_draw(self):
    #     """Player draws card(s)"""
    #     if self.current_player != "player" or self.game_over:
    #         return
        
    #     if self.draw_stack > 0:
    #         # Draw penalty cards
    #         cards_drawn = self.draw_stack
    #         self.draw_cards(self.player_hand, cards_drawn)
    #         self.draw_stack = 0
    #         self.drawn_this_turn = False
    #         self.update_display()
    #         messagebox.showinfo("Cards Drawn", f"You drew {cards_drawn} penalty cards!")
    #         self.switch_turn()
    #     else:
    #         # Normal draw
    #         drawn_card = self.draw_cards(self.player_hand, 1)
    #         self.drawn_this_turn = True
    #         self.update_display()
            
    #         # Check if drawn card is playable
    #         if drawn_card and self.can_play_card(drawn_card):
    #             response = messagebox.askyesno("Playable Card!", 
    #                 f"You drew a playable card: {drawn_card[0]} {drawn_card[1]}\n\nDo you want to play it now?")
    #             if response:
    #                 self.play_card(drawn_card)
    #                 return
            
    #         # If not played, player can pass or keep it
    def player_draw(self):
        """Player draws card(s)"""
        if self.current_player != "player" or self.game_over:
            return
        
        if self.draw_stack > 0:
            # Draw penalty cards
            cards_drawn = self.draw_stack
            self.draw_cards(self.player_hand, cards_drawn)
            self.draw_stack = 0
            self.drawn_this_turn = False
            self.update_display()
            messagebox.showinfo("Cards Drawn", f"You drew {cards_drawn} penalty cards!")
            self.switch_turn()
        else:
            # Normal draw - only draw ONE card
            drawn_card = self.draw_cards(self.player_hand, 1)
            self.drawn_this_turn = True
            self.update_display()
            
            # Check if drawn card is playable
            if drawn_card and self.can_play_card(drawn_card):
                response = messagebox.askyesno("Playable Card!", 
                    f"You drew a playable card: {drawn_card[0]} {drawn_card[1]}\n\nDo you want to play it now?")
                if response:
                    self.play_card(drawn_card)
                    return
                else:
                    # Player chose not to play it, turn ends
                    self.drawn_this_turn = False
                    self.switch_turn()
            else:
                # Card is not playable, turn ends automatically
                messagebox.showinfo("Cannot Play", "The drawn card cannot be played. Your turn ends.")
                self.drawn_this_turn = False
                self.switch_turn()
    
    def player_pass(self):
        """Player passes turn after drawing"""
        if self.current_player != "player" or not self.drawn_this_turn:
            return
        
        self.drawn_this_turn = False
        self.switch_turn()
    
    def computer_turn(self):
        """Computer's turn logic"""
        if self.game_over:
            return
        
        self.update_display()
        self.root.update()
        self.root.after(1000)
        
        # Handle draw stack - computer MUST draw if can't counter
        if self.draw_stack > 0:
            # Check if computer can counter
            can_counter = False
            counter_card = None
            
            # Can only counter +2 with +2, or +4 with +4
            last_played = self.discard_pile[-1] if self.discard_pile else None
            
            if last_played and last_played[1] == "Draw Two":
                # Can counter with another Draw Two
                plus_two = [c for c in self.computer_hand if c[1] == "Draw Two"]
                if plus_two:
                    can_counter = True
                    counter_card = random.choice(plus_two)
            
            if last_played and last_played[1] == "Wild Draw Four":
                # Can only counter with Wild Draw Four
                wild_plus_four = [c for c in self.computer_hand if c[1] == "Wild Draw Four"]
                if wild_plus_four:
                    can_counter = True
                    counter_card = random.choice(wild_plus_four)
            
            if can_counter and counter_card:
                # Counter with the card
                self.computer_play_card(counter_card)
                return
            else:
                # Must draw all penalty cards
                cards_to_draw = self.draw_stack
                self.draw_cards(self.computer_hand, cards_to_draw)
                self.draw_stack = 0
                self.status_label.config(text=f"💻 Computer drew {cards_to_draw} penalty cards!")
                self.root.update()
                self.root.after(1500)
                self.switch_turn()
                return
        
        # Find playable cards
        playable = [c for c in self.computer_hand if self.can_play_card(c)]
        
        if playable:
            # Strategy: prioritize action cards, save wilds
            actions = [c for c in playable if c[1] in ACTIONS]
            wilds = [c for c in playable if c[0] == "Wild"]
            normal = [c for c in playable if c[0] != "Wild" and c[1] not in ACTIONS]
            
            if actions:
                card = random.choice(actions)
            elif normal:
                card = random.choice(normal)
            else:
                card = random.choice(playable)
            
            self.computer_play_card(card)
        else:
            # Must draw
            self.draw_cards(self.computer_hand, 1)
            self.root.after(500)
            
            # Try to play drawn card
            if self.can_play_card(self.computer_hand[-1]):
                self.root.after(500, lambda: self.computer_play_card(self.computer_hand[-1]))
            else:
                self.switch_turn()
    
    def computer_play_card(self, card):
        """Computer plays a card"""
        self.computer_hand.remove(card)
        self.discard_pile.append(card)
        
        # Handle wild cards
        if card[0] == "Wild":
            # Choose most common color in hand
            color_count = {c: sum(1 for cd in self.computer_hand if cd[0] == c) for c in COLORS}
            chosen = max(color_count, key=color_count.get)
            self.wild_color = chosen if color_count[chosen] > 0 else random.choice(COLORS)
            self.current_card = card
            
            if card[1] == "Wild Draw Four":
                self.draw_stack += 4
            
            self.status_label.config(text=f"💻 Computer chose {self.wild_color}!")
            self.root.update()
            self.root.after(1000)
        else:
            self.current_card = card
            self.wild_color = None
        
        self.apply_card_effect(card)
        
        # Check for win
        if len(self.computer_hand) == 0:
            self.end_game("💻 COMPUTER WINS! Better luck next time!")
            return
        
        # Auto-call UNO
        if len(self.computer_hand) == 1:
            self.computer_said_uno = True
            self.status_label.config(text="🔔 Computer called UNO!", fg="#ff0000")
            self.root.update()
            self.root.after(1500)
        else:
            self.computer_said_uno = False
        
        # Handle turn
        if self.skip_next:
            self.skip_next = False
            self.update_display()
            self.root.after(1000, self.computer_turn)
        else:
            self.switch_turn()
    
    def switch_turn(self):
        """Switch between player and computer"""
        self.current_player = "computer" if self.current_player == "player" else "player"
        self.update_display()
        
        if self.current_player == "computer":
            self.root.after(1000, self.computer_turn)
    
    def draw_cards(self, hand, count):
        """Draw cards from deck to hand"""
        last_drawn = None
        for _ in range(count):
            if not self.deck:
                self.reshuffle_discard()
            if self.deck:
                card = self.deck.pop()
                hand.append(card)
                last_drawn = card
        self.update_display()
        return last_drawn
    
    def reshuffle_discard(self):
        """Reshuffle discard pile into deck"""
        if len(self.discard_pile) > 1:
            self.deck = self.discard_pile[:-1]
            self.discard_pile = [self.discard_pile[-1]]
            random.shuffle(self.deck)
    
    def call_uno(self):
        """Player calls UNO"""
        if len(self.player_hand) == 1:
            self.player_said_uno = True
            messagebox.showinfo("UNO!", " You called UNO!")
        else:
            messagebox.showwarning("Invalid", " You can only call UNO with 1 card!\nPenalty: Draw 2 cards")
            self.draw_cards(self.player_hand, 2)
    
    def check_forgot_uno(self, player):
        """Check if player forgot to call UNO"""
        if player == "player" and len(self.player_hand) == 1 and not self.player_said_uno:
            messagebox.showwarning("Forgot UNO!", " You forgot to call UNO!\nPenalty: Draw 2 cards")
            self.draw_cards(self.player_hand, 2)
    
    def toggle_fullscreen(self):
        """Toggle fullscreen mode"""
        try:
            is_fullscreen = self.root.attributes('-fullscreen')
            self.root.attributes('-fullscreen', not is_fullscreen)
        except:
            pass
    
    def end_game(self, message):
        """End the game"""
        self.game_over = True
        self.status_label.config(text=message, font=("Arial", 18, "bold"), fg="#ffff00")
        self.update_display()
        messagebox.showinfo("Game Over", message)
    
    def new_game(self):
        """Start a new game"""
        self.deck = create_deck()
        self.discard_pile = []
        self.player_hand = []
        self.computer_hand = []
        self.current_player = "player"
        self.game_direction = 1
        self.draw_stack = 0
        self.player_said_uno = False
        self.computer_said_uno = False
        self.game_over = False
        self.skip_next = False
        self.wild_color = None
        self.drawn_this_turn = False
        
        self.deal_initial_cards()
        self.update_display()

if __name__ == "__main__":
    root = Tk()
    game = UnoGame(root)
    root.mainloop()