
# Odoo Core
![Odoo Version](https://img.shields.io/badge/Odoo-18.0-blue.svg)
![License](https://img.shields.io/badge/License-LGPL--3-green.svg)

# Overview
This module enhances the Odoo developer experience by adding a new tab to the "Models" menu. It provides a comprehensive list of all window actions, server actions, and report actions that are bound to a specific model, along with their External IDs. This helps developers and administrators quickly audit and manage a model's related actions without navigating through multiple menus.

# Features
- **New `Actions` Tab:** A dedicated tab on the `ir.model` form view to display bound actions.
- **Action Listing:** Lists all `ir.actions` records (`act_window`, `server`, `report`, etc.) that are bound to the current model.
- **External ID:** Displays the External XML ID for each action, which is essential for development and migration tasks.
- **Simplified Navigation:** Provides a direct link to the action's form view for easy editing.

# Installation
1.  Add the `odoo_core` directory to your Odoo `addons` path.
2.  Log in as a user with administrative rights.
3.  Go to the Apps menu and update your apps list.
4.  Search for "Odoo Core" and click the "Install" button.

# Usage
1.  Navigate to **Settings > Technical > Database Structure > Models**.
2.  Select any model from the list (e.g., `Contacts` / `res.partner`).
3.  You will now see a new `Actions` tab on the form view.
4.  Click the tab to see a list of all actions bound to the `res.partner` model.

# Contributing
Contributions are welcome! If you find a bug or have an idea for an improvement, please feel free to open an issue or submit a pull request on this repository.

**Author:**
Mohand KG

**License:**
This module is licensed under the [LGPL-3 License](https://www.gnu.org/licenses/lgpl-3.0.en.html).

# Example

<img width="1910" height="961" alt="cover" src="https://github.com/user-attachments/assets/b9ec6a98-d198-4d34-ad00-bf97225c9344" />
