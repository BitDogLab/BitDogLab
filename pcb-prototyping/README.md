# PCB Prototyping / Prototipagem de PCB

[English](#english) | [Portugues](#portugues)

## English

This directory contains the public PCB design and fabrication files for the BitDogLab boards.

The folder name is `pcb-prototyping` because not every file here was created in KiCad. It includes KiCad projects, Altium projects, manufacturing outputs, 3D models, images, BOM files and support libraries.

### Folder Structure

```text
pcb-prototyping/
+-- BitDogLab V6/
|   +-- bitdoglab-through-hole/
|   +-- bitdoglab-smd/
|   +-- component-libraries/
+-- BitDogLab V7/
    +-- Project Outputs for BitDogLab V7/
    +-- __Previews/
    +-- History/
    +-- bitdoglab-v7-pcb-top-view.png
    +-- bitdoglab-v7-pcb-bottom-view.png
```

### BitDogLab V6

BitDogLab V6 was developed in KiCad.

- `bitdoglab-through-hole/`: through-hole/DIY KiCad project files.
- `bitdoglab-smd/`: SMD KiCad project files, schematic, PCB layout, fabrication outputs and board images.
- `component-libraries/`: symbols, footprints, 3D models and support files used by the KiCad projects.

Common KiCad files found here:

- `.kicad_pro`: KiCad project file.
- `.kicad_sch`: schematic file.
- `.kicad_pcb`: PCB layout file.
- `.kicad_mod`: footprint file.
- `.kicad_sym`: symbol library file.
- `.step` / `.stp`: 3D model files.
- `.zip`: fabrication package when available.
- `.csv` / `.xlsx`: BOM or component data when available.

### BitDogLab V7

BitDogLab V7 was developed in Altium Designer.

<p align="center">
  <img src="BitDogLab%20V7/bitdoglab-v7-pcb-top-view.png" alt="BitDogLab V7 PCB top view" width="45%">
  <img src="BitDogLab%20V7/bitdoglab-v7-pcb-bottom-view.png" alt="BitDogLab V7 PCB bottom view" width="45%">
</p>

Main files:

- `BitDogLab V7.PrjPcb`: Altium PCB project.
- `BitDogLab V7.SchDoc`: Altium schematic document.
- `BitDogLab V7.PcbDoc`: Altium PCB layout document.
- `BitDogLab V7.OutJob`: Altium output job configuration.
- `BitDogLab V7.pdf`: exported schematic/documentation PDF.
- `BitDogLab V7_Lista de Materiais com Custo.xlsx`: bill of materials with cost information.
- `BitDogLab V7_Gerber.rar`: Gerber fabrication package.
- `Project Outputs for BitDogLab V7/`: manufacturing outputs exported from the project, including Gerber layers, drill reports, BOM, pick-and-place and 3D STEP model.
- `bitdoglab-v7-pcb-top-view.png`: technical top view image of the PCB.
- `bitdoglab-v7-pcb-bottom-view.png`: technical bottom view image of the PCB.

### Public Fabrication Files

Gerber files are publicly available for fabrication. They can be used by PCB manufacturers to produce the board.

Before ordering a board, review the fabrication package, BOM, drill files and pick-and-place data. Manufacturing settings can vary by supplier, so the files should always be checked in a Gerber viewer or CAM tool before production.

### Notes

- KiCad is recommended for opening and editing the BitDogLab V6 project files.
- Altium Designer is recommended for opening and editing the BitDogLab V7 source project files.
- Gerber and drill files can usually be inspected with vendor tools or independent Gerber viewers.
- Board images are provided as visual references and are not a replacement for fabrication data.

## Portugues

Esta pasta contem os arquivos publicos de projeto e fabricacao das placas BitDogLab.

O nome da pasta e `pcb-prototyping` porque nem todo arquivo aqui foi desenvolvido no KiCad. Ela inclui projetos KiCad, projetos Altium, arquivos de fabricacao, modelos 3D, imagens, listas de materiais e bibliotecas de apoio.

### Estrutura de Pastas

```text
pcb-prototyping/
+-- BitDogLab V6/
|   +-- bitdoglab-through-hole/
|   +-- bitdoglab-smd/
|   +-- component-libraries/
+-- BitDogLab V7/
    +-- Project Outputs for BitDogLab V7/
    +-- __Previews/
    +-- History/
    +-- bitdoglab-v7-pcb-top-view.png
    +-- bitdoglab-v7-pcb-bottom-view.png
```

### BitDogLab V6

A BitDogLab V6 foi desenvolvida no KiCad.

- `bitdoglab-through-hole/`: arquivos KiCad da versao through-hole/DIY.
- `bitdoglab-smd/`: arquivos KiCad da versao SMD, esquematico, layout da placa, saidas de fabricacao e imagens da placa.
- `component-libraries/`: simbolos, footprints, modelos 3D e arquivos de apoio usados pelos projetos KiCad.

Arquivos KiCad comuns nesta pasta:

- `.kicad_pro`: arquivo de projeto KiCad.
- `.kicad_sch`: arquivo de esquematico.
- `.kicad_pcb`: arquivo de layout da PCB.
- `.kicad_mod`: arquivo de footprint.
- `.kicad_sym`: biblioteca de simbolos.
- `.step` / `.stp`: modelos 3D.
- `.zip`: pacote de fabricacao quando disponivel.
- `.csv` / `.xlsx`: BOM ou dados de componentes quando disponiveis.

### BitDogLab V7

A BitDogLab V7 foi desenvolvida no Altium Designer.

<p align="center">
  <img src="BitDogLab%20V7/bitdoglab-v7-pcb-top-view.png" alt="Vista superior da PCB BitDogLab V7" width="45%">
  <img src="BitDogLab%20V7/bitdoglab-v7-pcb-bottom-view.png" alt="Vista inferior da PCB BitDogLab V7" width="45%">
</p>

Arquivos principais:

- `BitDogLab V7.PrjPcb`: projeto PCB do Altium.
- `BitDogLab V7.SchDoc`: documento de esquematico do Altium.
- `BitDogLab V7.PcbDoc`: documento de layout da PCB no Altium.
- `BitDogLab V7.OutJob`: configuracao de saidas do Altium.
- `BitDogLab V7.pdf`: PDF exportado com esquematico/documentacao.
- `BitDogLab V7_Lista de Materiais com Custo.xlsx`: lista de materiais com informacoes de custo.
- `BitDogLab V7_Gerber.rar`: pacote Gerber para fabricacao.
- `Project Outputs for BitDogLab V7/`: saidas de fabricacao exportadas do projeto, incluindo camadas Gerber, relatorios de furo, BOM, pick-and-place e modelo 3D STEP.
- `bitdoglab-v7-pcb-top-view.png`: imagem tecnica da face superior da PCB.
- `bitdoglab-v7-pcb-bottom-view.png`: imagem tecnica da face inferior da PCB.

### Arquivos Publicos para Fabricacao

Os arquivos Gerber estao disponiveis publicamente para fabricacao. Eles podem ser usados por fabricantes de PCB para produzir a placa.

Antes de encomendar uma placa, revise o pacote de fabricacao, a BOM, os arquivos de furo e os dados de pick-and-place. As configuracoes de fabricacao podem variar conforme o fornecedor, entao os arquivos devem sempre ser conferidos em um visualizador Gerber ou ferramenta CAM antes da producao.

### Observacoes

- O KiCad e recomendado para abrir e editar os arquivos da BitDogLab V6.
- O Altium Designer e recomendado para abrir e editar os arquivos fonte da BitDogLab V7.
- Arquivos Gerber e de furo normalmente podem ser inspecionados em ferramentas dos fabricantes ou em visualizadores Gerber independentes.
- As imagens da placa servem como referencia visual e nao substituem os arquivos de fabricacao.
