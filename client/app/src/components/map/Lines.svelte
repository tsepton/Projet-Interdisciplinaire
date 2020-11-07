<script>
  import { getContext } from "svelte";
  import { key } from "../../lib/mapbox.js";

  const { getMap } = getContext(key);
  const map = getMap();

  export let lines;

  map.on("load", () =>
    lines.features.forEach((line, index) => {
      map.addSource(`${index}-route`, {
        type: "geojson",
        data: line,
      });
      map.addLayer({
        id: `${index}-route`,
        type: "line",
        source: `${index}-route`,
        layout: {
          "line-join": "round",
          "line-cap": "round",
        },
        paint: {
          "line-color": line.properties.COLOR_HEX,
          "line-width": 1.7,
        },
      });
    })
  );
</script>
