# homeassistant-metrosaopaulo
Custom sensor for getting São Paulo's Metro Status

Installation instructions
======

Download `sensor.py` and put it inside custom_components/metrosaopaulo under Home assistant config folder.

Configuration
====

Create a new entry in configuration.yaml with the lines you want to monitor, as show bellow

```yaml
sensor:
  - platform: metrosaopaulo
    lines:
      - Linha 1-Azul
      - Linha 2-Verde
      - Linha 3-Vermelha
      - Linha 4-Amarela
      - Linha 5-Lilás
  ```
