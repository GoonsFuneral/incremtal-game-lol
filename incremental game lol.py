import tkinter as tk

class IncrementalBodyStrengthGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Incremental Game: Body Strengthening to Magic")

        # Initial attributes
        self.strength = 0
        self.dexterity = 0
        self.mana = 0
        self.energy = 100  # Starting energy
        self.energy_cap = 100  # Starting energy cap
        self.xp = 0
        self.level = 1
        self.training_cost = 10  # Initial energy cost for basic training
        self.magic_unlocked = False

        # Labels for attributes
        self.strength_label = tk.Label(master, text=f"Strength: {self.strength}")
        self.strength_label.pack()
        self.dexterity_label = tk.Label(master, text=f"Dexterity: {self.dexterity}")
        self.dexterity_label.pack()
        self.mana_label = tk.Label(master, text=f"Mana: {self.mana}")
        self.mana_label.pack()
        self.energy_label = tk.Label(master, text=f"Energy: {self.energy}/{self.energy_cap}")
        self.energy_label.pack()
        self.xp_label = tk.Label(master, text=f"XP: {self.xp}")
        self.xp_label.pack()
        self.level_label = tk.Label(master, text=f"Level: {self.level}")
        self.level_label.pack()

        # Basic muscle training button
        self.train_button = tk.Button(master, text="Basic Muscle Training", command=self.basic_training)
        self.train_button.pack()

        # Advanced training button (disabled until level 10)
        self.advanced_train_button = tk.Button(master, text="Advanced Training (Unlocks at Level 10)", state=tk.DISABLED, command=self.advanced_training)
        self.advanced_train_button.pack()

        # Weight training button (disabled until level 30)
        self.weight_train_button = tk.Button(master, text="Weight Training (Unlocks at Level 30)", state=tk.DISABLED, command=self.weight_training)
        self.weight_train_button.pack()

        # Unlock magic button (disabled initially, unlocks at level 100)
        self.magic_button = tk.Button(master, text="Unlock Magic (Requires Level 100)", state=tk.DISABLED, command=self.unlock_magic)
        self.magic_button.pack()

        # Start the game loop
        self.update_labels()
        self.energy_regeneration()

    def basic_training(self):
        """Perform basic training to increase strength and XP."""
        if self.energy >= self.training_cost:
            self.strength += 1
            self.xp += 10
            self.energy -= self.training_cost
            self.check_level_up()
            self.update_labels()
        else:
            print("Not enough energy to train!")

    def advanced_training(self):
        """Advanced training unlocked at level 10, increases strength and dexterity with moderate energy cost."""
        advanced_training_cost = self.training_cost + 5  # Moderate increase in energy cost for advanced training
        if self.energy >= advanced_training_cost:
            self.strength += 3  # Advanced training gives more strength
            self.dexterity += 1  # Dexterity improves slightly
            self.xp += 15
            self.energy -= advanced_training_cost
            self.check_level_up()
            self.update_labels()
        else:
            print("Not enough energy for advanced training!")

    def weight_training(self):
        """Weight training unlocked at level 30, increases strength and dexterity, higher energy cost."""
        weight_training_cost = self.training_cost + 10  # Higher energy cost for weight training
        if self.energy >= weight_training_cost:
            self.strength += 5  # Weight training gives significant strength increase
            self.dexterity += 2  # Dexterity improves more with weight training
            self.xp += 25  # Weight training gives higher XP
            self.energy -= weight_training_cost
            self.check_level_up()
            self.update_labels()
        else:
            print("Not enough energy for weight training!")

    def unlock_magic(self):
        """Unlock magical abilities once the player reaches level 100."""
        if self.level >= 100:
            self.mana += 10  # Initial mana when unlocking magic
            self.magic_unlocked = True
            self.level_up_magic()
            self.update_labels()

    def check_level_up(self):
        """Check if the player levels up based on XP."""
        if self.xp >= 50 * self.level:
            self.level += 1
            self.energy_cap += 20  # Increase energy cap with each level
            self.training_cost += 5  # Increase energy cost as levels rise
            print(f"Leveled up! Now at level {self.level}. Energy cap: {self.energy_cap}")

            # Unlock advanced training at level 10
            if self.level >= 10:
                self.advanced_train_button.config(state=tk.NORMAL)

            # Unlock weight training at level 30
            if self.level >= 30:
                self.weight_train_button.config(state=tk.NORMAL)

            # Unlock magic at level 100
            if self.level >= 100:
                self.magic_button.config(state=tk.NORMAL)

    def level_up_magic(self):
        """Enable magic training and use."""
        self.magic_button.config(text="Use Magic (Mana-based)", state=tk.DISABLED)  # Disable after unlocking
        self.train_button.config(text="Advanced Martial Training")

    def energy_regeneration(self):
        """Regenerate energy based on player's level (e.g., +1 energy per second at level 1)."""
        energy_regen_rate = self.level  # Energy regeneration increases with level
        if self.energy < self.energy_cap:
            self.energy = min(self.energy + energy_regen_rate, self.energy_cap)
        self.update_labels()
        self.master.after(1000, self.energy_regeneration)  # Regenerate energy every second

    def update_labels(self):
        """Update the GUI labels to reflect current stats."""
        self.strength_label.config(text=f"Strength: {self.strength}")
        self.dexterity_label.config(text=f"Dexterity: {self.dexterity}")
        self.mana_label.config(text=f"Mana: {self.mana}")
        self.energy_label.config(text=f"Energy: {self.energy}/{self.energy_cap}")
        self.xp_label.config(text=f"XP: {self.xp}")
        self.level_label.config(text=f"Level: {self.level}")

# Run the game with GUI
root = tk.Tk()
game = IncrementalBodyStrengthGame(root)
root.mainloop()
