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

  .footer-image-logo-only {
    position: absolute;
    left: 10px;
    bottom: 10px;
    width: 125px;
  }
---

![bg left:40% 80%](./mapterhorn-icon-grid.svg)

## Mapterhorn Terrain and Imagery

CNG Zürich 2026

Zürich &middot; Oct 29th, 2026

Oliver Wipfli

---

<img src="mapterhorn-icon-grid.svg" class="footer-image-logo-only"/>

<!-- ## Usage

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> -->

![bg 75%](./servers.jpg)

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

<!-- ---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Outline

- Input
- Aggregation
- Output and Usage
- Funding and Governance
- Contributing
- Outlook -->

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

## Input Normalization

- Download from geoportal
- Store LICENSE.pdf and metadata
- Set consistent projection and NoData value
- Store as GeoTiffs with unified compression and internal tiling
- Pack GeoTiffs, license, and metadata into a tarball
- Normalized tarballs available for download at <a href="https://mapterhorn.com/attribution">mapterhorn.com/attribution</a>

<!-- ---
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

## Rounding

- Terrarium: elevation = 256 * red + green + blue / 256 - 2 ** 15
- zoom 19:
  - dx = 0.15
  - dh = 1 / 256
- zoom 18:
  - dx = 0.3
  - dh = 2 / 256
- zoom 17: ...

<br /><br /><br />

![bg right:50% 100%](./rounding-angle-path.svg)

---

<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Rounding

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />


![bg 75%](./rounding-path.svg) -->

---

<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Hardware Requirements

### CPU
- Total number of tiles: 155M
- WebP lossless encoding ~200 ms per tile -> 359 days
- With 32 threads -> 11 days for WebP encoding alone, add 50% for reprojection and merging

### RAM
- Only 200 MiB per thread -> 6.25 GiB for 32 threads
- Tune down GDAL_CACHEMAX and GDAL_MAX_DATASET_POOL_SIZE

<br /><br />

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

## Hosting

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />


![bg 75%](./cloudflare-workers-path.svg)


---

<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Usage

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

![bg 50%](./examples-path.svg)

---

<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Users

- Media
  - ORF, SVT, zeit.de, FAZ, Seattle Times, The Guardian
- Routing
  - GraphHopper
- Outdoor
  - Komoot, outdooractive

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Funding

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />


![bg 90%](./sponsors-path.svg)

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Governance

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />


![bg 50%](./governance.svg)

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Contributing

- Share bug reports, suggest new or updated datasets
  - https://github.com/mapterhorn/mapterhorn
- Contribute financially
  - https://opencollective.com/mapterhorn

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## What's Next

- Aerial Imagery
- Same producers, "same" format, same pipeline
- Challenges: 
  - 10x more data (100+ TiB)
  - Updates more frequently
- Maintenance, maintenance, maintenance

<br /><br /><br />

![bg right:50% 80%](./imagery-path.svg)

<!-- ---

<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Imagery Coverage

- Global: Sentinel-2 imagery 10 m
- High-resolution: 18 countries and regions
- Focus first on Europe, then expand to JP, NZ, US, CA, etc...
- First release still in 2026
<br /><br /><br />

![bg right:50% 80%](./imagery-countries.jpg) -->

---
<img src="mapterhorn-logo-main.svg" class="footer-image" />

## Thank You!

- oliver.wipfli@leichteralsluft.ch
- Get a Mapterhorn sticker or key chain after the talk...
