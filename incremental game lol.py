import tkinter as tk

class IncrementalGameWithEnhancements:
    def __init__(self, master):
        self.master = master
        self.master.title("Incremental Game")

        # Initial game state
        self.gold = 0  # Primary resource
        self.wood = 0  # Secondary resource
        self.gold_per_second = 1
        self.wood_per_second = 0.5  # Collect wood slower than gold
        self.upgrade_cost = 10
        self.auto_upgrade_enabled = False  # Automate upgrades if true

        # Labels for resources
        self.gold_label = tk.Label(master, text=f"Gold: {self.gold}")
        self.gold_label.pack()
        self.wood_label = tk.Label(master, text=f"Wood: {self.wood}")
        self.wood_label.pack()

        # Labels for resource collection rate
        self.gold_rate_label = tk.Label(master, text=f"Gold rate: {self.gold_per_second} gold/second")
        self.gold_rate_label.pack()
        self.wood_rate_label = tk.Label(master, text=f"Wood rate: {self.wood_per_second} wood/second")
        self.wood_rate_label.pack()

        # Upgrade button
        self.upgrade_button = tk.Button(master, text=f"Buy Upgrade (Cost: {self.upgrade_cost} gold)", command=self.upgrade)
        self.upgrade_button.pack()

        # Automation button
        self.auto_upgrade_button = tk.Button(master, text="Enable Auto Upgrade", command=self.toggle_auto_upgrade)
        self.auto_upgrade_button.pack()

        # Start collecting resources every second
        self.run_game()

    def collect_resources(self):
        """Automatically collects gold and wood based on the rate."""
        self.gold += self.gold_per_second
        self.wood += self.wood_per_second
        self.update_labels()

        # Automatically buy upgrades if auto-upgrade is enabled and we have enough gold
        if self.auto_upgrade_enabled and self.gold >= self.upgrade_cost:
            self.upgrade()

    def upgrade(self):
        """Allows the player to buy an upgrade if they have enough gold."""
        if self.gold >= self.upgrade_cost:
            self.gold -= self.upgrade_cost  # Deduct the cost from gold
            self.gold_per_second += 1  # Increase the gold collection rate
            self.wood_per_second += 0.5  # Increase the wood collection rate
            self.upgrade_cost *= 2  # Double the cost for the next upgrade
            self.update_labels()
            self.upgrade_button.config(text=f"Buy Upgrade (Cost: {self.upgrade_cost} gold)")
        self.update_upgrade_button_state()

    def update_labels(self):
        """Updates all the labels in the GUI to reflect the current game state."""
        self.gold_label.config(text=f"Gold: {self.gold:.1f}")
        self.wood_label.config(text=f"Wood: {self.wood:.1f}")
        self.gold_rate_label.config(text=f"Gold rate: {self.gold_per_second} gold/second")
        self.wood_rate_label.config(text=f"Wood rate: {self.wood_per_second} wood/second")

    def toggle_auto_upgrade(self):
        """Toggles the auto-upgrade feature on or off."""
        self.auto_upgrade_enabled = not self.auto_upgrade_enabled
        if self.auto_upgrade_enabled:
            self.auto_upgrade_button.config(text="Disable Auto Upgrade")
        else:
            self.auto_upgrade_button.config(text="Enable Auto Upgrade")

    def update_upgrade_button_state(self):
        """Disables or enables the upgrade button based on the player's gold."""
        if self.gold >= self.upgrade_cost:
            self.upgrade_button.config(state=tk.NORMAL)
        else:
            self.upgrade_button.config(state=tk.DISABLED)

    def run_game(self):
        """Main game loop: collects resources every second."""
        self.collect_resources()
        self.update_upgrade_button_state()
        self.master.after(1000, self.run_game)  # Run every second

# Run the game with GUI
root = tk.Tk()
game = IncrementalGameWithEnhancements(root)
root.mainloop()
