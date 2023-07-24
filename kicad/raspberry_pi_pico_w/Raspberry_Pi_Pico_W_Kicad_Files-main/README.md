# Raspberry Pi Pico W (WiFi) SC0918 Module

### Note that this footprint uses pin headers for __THT__ applications.

<br> 
<img src = "./images for README/Pico W 3D view.png" width = "600"/>

<br>

<img src = "./images for README/Pico W symbol.png" width = "600"/>

<br>

https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf

https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf

https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf

<br>

# KiCad 6 Custom Libraries

### Configure Paths

KiCad custom libraries can be made more portable by using custom path designations. These allow the locations of any custom libraries to be modified easily. These can be added in the form of ***Environment Variables***. 
From the main KiCad 6 application, open the ***Preferences*** menu, then select ***Configure Paths***.

<img src = "./images for README/KiCad 6 main app2.png" width = "600"/>

- Use the ```+``` icon at the lower left to add entries to the table.
- An entry can be deleted using the trash can icon at the lower left.
- Note that an environment variable ```<env_var>``` can be referenced using the syntax ```${<env_var>}```, *e.g.*, ```${KICAD6_SYMBOL_USER_DIR}```.
- When finished, select ***OK***.
 
 <img src = "./images for README/KiCad 6 path configuration 2.png" width = "600"/>


### KiCad 6 Library File Formats

In KiCad 6, symbols, footprints, and 3D model files have the following formats.

 | File Type | Description
|-----|-------
| *.kicad_sym 	| Schematic Symbols 
| *.kicad_mod | PCB Footprints  
| *.stp, *.step, *.wrl, *.x3d | 3D Models 

### Add Schematic Symbols

- From the main KiCad 6 application, open the ***Preferences*** menu, then select ***Manage Symbol Libraries***.
- Choose either the ***Global Libraries*** or ***Project Specific Libraries*** table, then select the ```+``` or folder icon at the lower left to 
add one or more existing libraries.
- Note the ***Path Substitutions*** displayed at the bottom. These indicate the ***Environment Variables*** set using the ***Configure Paths***
option.
- A library can be moved up/down using the arrows at the lower left.
- A library can be deleted using the trash can icon at the lower left.
- A library can be activated/deactivated using the checkbox in the ***Active*** column.
- Also note the entry in the ***Library Format*** column. ***KiCad*** indicates that it is using the newest format. Any ***Legacy*** libraries present can be updated to the 
newest format using the ***Migrate Libraries*** button at the lower right.
- An optional ***Nickname*** and/or ***Description*** can be added.
- When finished, select ***OK***.
 
 <img src = "./images for README/KiCad 6 symbol libraries.png" width = "600"/>
 
### Add PCB Footprints

- From the main KiCad 6 application, open the ***Preferences*** menu, then select ***Manage Footprint Libraries***.
- Choose either the ***Global Libraries*** or ***Project Specific Libraries*** table, then select the ```+``` or folder icon at the lower left to 
add one or more existing libraries. Note that other formats, such as Eagle or KiCad Legacy can be used.
- Note the ***Path Substitutions*** displayed at the bottom. These indicate the ***Environment Variables*** set using the ***Configure Paths***
option.
- A library can be moved up/down using the arrows at the lower left.
- A library can be deleted using the trash can icon at the lower left.
- A library can be activated/deactivated using the checkbox in the ***Active*** column.
- Also note the entry in the ***Library Format*** column. ***KiCad*** indicates that it is using the newest format.
- An optional ***Nickname*** and/or ***Description*** can be added.
- When finished, select ***OK***.

 <img src = "./images for README/KiCad 6 footprint libraries.png" width = "600"/>


### Add 3D Models

- From ***Footprint Editor***, select the desired footprint.
- Double-click to open it for editing.
- From the ***File*** menu, select ***Footprint Properties***. Alternatively, select the ***Edit Footprint Properties*** icon in the menu bar.
- Select the ***3D Models*** tab.
- Select the ```+``` or folder icon at the lower left to add a model.
- Note that the ***Configure Paths*** button at the lower right can be used to access the ***Environment Variables*** table described above.
- A model can be deleted using the trash can icon at the lower left.
- A model can be displayed/hidden using the checkbox in the ***Show*** column.
- The ***Scale***, ***Rotation***, and ***Offset*** controls located at the lower left can be used to properly position the model.
- When finished, select ***OK***.
- Be sure to save any changes before exiting the ***Footprint Editor*** using the ***Save*** or ***Save As*** command.

 <img src = "./images for README/KiCad 6 3D models 2.png" width = "600"/>


### Resources

https://circuitstate.com/tutorials/how-to-install-kicad-version-6-and-organize-part-libraries/

https://techexplorations.com/blog/kicad/kicad-6-review-new-and-improved-features/

