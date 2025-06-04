# Pose Visualizer

This project provides two interactive 3D arrow visualizer tools using Python and matplotlib:

## 1. arrow_gui.py
- Visualizes a 3D arrow at an arbitrary XYZ position.
- The orientation is controlled by user-adjustable yaw, pitch, and roll angles (in degrees) via sliders.

## 2. arrow_gui_vector.py
- Visualizes a 3D arrow at an arbitrary XYZ position.
- The direction is controlled directly by user-adjustable X, Y, Z direction vector components via sliders.

## Executables

Both scripts have been compiled to standalone Windows executables using PyInstaller:
- `dist/arrow_gui.exe`
- `dist/arrow_gui_vector.exe`

You can run these `.exe` files on any Windows machine without needing Python installed.

## How to Use
1. Download the desired `.exe` from the `dist` folder.
2. Double-click to launch the interactive GUI.
3. Adjust the sliders to change the arrow's orientation or direction in real time.

## Building from Source
If you want to build the executables yourself:
1. Install requirements: `pip install -r requirements.txt`
2. Install PyInstaller: `pip install pyinstaller`
3. Build: `pyinstaller --onefile arrow_gui.py` and/or `pyinstaller --onefile arrow_gui_vector.py`

---

For any questions, open an issue on the repository.
