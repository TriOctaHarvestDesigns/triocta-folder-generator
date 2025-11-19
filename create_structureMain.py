import os, json, copy

# =============================
# Tri-Octa Harvest Designs
# Folder Generator v1.2
# =============================

def create_folder(path):
    """Safely create a folder if it doesn't exist."""
    os.makedirs(path, exist_ok=True)

def sanitize_name(name):
    """Clean illegal filename characters."""
    forbidden = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for c in forbidden:
        name = name.replace(c, "_")
    return name.strip()

def rename_project_prefixes(structure, num):
    """Recursively rename P001 prefixes to match project number."""
    if "folders" in structure:
        new_folders = {}
        for name, sub in structure["folders"].items():
            new_name = name.replace("P001", f"P{num:03d}")
            rename_project_prefixes(sub, num)
            new_folders[new_name] = sub
        structure["folders"] = new_folders

def create_structure(base_path, structure):
    """Recursively create folders and files from JSON."""
    for folder_name, content in structure.get("folders", {}).items():
        folder_path = os.path.join(base_path, sanitize_name(folder_name))
        create_folder(folder_path)
        create_structure(folder_path, content)

    for f in structure.get("files", []):
        if isinstance(f, dict) and "name" in f and "content" in f:
            with open(os.path.join(base_path, sanitize_name(f["name"])), "w", encoding="utf-8") as file:
                file.write(f["content"])
        elif isinstance(f, str):
            open(os.path.join(base_path, sanitize_name(f)), "a").close()  # blank file

def create_projects(base_path, base_structure, num_projects):
    """Create numbered Project_00# folders using base structure."""
    for i in range(1, num_projects + 1):
        proj_name = f"Project_{i:03d}"
        proj_path = os.path.join(base_path, proj_name)
        create_folder(proj_path)

        proj_structure = copy.deepcopy(base_structure)
        rename_project_prefixes(proj_structure, i)
        create_structure(proj_path, proj_structure)

def preview_structure(name, structure, indent=0):
    """Show folder preview before building."""
    spacer = "│  " * indent
    tree = f"{spacer}├─ {name}/\n"
    for f in structure.get("files", []):
        if isinstance(f, dict):
            tree += f"{spacer}│  └─ {f['name']}\n"
        elif isinstance(f, str):
            tree += f"{spacer}│  └─ {f}\n"
    for sub, subcont in structure.get("folders", {}).items():
        tree += preview_structure(sub, subcont, indent + 1)
    return tree

def main():
    print("\n=== Tri-Octa Harvest Designs · Folder Generator v1.2 ===\n")
    print("Options:")
    print("1. Generate folder structure from JSON")
    print("2. Create sequential folders only\n")

    choice = input("Choose an option (1/2): ").strip() or "1"

    if choice == "2":
        name = input("Base folder name (default: Folder): ").strip() or "Folder"
        count = int(input("How many folders to create? (default: 5): ") or 5)
        for i in range(1, count + 1):
            folder_name = f"{name}_{i:03d}"
            create_folder(folder_name)
        print(f"\n✅ Created {count} sequential folders.\n")
        return

    # === Option 1: JSON-based structure ===
    json_name = input("Enter JSON filename (default: structure.json): ").strip() or "structure.json"
    root_name = input("Enter root folder name (default: 000 DesktopLayer 001 - Rename): ").strip() or "000 DesktopLayer 001 - Rename"
    num_projects = int(input("Enter number of Project folders to create (default: 1): ") or 1)

    # Load structure
    with open(json_name, "r", encoding="utf-8") as f:
        structure = json.load(f)

    print("\n=== Preview Folder Structure ===")
    print(preview_structure(root_name, structure))

    confirm = input("Proceed with creation? (y/n): ").strip().lower()
    if confirm != "y":
        print("❌ Cancelled.")
        return

    base_path = os.path.join(os.getcwd(), sanitize_name(root_name))
    create_folder(base_path)

    # Create base structure
    create_structure(base_path, structure)

    # Create project folders
    if "Projects" in structure["folders"]:
        proj_base = structure["folders"]["Projects"]["folders"]["Project_001"]
        proj_root = os.path.join(base_path, "Projects")
        create_projects(proj_root, proj_base, num_projects)

    print(f"\n✅ Folder structure successfully created at: {base_path}\n")

if __name__ == "__main__":
    main()
