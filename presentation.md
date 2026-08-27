---
theme: default
paginate: false
backgroundColor: #fff
style: |
  @font-face {
    font-family: 'General Sans';
    src: url('./fonts/GeneralSans-Variable.ttf');
    font-weight: bold;
    font-style: normal;
  }
  
  @font-face {
    font-family: 'Source Serif';
    src: url('./fonts/SourceSerif4-VariableFont_opsz,wght.ttf');
    font-weight: normal;
    font-style: normal;
  }
  
  h1, h2, h3, h4, h5, h6 {
    font-family: 'General Sans', sans-serif;
  }
  
  p, li, code, td {
    font-family: 'Source Serif', serif;
  }

  .footer-image {
    position: absolute;
    left: 10px;
    bottom: -10px;
    width: 300px;
  }
---

![bg left:40% 80%](./mapterhorn-icon-grid.svg)

## Mapterhorn Terrain and Imagery

State of the Map Paris, 28.08.2026

Oliver Wipfli

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## About Me

- Oliver Wipfli
- Based in Zürich, Switzerland
- Consultant in Maps and Location Technology
- Email: oliver.wipfli@leichteralsluft.ch
- GitHub: https://github.com/wipfli
- LinkedIn: <a href="https://www.linkedin.com/in/oliver-wipfli-562258210/">oliver-wipfli-562258210</a>

![bg right:40% 60%](./oliver-wipfli.png)

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## About Mapterhorn

<img src="mapterhorn-logo-main.svg" class="footer-image" />

- Aggregation of open terrain data
- Global low-resolution coverage, local high-resolution lidar
- For hillshading, contour lines, routing, u.s.w.
- Soon also aerial imagery

![bg right:50% 80%](./jura.jpg)

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## History

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />


![bg 90%](./timeline-path.svg)

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Outline

- **Input**
- Aggregation
- Output and Usage
- Sponsors
- Imagery
- Contributing

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Input

- Global: Copernicus 30 m resolution
- Local: High-resolution Lidar
- 70 data producers
- 18 TiB total input data, shared as tarballs
- <a href="https://mapterhorn.com/attribution">mapterhorn.com/attribution</a>
- License CC-BY "or less"

<br /><br /><br />

![bg right:50% 80%](./coverage.jpg)

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Aggregation

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />


![bg 90%](./aggregation-a-path.svg)

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Aggregation

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />


![bg 90%](./aggregation-b-path.svg)

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Aggregation

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />


![bg 90%](./aggregation-c-path.svg)

---

<img src="mapterhorn-logo-main.svg" class="footer-image" />


![bg 90%](./aggregation-example-path.svg)

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Output

- 11.8 TiB elevation tiles
- 458 PMTiles archives
- planet.pmtiles: global, zoom 0-12
- 6-x-y.pmtiles: local, zoom 13-var
- <a href="https://mapterhorn.com/data-access">mapterhorn.com/data-access</a>

<br /><br /><br />

![bg right:50% 80%](./pyramid-path.svg)

---

<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Usage

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

![bg 50%](./examples-path.svg)

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Sponsors

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />


![bg 90%](./sponsors-path.svg)

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Mapterhorn Imagery

- Extend terrain pipeline to aerial imagery
- Alternative to VersaTiles Imagery
- Same producers, "same" format
- Updates more frequently
- Storage: 100+ TiB
- Prepare for Petabytes...

<br /><br /><br />

![bg right:50% 80%](./imagery-path.svg)

---

<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Initial Imagery Coverage

- Global 10 m coverage Sentinel-2
- High-resolution: 18 countries and regions
- Focus first on Europe, then expand to JP, NZ, US, CA, etc...
- First release still in 2026
<br /><br /><br />

![bg right:50% 80%](./imagery-countries.jpg)

---