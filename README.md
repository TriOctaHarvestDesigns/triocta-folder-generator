# triocta-folder-generator
“A set of Python tools for folder generation, chat export splitting, and image metadata cleaning.”  “TriOcta productivity tools for creators, developers, and Obsidian users.”  “Automation utilities: folder generator, universal splitter, and metadata scrubber.”

# 📁 Folder Generator Utility — v1.2

**By Tri-Octa Harvest Designs**

Create structured, professional folder systems instantly — from a JSON blueprint or with a single line of input.
Perfect for artists, students, freelancers, and researchers who love clean workspaces.

---

## 🚀 Quick Start

1. Place your `create_structureMain.py` and `structure.json` files in the same folder.
2. Open **PowerShell**, **Terminal**, or **VS Code terminal** in that directory.
3. Run the command:

   ```
   python create_structureMain.py
   ```
4. Choose one of two options:

   * **Option 1:** Build folders from your `structure.json` blueprint
   * **Option 2:** Quickly generate numbered folders (like Folder_001, Folder_002, etc.)

---

## ⚙️ Option 1 — JSON Structure Mode

When you pick **Option 1**, the script will:

* Ask for your JSON filename (defaults to `structure.json`)
* Ask for a **root folder name** (defaults to `000 DesktopLayer 001 - Rename`)
* Ask how many **Project_00#** folders you want to make (default: 1)
* Show a full **preview tree** of the folder structure before building
* Confirm before creating anything

✨ **Smart Features:**

* Automatically numbers internal project folders (`P001`, `P002`, etc.)
* Avoids recursive “Audio/Audio” duplication
* Includes README and `.gitignore` generation (if in your JSON)
* Works on Windows, macOS, or Linux
* Keeps your workspace modular, portable, and professional

---

## 🧰 Option 2 — Sequential Folder Mode

Don’t need a full structure? Use this quick-create tool.

* Prompts for a base name (e.g. `Folder`)
* Asks how many you want (default: 5)
* Instantly generates `Folder_001`, `Folder_002`, etc.

Great for:

* Multi-day project dumps
* Batch renders or photo sets
* Client folders or versioning

---

## 🧩 Customizing Your JSON

* Open `structure.json` in any text editor (VS Code, Notepad++, etc.)
* Add, remove, or rename folder and file entries
* Example snippet:

  ```json
  {
    "root": "000 DesktopLayer 001 - Rename",
    "folders": {
      "Audio": {},
      "Images": {"folders": {"PNG": {}, "JPG": {}}},
      "Projects": {
        "folders": {
          "Project_001": {
            "folders": {
              "P001 - Audio": {},
              "P001 - Notes": {}
            }
          }
        }
      }
    },
    "files": [{"name": "README.md", "content": "Custom workspace."}]
  }
  ```

Save your edit as `structure_custom.json` and run the script again — it will detect your custom file when prompted.

---

## 🧭 Notes & Tips

* Works fully **offline** — no internet required
* All files are written **locally** and safely
* You can duplicate this tool anywhere (USB drives, cloud folders, etc.)
* Ideal for repeatable folder setups across systems

---

### 🪶 Credits

Designed by **Tri-Octa Harvest Designs (2025)**
Part of the **Productivity Tools Collection** — paired with the **ChatGPT Splitter Utility**
THIS PARTICULAR TOOL IS FREE. MIT License - Permissive license allows users to freely user, modify and distribute.
